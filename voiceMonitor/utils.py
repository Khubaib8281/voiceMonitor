import os
import datetime

def timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)