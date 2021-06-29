import time
import glob
import re
import openpyxl
import xlrd
import pytoml
import os
import shutil
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# Defined variables
login_payload = {'phone_num': '91784364', 'pw': 'fupin123'}
login_url = 'https://login.taosj.com/?redirectURL=https%3A%2F%2Fwww.taosj.com%2F'
taosj_meta_data = r'C:\Users\Dell\IdeaProjects\TaoSJDL\src\TaoSJ Meta'
download_dump_folder = r'C:\Users\Dell\IdeaProjects\TaoSJDL\src\download-dump'

# config path
CONFIG_PATH = 'config.toml'

# Arguments for chrome webdriver
option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("""user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 
                        Chrome/58.0.3029.110 Safari/537.36""")
option.add_argument("--incognito")
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
prefs = {'download.default_directory' : r'C:\Users\Dell\IdeaProjects\TaoSJDL\src\download-dump'}
option.add_experimental_option('prefs', prefs)

# Read config.toml file
def read_config(path):
    config = pytoml.load(open(path, 'rb'))
    return config


def read_xlsx_file(xlsx_file_path):
    wb = openpyxl.load_workbook(xlsx_file_path)
    ws = wb.active
    brand = ws['C2'].value
    category = ws['D2'].value
    return brand, category


def read_xls_file(xls_file_path):
    wb = xlrd.open_workbook(xls_file_path)
    ws = wb.sheet_by_index(0)
    brand = ws.cell_value(rowx=1, colx=2)
    category = ws.cell_value(rowx=1, colx=3)
    return brand, category

# TODO: Edit function to include all brands based on config.toml
def sort_file_path(sku_dict, overall_sku_dict):
    if sku_dict['brand'] == '久年':
        if '花胶/鱼胶' in sku_dict['category']:
            sku_dict['dest_path'] = config['file_dest']['jn_fm']
            overall_sku_dict.append(sku_dict)

        elif '海参' in sku_dict['category']:
            sku_dict['dest_path'] = config['file_dest']['jn_sc']
            overall_sku_dict.append(sku_dict)
    else:
        overall_sku_dict.append(sku_dict)
    return overall_sku_dict


def click_xpath(html_xpath):
    element = driver.find_element_by_xpath(html_xpath)
    element.click()


def send_keys(html_xpath, key):
    element = driver.find_element_by_xpath(html_xpath)
    element.send_keys(key)


def clear_text_field(html_xpath):
    element = driver.find_element_by_xpath(html_xpath)
    element.clear()


def login_process():
    try:
        # Select country code
        country_xpath = '//*[@id="J_Mod_Login"]/form/div[2]/span'
        click_xpath(country_xpath)

        singapore_xpath = '//*[@id="J_Mod_Login"]/form/div[2]/div/p[6]'
        click_xpath(singapore_xpath)

        time.sleep(3)

        # Input phone num and pw
        phone_num = '//*[@id="J_Mod_Login"]/form/div[2]/input'
        send_keys(phone_num, login_payload['phone_num'])

        passw = '//*[@id="J_Mod_Login"]/form/div[3]/input'
        send_keys(passw, login_payload['pw'])

        time.sleep(3)

        # Click on login button
        login = '//*[@id="T_Login"]'
        click_xpath(login)
        print("Log In Successful.")

    except Exception as e:
        print(e)


def mouse_over(xpath):
    element = driver.find_element_by_xpath(xpath)
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()

#TODO: Replace time.sleep with wait till element appears
def shop_data():
    try:
        # Navigate to '找宝贝' Tab
        china_services = '//*[@id="J_c-data-top"]/div/div[2]/ul/li[2]/div[2]'  # '国内电商‘ Element
        mouse_over(china_services)

        shop_data = '//*[@id="J_c-data-top"]/div/div[2]/ul/li[2]/div[3]/div/div[1]/a[3]'  # '店铺数据’ Element
        click_xpath(shop_data)

        time.sleep(5)

        driver.switch_to.window(driver.window_handles[-1])
        sku_lookup = '//*[@id="header"]/div/div[6]/div/div[1]/div/ul/li[2]/a'
        click_xpath(sku_lookup)
        print("Successfully Navigated to '找宝贝‘ Tab. ")

    except Exception as e:
        print(e)


def scrape_sku(sku_id):
    # Input sku_id into search bar
    sku_input_field_xpath = '//*[@id="search"]'
    send_keys(sku_input_field_xpath, sku_id)

    # Click on search button
    sku_search_button = '//*[@id="header"]/div/div[6]/div/div[1]/div/div/a'
    click_xpath(sku_search_button)

    time.sleep(5)

    # Look for SKU in search results
    # Error handling: Can either be found or not be found

    try:
        sku_exists = driver.find_element_by_xpath(f'//a[contains(@href,"//item.taobao.com/item.htm?id={sku_id}")]')
        sku_data_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[4]/div/div/div[2]/table/tbody/tr/td[7]/div/div/a')
        print(f"{sku_id} exists. Found data on it.")
        download_data(sku_data_button, sku_id)
        driver.switch_to.window(driver.window_handles[-1])
        clear_text_field(sku_input_field_xpath)

    except NoSuchElementException:

        try:
            sku_no_exist = driver.find_element_by_xpath('//*[@id="container"]/div/div[4]/div/div/div[1]/form/div/span[1]')
            print(f"{sku_id} does not exist.")
            clear_text_field(sku_input_field_xpath)

        except NoSuchElementException:
            sku_no_exist = driver.find_element_by_xpath('//div[text()="暂无数据"]')
            print(f"{sku_id} does not exist.")
            clear_text_field(sku_input_field_xpath)

# TODO: Deal with long waiting time because of hanging, implement refresh function
def download_data(selenium_element, sku_id):
    selenium_element.click()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[-1])

    download_button = '//*[@id="itemMain"]/div/div[4]/div/div[1]/a'
    click_xpath(download_button)
    print(f"Downloading data for {sku_id}.....")
    time.sleep(10)
    print("Download completed.")

    driver.close()
    time.sleep(5)

def read_directory(folder_path):
    search = folder_path + '\\*.xls'
    list_files = glob.glob(search,recursive=True)
    return list_files

def rename_files(list_files):
    for files in list_files:
        pre, ext = os.path.splitext(files)
        os.rename(files, pre + '.xlsx')

def shift_files(download_sku, old_file_path, list_of_dicts):
    for dicts in list_of_dicts:
        if dicts['sku_id'] == download_sku:
            file_dest = dicts['dest_path']
            print(f"Shifting {download_sku} from {old_file_path} to {file_dest}...")
            shutil.copy(old_file_path, file_dest)
            print("Successfully copied.")

if __name__ == '__main__':

    # Obtain list of files containing SKU IDs to scrape from directory
    list_of_xlsx = glob.glob('**/TaoSJ Meta/*.xlsx', recursive=True) + \
                   glob.glob('**/TaoSJ Meta/*.xls', recursive=True)
    len_list_of_xlsx = len(list_of_xlsx)
    print(f"Found {len_list_of_xlsx} SKUs to scrape.")

    # Obtain data regarding each SKU, outputs destination path(str) for downloading
    sku_id_regex = re.compile('\\\\([0-9]*).xls')
    list_sku_id = []
    brands = []
    categories = []
    overall_sku_info = []
    config = read_config(CONFIG_PATH)

    for filepath in list_of_xlsx:

        sku_info = {}
        # Get SKU_ID and put inside sku_info dictionary
        sku_id = sku_id_regex.search(filepath).group(1)
        list_sku_id.append(sku_id)
        sku_info['sku_id'] = sku_id

        # Get brand and put inside sku_info_dictionary
        try:
            brand, category = read_xlsx_file(filepath)
            brands.append(brand)
            categories.append(category)
            sku_info['brand'] = brand
            sku_info['category'] = category

        except Exception:
            brand, category = read_xls_file(filepath)
            brands.append(brand)
            categories.append(category)
            sku_info['brand'] = brand
            sku_info['category'] = category

        # Use sort_file_path function to add file dest paths to each ID
        overall_sku_info = sort_file_path(sku_info, overall_sku_info)

    # End of file meta reading to get list of SKUs to scrape from TaoSJ, as well as their
    # File Destination Paths to download to

    # Login Process using selenium starts here
    driver = webdriver.Chrome('chromedriveedit.exe', options=option)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })
    driver.get(login_url)
    wait = WebDriverWait(driver, 10)
    login_process()

    time.sleep(5)

    # Navigate to '找宝贝' Tab
    shop_data()

    for sku in overall_sku_info:
        taosj_sku_id = sku['sku_id']
        taosj_brand = sku['brand']

        #TODO: Edit to remove restriction on 'JN'
        if taosj_brand == '久年':
            scrape_sku(taosj_sku_id)

    # Download of files to download-dump completed

    # Start shifting files to correct dest path
    download_dump_files = read_directory(download_dump_folder)

    # Rename file type from xls to xlsx
    #rename_files(download_dump_files)
    new_download_dump_files = read_directory(download_dump_folder)

    sku_id_regex_download = re.compile('_([0-9]*)_')

    for files in new_download_dump_files:
        sku_id_download = sku_id_regex_download.search(files).group(1)
        shift_files(sku_id_download,files,overall_sku_info)
