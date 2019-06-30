#!/bin/bash

import paramiko

host='172.20.0.10'
user='san'
passwd='s'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_system_host_keys()
client.connect(host,port=22,username=user,password=passwd,look_for_keys=False)
stdin, stdout, stderr = client.exec_command('ls')
print("\noutput from remote server:\n")
for line in stdout.readlines():
    print line
    client.close()


