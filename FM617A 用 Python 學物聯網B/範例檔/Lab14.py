# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin
import dht, BlynkLib, network              # 匯入 Blynk 模組

sta_if = network.WLAN(network.STA_IF)      # 取得無線網路介面
sta_if.active(True)                        # 取用無線網路
sta_if.connect('無線網路名稱', '密碼')      # 連結無線網路
while not sta_if.isconnected():            # 等待連上無線網路
    pass               
print("Wifi已連上")                         # 顯示連上網路的訊息

token = '這裡要填入剛剛收到的權杖'           # Blynk 寄給你的權杖
blynk = BlynkLib.Blynk(token)              # 取得 Blynk 物件

sensor = dht.DHT11(Pin(0))                 # 使用 D3 腳位取得溫溼度物件
relay = Pin(14, Pin.OUT, value = 0)        # 使用 D5 腳位控制繼電器

def v1_handler():              # 提供溫度到 V1 虛擬腳位的函式
    sensor.measure()
    blynk.virtual_write(1, sensor.temperature())

def v2_handler():              # 提供濕度到 V2 虛擬腳位的函式
    # 使用剛剛讀取的感測值, 避免讀取時間間隔太近
    blynk.virtual_write(2, sensor.humidity())

def v3_handler(value):         # 從 V3 虛擬腳位讀取手機按鈕狀態的函式
    relay.value(int(value[0]))

blynk.on("readV1", v1_handler) # 註冊由 v1_handler 處理 V1 虛擬腳位
blynk.on("readV2", v2_handler) # 註冊由 v2_handler 處理 V2 虛擬腳位
blynk.on("V3", v3_handler)     # 註冊由 v3_handler 處理 V3 虛擬腳位

while True:
    blynk.run()                # 持續檢查是否有收到 Blynk 送來的指令
    
    