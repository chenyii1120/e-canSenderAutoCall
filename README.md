# e-canSenderAutoCall

## 大嘴鳥 / 宅配通 自動派收

Automatically do the E-can Sender call for you.

## 關於

本專案可以協助你每天完成 大嘴鳥 / 宅配通 的通知收件，  
但你必須符合以下條件：

<ul>
    <li>必須要是 大嘴鳥 / 宅配通 的契約客戶</li>
    <li>必須要 申請/使用 過大嘴鳥的 WebEDI 服務</li>
    <li>電腦已安裝 Google Chrome 瀏覽器</li>
</ul>

## 如何開始

### 1. 檢查 Google Chrome 版本
進入 Google Chrome 後點選右上角三個點點，選擇「設定」  
進入設定畫面後點選左側「關於 Chrome」查看版本號碼
### 2. 下載 Chrome Driver
進入以下連結，選擇對應的版本下載即可  
https://chromedriver.chromium.org/
### 3. 將 Chrome Driver 丟進 /ChromeDriver 資料夾
### 4. 設定 config.py 檔案
### 5. 編寫 bat / sh 檔案
 * for Windows
 ```console
 python3 main.py
 pause
 ```
   儲存成 start.bat 後即可雙擊啟動
 * for Mac / Linux
 ```console
 python3 main.py
 ```
   儲存成 start.sh 後即可雙擊啟動
   Mac 系統可參考 [這篇](https://www.minwt.com/mac/22625.html) 教學來讓系統可雙擊開啟 sh
