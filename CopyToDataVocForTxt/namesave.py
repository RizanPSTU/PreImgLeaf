import os

with open("name.txt", "w") as a:
    for path, subdirs, files in os.walk(r'JPEGImages'):
       for filename in files:
         f = os.path.join(path, filename)
         #print(filename)
         filename = filename.replace(".jpg", "\n") 
         print(filename)
         a.write(str(filename)) 