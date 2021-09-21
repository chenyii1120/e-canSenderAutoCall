import config
import datetime
import time


def check_time():
    run_time = config.TIME.split(":")

    while True:
        now = datetime.datetime.now()
        now_inform = now.strftime(config.TIME_FORMAT)

        if now.hour == int(run_time[0]) and now.minute >= int(run_time[1]):
            return True
            break

        else:
            print(f"現在時間：{now_inform}，排程預計於每日 {run_time[0]}:{run_time[1]} 執行，每 5 分鐘檢查一次")
            time.sleep(300)

def get_now():
    return datetime.datetime.now()