# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import Pin, PWM
import time, network, urequests

# 連線 Wifi 網路 
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wi-Fi 基地台", "Wi-Fi 密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

rLED = PWM(Pin(12))  # 控制紅燈
gLED = PWM(Pin(13))  # 控制綠燈
bLED = PWM(Pin(15))  # 控制藍燈

while True:
    # 取得 AQI 空污指數
    res = urequests.get("AQI 網址")
    j = res.json()  # 載入並解析 JSON 格式資料
    print("測站名稱：", j['data']['city']['name'])
    print("發布時間：", j['data']['time']['s'])
    print("AQI：", j['data']['aqi'])
    print("PM2.5：", j['data']['iaqi']['pm25']['v'])

    AQI = j['data']['aqi']  # 將 AQI 空污指數轉為整數, 以便比較大小

    if AQI <= 50:
        gLED.duty(1023); rLED.duty(0)    # 空氣品質良好顯示綠燈
    elif 51 < AQI <= 100:
        gLED.duty(300); rLED.duty(1023)  # 空氣品質普通顯示黃燈
    else:
        gLED.duty(0); rLED.duty(1023)    # 空氣品質不佳顯示紅燈
    
    time.sleep(1800)  # 每半小時更新一次燈號