# Binary Search Algorithm

def BinarySearch(list, target):
    start = 0
    end = len(list)
    while start<=end:
        mid = int (start+(end-start)/2)
        if list[mid]>target :
            end = mid-1
        elif list[mid]<target :
            start = mid+1
        else :
            return mid


list = [1,2,3,4,5,6,7,8,9]
target = int (input("Enter target element: "))
mid = BinarySearch(list, target)
print("So element found at index:", mid," as the target value is:", target)


