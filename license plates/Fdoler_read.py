import os
for root, dirs, files in os.walk("C:\Computing\Josh\CS-Coursework\Coursework\license plates"):
    for name in files:
        if name.endswith((".jpeg", ".jpg")):
            htmlfiles = [os.path.join(root, name)
                for root, dirs, files in os.walk("C:\Computing\Josh\CS-Coursework\Coursework\license plates")
                for name in files
                if name.endswith((".jpeg", ".jpg"))]
print(htmlfiles)