import os
import base64
import requests

# initializing global
data = {}


def write_photo(name, txt, photo_num=1):
    txt = txt[23:]
    print(txt)
    if not name:
        return

    if not os.path.exists("train_dir"):
        os.makedirs("train_dir")

    if not os.path.exists(os.path.join("train_dir", name)):
        os.makedirs(os.path.join("train_dir", name))

    with open(os.path.join("train_dir", name, f"{name}{photo_num}.jpg"), "wb") as f:
        f.write(base64.b64decode(txt))

    data[name] = False
    requests.post('http://localhost:5000/admin', json=data)
