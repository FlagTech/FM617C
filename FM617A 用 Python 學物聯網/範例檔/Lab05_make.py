# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin
import time, network, urequests

# 連線 Wifi 網路 
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

# 建立 16 號腳位的 Pin 物件, 設定為輸入腳位, 並命名為 shock
shock = Pin(16, Pin.IN)

make_url = '你的 make.com web hook 網址'
replit_url = '你的 replit 專案網站網址'

while True:
    if shock.value() == 1:
        print("感應到振動!")
        
        # 連線 MAKE 服務發送簡訊通知
        urequests.get(replit_url
                      + '?url=' + make_url)  
        
        # 暫停 60 秒, 避免短時間內一直收到重複的警報
        time.sleep(60)

