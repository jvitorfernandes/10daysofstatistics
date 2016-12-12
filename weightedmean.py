N = int(input()) #Number of elements on the following arrays
X = [float(x) for x in input().split(' ')] #elements
W = [float(x) for x in input().split(' ')] #elements' weights

soma = 0
soma_pesos = 0
i=0
while i < N:
	soma += X[i]*W[i]
	soma_pesos += W[i]
	i+=1

weighted_mean = round((soma/soma_pesos), 1)
print(weighted_mean)
