import Shares as sh
import time , importlib
# Main Program
def dispshare(d):
    print("---------------------------")
    print("ShareName\t\t ShareVal ")
    for sn,sv in d.items():
        print("\t{}\t\t{}".format(sn,sv))
    # for sn in d:
    # print("\t{}\t\t{}".format(sn,d[sn]))

d=sh.shareinfo() #Function call
dispshare(d)
print("I am going to Sleep for 10 sec")
time.sleep(10)
print("I am commig out of sleep")
# Reloading the previously imported modules we reload() --imp
importlib.reload(sh)
d=sh.shareinfo() #Function call
dispshare(d)