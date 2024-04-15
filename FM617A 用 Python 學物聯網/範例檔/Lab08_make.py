# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin
import mfrc522, network, urequests, time

# 連線 Wifi 網路 
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

rfid = mfrc522.MFRC522(0, 2, 4, 5, 14)
led = Pin(15, Pin.OUT)

make_url = "MAKE 請求網址"
replit_url = '你的 replit 專案網站網址'

while True:

    led.value(0)  # 搜尋卡片之前先關閉 LED
    stat, tag_type = rfid.request(rfid.REQIDL)  # 搜尋 RFID 卡片
    
    if stat == rfid.OK:  # 找到卡片
        stat, raw_uid = rfid.anticoll()  # 讀取 RFID 卡號
        if stat == rfid.OK:
            led.value(1)  # 讀到卡號後點亮 LED
            
            id = "%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1],
                                       raw_uid[2], raw_uid[3])
            print("偵測到卡號：", id)
            
            # 連線 MAKE 服務以便將卡號傳送到 Google 試算表
            urequests.get(replit_url
                             + '?url=' + make_url
                             +'&value=' + id)
            
            time.sleep(0.5)  # 暫停一下, 避免 LED 太快熄滅看不到
