from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config
import datetime
import traceback

run_time = config.TIME.split(":")
message = str

while True:

    now = datetime.datetime.now()
    now_inform = now.strftime(config.TIME_FORMAT)

    if now.hour == int(run_time[0]) and now.minute == int(run_time[1]):

        try:

            now_inform = now.strftime(config.TIME_FORMAT)
            report_time_inform = now.strftime(config.CRASH_REPORT_NAME_FORMAT)
            driver = webdriver.Chrome(config.BROWSER_DRIVER_PATH)

            driver.get("http://query3.e-can.com.tw/wedi2012/wedilogin.asp")

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
            message = "Fail"
            print(traceback.format_exc())
            report_path = f"CrashReport/{report_time_inform}.txt"
            with open(report_path, mode="w") as crash_report:
                crash_report.write(traceback.format_exc())
            print(f"The Crash Report has saved in path: {report_path}")
            raise Exception("")
        else:
            message = "Success"
        finally:
            print(f"Status: {message}")
            with open("log.txt", mode="a") as file:
                file.write(f"{now_inform}\t{message}\n")
            time.sleep(1)
            driver.quit()

            break


    else:
        print(f"現在時間：{now_inform}，排程預計於每日 {run_time[0]}:{run_time[1]} 執行，每分鐘檢查一次")
        time.sleep(60)