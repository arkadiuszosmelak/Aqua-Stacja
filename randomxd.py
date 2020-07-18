import random

file = open("testfile.txt", "a") 
rok = 2020
miesiac = 1
dzien = 30
godzina = 0
minuta = 0
sekundy = 0
for i in range (864):
    y = random.uniform(0.0,40.0)
    file.write(str(y)+"\n")
    x = random.uniform(10.0, 40.0)
    file.write(str(x)+"\n")
    file.write("{0}-{1}-{2} {3}:{4}:{5}\n".format(2020,random.randint(1,12),random.randint(1,30),random.randint(0,23),random.randint(0,59),random.randint(0,59)))
file.close()