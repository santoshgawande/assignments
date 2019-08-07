**For Installation of mod_python**
*1. first install this packages which required for mod_python.*
```bash
apt-get install apache2
apt-get install libapache2-mod-python
```

*2. put apache2.conf and httpd.conf file in apache2 directory.*
```bash
 sudo mv apache2.conf httpd.conf /etc/apache2/
 ```

*3. for checking mod_python working or not run hello.py. first put in /var/www/html*
```bash
python hello.py
```
