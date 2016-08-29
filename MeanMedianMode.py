#Day 0: Mean, Median, and Mode
#I could have used modules like numpy or scipy, but I believe the point was dealing with the algorithm for each measure.

def setMean(arr):
	soma = 0
	for i in arr:
		soma+=int(i)

	mean = round(soma/N, 1)
	return mean


def setMedian(arr):
	arr.sort()
	size=len(arr)
	if size%2==0:
		firstIndex = int(size/2)
		firstItem = int(arr[firstIndex])

		secondIndex = int(size/2 - 1)
		secondItem = int(arr[secondIndex])

		median = round((firstItem + secondItem)/2, 1)

	else:
		index = int(size/2)
		median = round(float(arr[index]),1)

	return median


def setMode(arr):
	counter = {}

	for i in arr:
		counter.setdefault(i, 0)
		counter[i]+=1

	greater = 0
	for v in counter.values():
		if v > greater:
			greater = v

	equalOccurrence = []
	for k, v in counter.items():
		if v == greater:
			equalOccurrence.append(int(k))

	equalOccurrence.sort()
	return equalOccurrence[0]

N = int(input())
arr = [int(x) for x in input().split(' ')]

print(setMean(arr))
print(setMedian(arr))
print(setMode(arr))