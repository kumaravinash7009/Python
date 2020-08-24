f=open('Mydata','r')			#to read
print(f.read())
print(f.readline())

f1=open('abc','w')			#to write
f1.write('something')

f2=open('xyz','a')			#to append
f2.write('Mobile')
