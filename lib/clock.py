import config
import datetime
import time


def check_time():
    # 判斷是否使用內建計時器
    if not config.USE_INNER_TIMER:
        return True
    else:
        # 若跳過周末功能開啟
        if config.SKIP_WEEKEND:
            # 判定是否為周末
            today = datetime.datetime.now()
            today_inform = today.strftime("%a")
            if today_inform == "Sat" or today_inform == "Sun":
                print(f"今日為 {today_inform}，因此跳過不派車，若您需要假日派車服務，請將 config.py 中的 SKIP_WEEKEND 變更為 False")
                return False

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
