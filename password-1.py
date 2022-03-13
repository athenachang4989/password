password = 'a123456'
chance = 3
while chance > 0:
    chance = chance - 1
    pin = input('請輸入密碼：')
    if pin == password:
        print('登入成功！')
        break
    else:
        print('密碼錯誤！')
        if chance > 0:
            print('還有', chance, '次機會')
        else:
            print('您的帳號已鎖定！')
