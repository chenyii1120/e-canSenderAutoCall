#============================ 基本設定 ============================

# 建議參考README.md文件設定
BROWSER_DRIVER_PATH = "ChromeDriver/chromedriver.exe"

# 宅配通EDI客代
ID = "1234567890"

# 宅配通EDI密碼
PASSWORD = "abcd1234"





#============================ 計時器設定 ============================

# 是否啟用程序內的計時器
# (建議為 True，若設置為 False 時程式一開啟將直接啟動 bot，若需定時則需搭配系統內建排程功能)
USE_INNER_TIMER = True

# 排程執行時間 (24小時制，HH:MM冒號分隔，不足兩位數請補0)
TARGET_TIME = "16:05"

# 內建計時器檢查間隔 (分鐘)
# (建議至少設置 5 分鐘以上，設置為 0 仍將判斷為 1 分鐘，若真的要停用間隔請輸入 -1)
INNER_TIMER_CHECK_INTERVAL = 5





#============================ 不建議變更 ============================

# log檔內的時間格式，不建議變更
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# 崩潰報告檔名格式，不建議變更
CRASH_REPORT_NAME_FORMAT = "%Y%m%d_%H%M%S"





#============================ 待實現功能 ============================

# TODO: 是否跳過週末 (True/False)
SKIP_WEEKEND = True

# TODO: 是否需生成log檔(建議為True)
NEED_LOG = True

# TODO: 若派件失敗是否自動重試
AUTO_RETRY = True

# TODO: 自動重試次數
RETRY_TIMES = 0