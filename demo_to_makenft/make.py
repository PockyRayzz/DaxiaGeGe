all_b = b""
with open("images.jpg","rb") as f:
    all_b += f.read()


with open("exp.py","rb") as f:
    all_b += f.read()


with open("new_images.jpg","wb") as f:
    f.write(all_b)


print("""
upload new_images,
embed password to unlockable content,
sell it!
""")