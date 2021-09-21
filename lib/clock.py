import config
import datetime
import time


def check_time():
    # 判斷是否使用內建計時器
    if not config.USE_INNER_TIMER:
        return True
    else:

        run_time = config.TARGET_TIME.split(":")
        interval = int(config.INNER_TIMER_CHECK_INTERVAL)

        # 若config內間隔設定為-1則停用間隔
        if interval == -1:
            interval = 0
        elif interval == 0:
            interval = 1

        # 判斷時間迴圈
        while True:
            now = datetime.datetime.now()
            now_inform = now.strftime(config.TIME_FORMAT)

            if now.hour == int(run_time[0]) and now.minute >= int(run_time[1]):
                return True

            else:
                print(f"現在時間：{now_inform}，排程預計於每日 {run_time[0]}:{run_time[1]} 執行，每 {interval} 分鐘檢查一次")

                time.sleep(60 * interval)


def get_now():
    return datetime.datetime.now()
