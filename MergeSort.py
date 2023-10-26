# Merge Sort in Analysis of Algorithms Python

def mergeSort(arr):
    if len(arr) > 1:
        mid  = len(arr)//2
        left = arr[:mid]
        Right = arr[mid:]
        mergeSort(left)
        mergeSort(Right)
        i = j = k = 0
        
        while i < len(left) and j < len(Right):
            if left[i] < Right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
            
            while i < len(left):
                arr[k] =  left[i]
                i += 1
                k +=1
            while j < len(Right):
                arr[k] = Right[j]
                j += 1
                k += 1
                
                
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()
    
if __name__ == '__main__':
    
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is: ")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ")
    printList(arr)
    
    