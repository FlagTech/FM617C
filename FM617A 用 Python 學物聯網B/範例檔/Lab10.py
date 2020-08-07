# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import ADC
import time, network, urequests

# 連線 Wifi 網路 
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

aio_username = "您的 Adafruit IO 帳號"
aio_key = "您的 Adafruit IO 金鑰"
aio_feed = "您的 Adafruit IO feed 名稱"

# 建立 A0 腳位的 ADC 物件, 並命名為 adc
adc = ADC(0)

while True:
    # 讀取雨水感測器經過 ADC 轉換後的數值
    value = adc.read()
    
    if value < 700: # 依照 Lab09 的測試, 低於 700 表示有下雨
        # 雨水越多, ADC 值越低, 所以用最大值 1024 減 ADC 值,
        # 以便將資料反轉為雨水越多, 數值越高
        data = {"value": 1024-value}
    else:
        # 沒下雨的話就送出 0
        data = {"value": 0}
        
    # 設定 Adafruit IO 上傳資料的 API 網址
    url = ("https://io.adafruit.com/api/v2/" + aio_username +
           "/feeds/" + aio_feed + "/data?X-AIO-Key=" + aio_key)
    
    # 用 POST 上傳 JSON 資料
    urequests.post(url, json=data)

    # 暫停 2 秒, 避免送出太多資料超過 Adafruit IO 免費額度
    time.sleep(2)