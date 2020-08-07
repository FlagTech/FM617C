# 因為 Thonny 開發環境近期版本更新, 所以操作步驟已經和手冊上不同了
# 為了避免學習時遇到操作上的問題, 請從下面網址下載和手冊上一樣的版本：
# https://github.com/thonny/thonny/releases/tag/v3.1.2

from machine import ADC
import time

# 建立 A0 腳位的 ADC 物件, 並命名為 adc
adc = ADC(0)

while True:
    # 用 read() 方法從 A0 號腳位讀取 ADC 轉換後的數值
    # 然後將讀到的值用 print() 輸出
    print(adc.read())
    
    # 暫停 0.05 秒
    time.sleep(0.05)
