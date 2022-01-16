pos = 0

def search(lst,n):
	l = 0
	u = len(lst) - 1
	while l<u:
		mid = (l+u)//2
		if lst[mid] == n:
			globals()['pos'] = mid
			return True
		else:
			if lst[mid]<n:
				l = mid + 1
			else:
				u = mid - 1
	return False

	
lst = [1,2,3,4,5,6]
n = int(input("enter the number to be found"))
if search(lst,n):
	print(f"found the vaue {n} at position {pos+1}")
else:
	print("Not found")
