import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

#Defined variables
login_payload = {'phone_num': '91784364', 'pw': 'fupin123'}
login_url = 'https://login.taosj.com/?redirectURL=https%3A%2F%2Fwww.taosj.com%2F'


#Arguments for chrome webdriver
option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("""user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 
                        Chrome/58.0.3029.110 Safari/537.36""")
option.add_argument("--incognito")
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

def click_xpath(html_xpath):
    element = driver.find_element_by_xpath(html_xpath)
    element.click()

def send_keys(html_xpath, key):
    element = driver.find_element_by_xpath(html_xpath)
    element.send_keys(key)

def login_process():
    try:
        #Select country code
        country_xpath = '//*[@id="J_Mod_Login"]/form/div[2]/span'
        click_xpath(country_xpath)

        singapore_xpath = '//*[@id="J_Mod_Login"]/form/div[2]/div/p[6]'
        click_xpath(singapore_xpath)

        time.sleep(3)

        #Input phone num and pw
        phone_num = '//*[@id="J_Mod_Login"]/form/div[2]/input'
        send_keys(phone_num, login_payload['phone_num'])

        passw = '//*[@id="J_Mod_Login"]/form/div[3]/input'
        send_keys(passw, login_payload['pw'])

        time.sleep(3)

        #Click on login button
        login = '//*[@id="T_Login"]'
        click_xpath(login)
        print("Log In Successful.")

    except Exception as e:
        print(e)

def mouse_over(xpath):
    element = driver.find_element_by_xpath(xpath)
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()


def shop_data():
    try:
        #Navigate to '找宝贝' Tab
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

if __name__ == '__main__':
    #Login Process
    driver = webdriver.Chrome('chromedriveedit.exe', options=option)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })
    driver.get(login_url)
    wait = WebDriverWait(driver,10)
    login_process()

    time.sleep(5)

    shop_data()














