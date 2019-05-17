def feibo(n):
	if (n==0):
		return 0
	if (n==1):
		return 1
	if (n<0):
		return False
	if(n>1):
		a=[-1]*(n+1)
		a[0]=0
		a[1]=1
		for i in range(2,n+1):
			a[i]=a[i-1]+a[i-2]
	return a[n]
