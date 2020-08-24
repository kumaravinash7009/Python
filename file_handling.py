f=open('IMG_2305.JPG','rb')

f2=open('Avinash.JPG','wb')

for i in f:
	f2.write(i)
	
for i in f:
	print(f.read())
