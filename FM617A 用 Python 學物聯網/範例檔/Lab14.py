# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

# 這是搭配新的 Blynk IoT 版本的範例檔, 與舊版的 Blynk Legacy 不相容
# 如果您仍在使用 Blynk Legacy 版本, 請至以下網址下載對應版本的範例檔：
# https://github.com/FlagTech/FM617C/releases/tag/FM617D

from machine import Pin
import dht, BlynkLib, network              # 匯入 Blynk 模組
from BlynkTimer import BlynkTimer

sta_if = network.WLAN(network.STA_IF)      # 取得無線網路介面
sta_if.active(True)                        # 取用無線網路
sta_if.connect('無線網路名稱', '無線網路密碼') # 連結無線網路
while not sta_if.isconnected():            # 等待連上無線網路
    pass               
print("Wifi已連上")                         # 顯示連上網路的訊息

token = 'Blynk 裝置的認證權杖'               # 裝置的認證權杖
blynk = BlynkLib.Blynk(token)              # 取得 Blynk 物件

sensor = dht.DHT11(Pin(0))                 # 使用 D3 腳位取得溫溼度物件
relay = Pin(14, Pin.OUT, value = 0)        # 使用 D5 腳位控制繼電器

def v3_handler(value):           # 從 V3 虛擬腳位讀取手機按鈕狀態的函式
    relay.value(int(value[0]))

def temp_huni_handler():         # 提供溫/濕度到 V1/V2 虛擬腳位的函式
    sensor.measure()
    blynk.virtual_write(1, sensor.temperature())
    blynk.virtual_write(2, sensor.humidity())

timer = BlynkTimer()                       # 建立計時器管理物件
timer.set_interval(3, temp_huni_handler)   # 建立週期性計時器, 定時傳送溫濕度

blynk.on("V3", v3_handler)     # 註冊由 v3_handler 處理 V3 虛擬腳位

while True:
    blynk.run()                # 持續檢查是否有收到 Blynk 送來的指令
    timer.run()                # 持續檢查是否觸發計時器
