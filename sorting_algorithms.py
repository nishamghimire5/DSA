Array = [5,6,73,67,123,3,9,1,2,5]
Array2 =[34,23,5,2,5,7,1,9,5,2,783,535,22]
Array3= [2,14,21,6,12,1,5,8,32,15]

#heap sort
def heapify(a,n,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and a[largest] < a[left]:
        largest = left
        
    if right < n and a[right] > a[largest]:
        largest = right
    
    if i != largest:
        a[i],a[largest] = a[largest],a[i]
        heapify(a,n,largest)

def heapSort(a):
    n = len(a)
    
    for i in range(n//2 -1, -1, -1):
        heapify(a,n,i)
    
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i],a[0]
        heapify(a,i,0)
    return a

print(f" heapSort: {heapSort(Array3)}")

#quick sort
def partition(arr,low,high):
    pivot = arr[high] #pivot = last element
    i = low - 1 # i is initialized element before that first element
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j] #putting lower than than pivot at first partition
    arr[high],arr[i+1] = arr[i+1],arr[high] #putting pivot in correct place 
    return i+1 #pivot element index
    
def quickSort(arr,low,high):
    if low < high:
        pivotIndex = partition(arr,low,high) #gets pivot index
        quickSort(arr,low,pivotIndex-1) #first half
        quickSort(arr,pivotIndex+1,high) #second half
        return arr


print(f" quickSort: {quickSort(Array2,0,len(Array2)-1)}")
  
#merge sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i=j=k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
                
        return arr
    return arr
    
print(f" MergeSort: {mergeSort(Array)}")

#insertion sort
def insertionSort(a):
    for i in range(len(a)):
        key = a[i]
        j = i - 1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a
        
print(f" InsectionSort: {insertionSort(Array)}")

#bubble sort
def bubbleSort(b):
    for i in range(len(b)):
        swapped = False
        for j in range(len(b)-1-i):
            if b[j] > b[j+1]:
                temp = b[j]
                b[j] = b[j+1]
                b[j+1] = temp
                swapped = True
        if not swapped:
            return b
    return b
    
print(f" bubbleSort: {bubbleSort(Array)}")    

#selection sort
def SelectionSort(c):
    n = len(c)
    for i in range(n):
        smallest = i
        for j in range(i+1,n):
            if c[j] < c[smallest]:
                smallest = j
        c[i],c[smallest] = c[smallest],c[i] #swapping smallest with the original index
    return c
    
print(f" SelectionSort: {SelectionSort(Array)}")    
     
