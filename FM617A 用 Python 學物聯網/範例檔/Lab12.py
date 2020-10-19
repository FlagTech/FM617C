# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin
import time
import network
from umqtt.robust import MQTTClient
import dht

sensor = dht.DHT11(Pin(0))                 # 使用 D3 腳位取得溫溼度物件

client = MQTTClient(
    client_id="weather", 
    server="io.adafruit.com", 
    user="帳戶名稱", 
    password="填入你的金鑰",
    ssl=False)

sta_if = network.WLAN(network.STA_IF)     # 取得無線網路介面
sta_if.active(True)                       # 啟用無線網路
sta_if.connect('無線網路名稱', '密碼')     # 連結無線網路
while not sta_if.isconnected():           # 等待無線網路連上
    pass

print("connected")

client.connect()
while True:
    sensor.measure()
    temp_humi = "%2d℃/%2d%%" % (
        sensor.temperature(),
        sensor.humidity())
    client.publish(
        b"帳戶名稱/feeds/temp_humi",
        temp_humi.encode())
    print(temp_humi)
    time.sleep(3)
