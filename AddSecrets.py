f = open ("secrets.py", -w)
f.write("TOKEN = " ${{secrets.TOKEN}})
f.close()
