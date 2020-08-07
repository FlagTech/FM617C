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

username = "簡訊服務帳號"
passwd = "簡訊服務密碼"
phone = "接收簡訊的手機號碼"
message = "有人打開保險箱在翻找東西,趕快去抓小偷!" #請勿輸入空格

# 建立 16 號腳位的 Pin 物件, 設定為輸入腳位, 並命名為 shock
shock = Pin(16, Pin.IN)

while True:
    if shock.value() == 1:
        print("感應到振動!")
        
        # 連線簡訊服務發送簡訊通知
        urequests.get(
            "http://api.message.net.tw/send.php?mtype=G&id="
            + username + "&encoding=utf8&password=" + passwd
            + "&tel=" + phone + "&msg=" + message)
        
        # 暫停 60 秒, 避免短時間內一直收到重複的警報
        time.sleep(60)