import os

file_list = os.listdir("d:\Desktop\david_copperfield_th_librivox")
print(len(file_list))
os.chdir("d:\Desktop\david_copperfield_th_librivox")
with open("d:\\Desktop\\name.txt",'r') as f:
    name = f.read()
    name1 = name.split("\n")
    print(type(name1))
    print(len(name1))

m=0
for i in  file_list:
    os.rename(i,name1[m]+".mp3")
    m += 1


