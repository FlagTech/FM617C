# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin
import time
import dht

sensor = dht.DHT11(Pin(0))         # 使用 D3 腳位取得溫溼度物件
while True:
    sensor.measure()
    temp_humi = "%2d℃/%2d%%" % (
        sensor.temperature(),
        sensor.humidity())
    print(temp_humi)
    time.sleep(3)

