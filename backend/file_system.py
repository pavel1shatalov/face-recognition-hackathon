import os
import base64


def write_photo(name, txt, photo_num=1):
    txt = txt[23:]
    print(txt)
    if not name:
        return

    if not os.path.exists("train_dir"):
        os.makedirs("train_dir")

    if not os.path.exists(os.path.join("train_dir", name)):
        os.makedirs(os.path.join("train_dir", name))

    with open(os.path.join("train_dir", name, f"photo{photo_num}.jpg"), "wb") as f:
        f.write(base64.b64decode(txt))
