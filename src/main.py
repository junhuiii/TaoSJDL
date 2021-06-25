import time
from selenium import webdriver
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

def taosj_login_xpath(html_xpath):
    element = driver.find_element_by_xpath(html_xpath)
    element.click()

def send_keys(html_xpath, key):
    element = driver.find_element_by_xpath(html_xpath)
    element.send_keys(key)

def login_process():
    try:
        #Select country code
        country_xpath = '//*[@id="J_Mod_Login"]/form/div[2]/span'
        taosj_login_xpath(country_xpath)

        singapore_xpath = '//*[@id="J_Mod_Login"]/form/div[2]/div/p[6]'
        taosj_login_xpath(singapore_xpath)

        time.sleep(3)

        #Input phone num and pw
        phone_num = '//*[@id="J_Mod_Login"]/form/div[2]/input'
        send_keys(phone_num, login_payload['phone_num'])

        passw = '//*[@id="J_Mod_Login"]/form/div[3]/input'
        send_keys(passw, login_payload['pw'])

        time.sleep(3)

        #Click on login button
        login = '//*[@id="T_Login"]'
        taosj_login_xpath(login)
        print("Log In Successful.")

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









