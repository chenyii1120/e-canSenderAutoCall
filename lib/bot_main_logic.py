from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import time
import lib.status as ss
import lib.file_output as file_output
import traceback



def sender_call():

    try:

        status = ss.Status()

        driver = webdriver.Chrome(config.BROWSER_DRIVER_PATH)

        driver.get("http://query3.e-cann.com.tw/wedi2012/wedilogin.asp")

        time.sleep(5)

        id_input = driver.find_element_by_name('CUST_ID')
        id_input.send_keys(config.ID)
        time.sleep(1)
        pws_input = driver.find_element_by_name('CUST_PASSWORD')
        pws_input.send_keys(config.PASSWORD)
        time.sleep(1)
        captcha = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[5]/td[2]/font/b/font')
        captcha_input = driver.find_element_by_name('KEY_RND')
        captcha_input.send_keys(captcha.text)
        time.sleep(1)
        login_btn = driver.find_element_by_name('LoginSubmit')
        login_btn.click()

        time.sleep(10)

        navi_title = driver.find_element_by_xpath('//*[@id="delivery_work"]/span')
        navi_title.click()
        time.sleep(0.5)
        sender_call = driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul/li[5]/a')
        sender_call.click()
        time.sleep(1)
        driver.switch_to.frame("datamain")
        notify_btn = driver.find_element_by_css_selector('#btnsubmit')
        notify_btn.click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

    except:
        status.result = False
        status.crash_info = traceback.format_exc()
        file_output.print_crash_report(status)

    else:
        status.result = True

    finally:
        file_output.print_log(status)
        time.sleep(1)
        driver.quit()
