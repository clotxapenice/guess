import random
start = input('請決定隨機數字開始值:')
start = int(start)
end = input('請決定隨機數字結束值:')
end = int(end)
r = random.randint( start , end )
count = 0
while True:
    count += 1
    num = input('請輸入一個數字:')
    num = int(num)
    if num == r:
        print('恭喜你猜對了! 總共猜了' , count,'次')
        break
    elif num > r:
        print('再低一點')
    elif num < r:
        print('再高一點')
    print('這是你猜的第' , count , '次')
        
