import random
import math

with open("name.txt", "r") as f:
    data = f.read().split('\n')

random.shuffle(data)
random.shuffle(data)
random.shuffle(data)

#for i in data:
#    print(i)

x=len(data)

train = math.ceil(x/2)
val = x - train

print(train)
print(val)


train_data = data[:train]
val_data = data[val:]

with open("train.txt", "w") as a:
       for filename in train_data:
         a.write(str(filename+"\n")) 
         
         
with open("val.txt", "w") as a:
       for filename in val_data:
         a.write(str(filename+"\n")) 