def MinCoin(n):
	nocoin = 0
	tens=n//10
	nocoin+=tens
	moneyleft=(n-10*tens)
	fives=moneyleft//5
	nocoin+=fives
	nocoin+=moneyleft-fives*5
	return nocoin

n=int(input())
print(MinCoin(n))	