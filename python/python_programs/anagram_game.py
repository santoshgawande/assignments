path = '/usr/share/dict/cracklib-small'
with open(path) as f:
    content =f.read().split('\n')
    
    for i in range(len(f)):
       if len(content[i]) <=5:
          print content