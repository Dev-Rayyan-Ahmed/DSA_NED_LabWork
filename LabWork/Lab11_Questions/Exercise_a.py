def insertion_sort(A,N):
    A.insert(0,-1000)
    for k in range(2,N+1):
        temp = A[k]
        PTR = k-1

        while temp < A[PTR]:
            A[PTR+1] = A[PTR]
            PTR-=1
        A[PTR+1] = temp
    return A[1:]


def shell_sort(Num, N, key):
    k = int(N/2)
    while k>0:
        for i in range(k, N-1):
            key = Num[i]
            j = i
            while j >= k and Num[j-k] > key:
                Num[j],Num[j-k] = Num[j-k],Num[j]
            k = int(k/4)
    Num = insertion_sort(Num, len(Num))
    return Num

arr = [2,4,1,5,7,6,1]
# print(insertion_sort(arr,len(arr)))
print(shell_sort(arr, len(arr),None))
