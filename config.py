# 建議參考README.md文件設定
BROWSER_DRIVER_PATH = "/Users/josephc./Desktop/Codes/Python/ChromeDriver/chromedriver"

# 宅配通EDI客代
ID = "4669080101"

# 宅配通EDI密碼
PASSWORD = "ab271020"

# 排程執行時間 (24小時制，HH:MM冒號分隔，不足兩位數請補0)
TIME = "16:05"

# log檔內的時間格式，不建議變更
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# 崩潰報告檔名格式，不建議變更
CRASH_REPORT_NAME_FORMAT = "%Y%m%d_%H%M%S"

# TODO: 是否跳過週末 (True/False)
SKIP_WEEKEND = True

# TODO: 是否需生成log檔(建議為True)
NEED_LOG = True

# TODO: 是否啟用程序內的計時器
#   (建議為 True，若設置為 False 時程式一開啟將直接啟動 bot，若需定時則需搭配系統內建排程功能)
INNER_TIMER = True

# TODO: 若派件失敗是否自動重試
AUTO_RETRY = True

# TODO: 自動重試次數
RETRY_TIMES = 0