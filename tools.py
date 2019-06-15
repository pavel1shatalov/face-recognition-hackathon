import os
import base64


def write_photo(person_num, photo_num, txt):
    if not os.path.exists("train_dir"):
        os.makedirs("train_dir")

    if not os.path.exists(os.path.join("train_dir", f"person{person_num}")):
        os.makedirs(os.path.join("train_dir", f"person{person_num}"))
    
    with open(os.path.join("train_dir", f"person{person_num}", f"photo{photo_num}.jpg"), "w") as f:
        f.write(base64.decodestring(txt))