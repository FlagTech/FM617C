# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

import network
import ESP8266WebServer                 # 匯入網站模組
from machine import Pin

def handleCmd(socket, args):            # 處理 /cmd 指令的函式
    if 'relay' in args:                 # 檢查是否有 relay 參數
        if args['relay'] == 'on':       # 若 relay 參數值為 'on'
            relay.value(1)              # 讓繼電器通電
        elif args['relay'] == 'off':    # 若 relay 參數值為 'off'
            relay.value(0)              # 讓繼電器斷電
        ESP8266WebServer.ok(socket, "200", "OK")   # 回應 OK 給瀏覽器
    else:
        ESP8266WebServer.err(socket, "400", "ERR") # 回應 ERR 給瀏覽器

print("啟動中...")
sta_if = network.WLAN(network.STA_IF)     # 取得無線網路介面
sta_if.active(True)                       # 啟用無線網路
sta_if.connect('無線網路名稱', '密碼')      # 連結無線網路
relay = Pin(14, Pin.OUT, value=0)         # 控制 D5 腳位
while not sta_if.isconnected():           # 等待無線網路連上
    pass

ESP8266WebServer.begin(80)                  # 啟用網站
ESP8266WebServer.onPath("/cmd",handleCmd)   # 指定處理指令的函式
ESP8266WebServer.setDocPath("/relay")       # 指定 HTML 檔路徑
print("伺服器位址：" + sta_if.ifconfig()[0]) # 顯示網站的 IP 位址

while True:
    ESP8266WebServer.handleClient()       # 持續檢查是否收到新指令





