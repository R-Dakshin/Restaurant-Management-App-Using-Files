import pickle

f=open(r'C:\Users\daksh\OneDrive\Desktop\APP\Restaurant Management App\BILLS.bin','rb')
l=pickle.load(f)
#for i in l:
#   print(i)
print(l[len(l)-1])
f.close()


