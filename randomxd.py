import random
import datetime

file = open("testfile.txt", "a") 
for i in range (5, 289*5, 5):
    y = random.uniform(0.0,40.0)
    file.write(str(y)+"\n")
    x = random.uniform(10.0, 40.0)
    file.write(str(x)+"\n")
    data = datetime.datetime.now() - datetime.timedelta(minutes=i)
    data = str(data)[:-7]
    file.write(data+"\n")
file.close()