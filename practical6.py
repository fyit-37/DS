#bubble sort
arr=[3,6,8,4,29]
n=len(arr)
for i in range(n):
    swappe = False
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swappe = True
        else:
            swappe = False 
            break



#insertion sort
n=[5,2,8,4,51]
for i in range(1,len(n)):
    val=n[i]
    j=i-1
    while j>=0 and val<n[j]:
        n[j+1]=n[j]
        j-=1
        n[j+1]=val


#selection sort
list_=[2,5,7,3,1,9]
for i in range(len(list_)):
    min_val=i
    for j in range(i+1,len(list_)):
        if list_[min_val]>list_[j]:
            min_val=j
    list_[i],list_[min_val]=list_[min_val],list_[i]
