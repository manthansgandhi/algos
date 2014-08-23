# Given a list and a target number as input, search the target number and
# return the index of the target if found else return None
# Use binary search and also implement it in a recursive manner
# For recursive you can pass in the start and the end of the list
# Eg: input = ([2,5,8,11,14,17,18,20],18) should return 6
# ([2,5,8,11,14,17,18,20],19) should return None
# Runtime: O(log n)

def binSearch(li,target):
    start = 0
    end = len(li) - 1
    while start <= end:
        mid = (start + end)/2
        if li[mid]==target:
            return mid
        elif target < li[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

print binSearch([2,5,8,11,14,17,18,20],18)
print binSearch([2,5,8,11,14,17,18,20],19)
print binSearch([2,5,8,11,14,17,18,20],6)
print binSearch([2,5,8,11,14,17,18,20],5)
print binSearch([2,5,8,11,14,17,18,20],2)
print binSearch([2,5,8,11,14,17,18,20],20)
print binSearch([2],10)
print binSearch([2],2)

def binSearchRec(li,target,start,end):
    mid = (start + end)/2
    if start > end:
        return None
    if li[mid]==target:
        return mid
    elif target < li[mid]:
        end = mid - 1
        return binSearchRec(li,target,start,end)
    else:
        start = mid + 1
        return binSearchRec(li,target,start,end)

print binSearchRec([2,5,8,11,14,17,18,20],18,0,7)
print binSearchRec([2,5,8,11,14,17,18,20],19,0,7)
print binSearchRec([2,5,8,11,14,17,18,20],6,0,7)
print binSearchRec([2,5,8,11,14,17,18,20],5,0,7)
print binSearchRec([2,5,8,11,14,17,18,20],2,0,7)
print binSearchRec([2,5,8,11,14,17,18,20],20,0,7)
print binSearchRec([2],20,0,0)
print binSearchRec([2],2,0,0)

