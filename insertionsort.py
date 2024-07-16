#Insertion sort
def insertionSort2(n, arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
                arr[j+1]=arr[j]
                j-=1
        arr[j+1]=key
        for k in range(len(arr)):
            print(arr[k],end=' ')
        print()

n=6
arr=[23,10,2,1,5]
insertionSort(n,arr)
