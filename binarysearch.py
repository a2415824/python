def binary_search(arr,low,high,x):
    #Check base case
    if high>=low:
        mid = (high+low)//2
        #if element is present at middle itself

        if arr[mid]==x:
            return mid

            #if element is smaller than mid the element is only presrnt in left of the array
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)    
         #else element is only present in right of the array
        else:
             return binary_search(arr,mid+1,high,x) 
    else:
        return -1

arr=[2,6,5,8,3,9]
x=2
result=binary_search(arr,0,len(arr)-1,x)
if result!=-1:
    print("Element is present at index",str(result +1))
else:
    print("Element is not present in arry")        