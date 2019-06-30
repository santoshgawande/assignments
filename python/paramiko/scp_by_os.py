import os,sys,getpass
if getpass.getuser()!="root":
    print "Needs root privileges"
    sys.exit()

os.system("scp san.txt san@172.20.0.10:/home/san")
