import time
while True:
    time.sleep(1)
    name = input('名前を入力してください。')
    if(name == 'finish'):
        print('OK')
        break 
    elif (name):
        print('Hello,' + name + '!')
    else:
        print('?')
