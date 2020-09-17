# linearly search
arr = [ 2, 3, 4, 5, 6, 10, 51 ]; 
x =int(input("enter linear search number:"))
lenth_arr= len(arr);
def search(arr, lenth_arr, x): 
  
    for i in range (0, lenth_arr): 
        if (arr[i] == x): 
            return i; 
    return -1; 
result = search(arr, lenth_arr, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result);



#binary search
arr = [ 21, 31, 41, 51, 61] 
x =int(input("enter binary search number:"))
def binarySearch (arr, l, r, x): 
    if r >= l:
        mid = l + (r - l) // 2 
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x)
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        return -1
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result == -1: 
    print ("Element is not present in array") 
else: 
    print ("Element is present at index", result) 
