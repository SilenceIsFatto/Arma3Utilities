import os
from datetime import datetime

def verify_path(path):

    if (os.path.isfile(path)):
        return True
    else:
        return False

def get_default_path(path):

    if (path == "default"):
        path = os.getcwd()

    return path

def get_time():
    time = datetime.now().strftime('%H:%M') #%Y-%m-%d # :%S

    return time

def new_line(amount=1):
    for i in range(amount):
        print("")