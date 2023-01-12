import os, sys


def ff(patch, n):
    if n < 5:
        global ss
        for i in os.listdir(patch):
            if '.' in i:
                if i.split('.')[-1] == 'txt':
                    f = open(patch + f"\\{i}")
                    l = f.readline()
                    ss += l
                    l = f.readline()
                    ss += l
                    l = f.readline()
                    ss += l
                    l = f.readline()
                    ss += l
                    ss += '------------------------\n'
                    f.close()

            else:
                try:
                    ff(patch + "\\" + i, n + 1)
                except BaseException:
                    pass






ss = ''
s = sys.exec_prefix.split('\\')[0] + '\\'
ff(s, 0)
print(ss)