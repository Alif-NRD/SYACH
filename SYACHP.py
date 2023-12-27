import os, sys
os.system("git pull")
try:
    __import__("SYACH").SYACH()
except Exception as e:
    exit(str(e))
