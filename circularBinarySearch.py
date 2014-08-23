# Given a list of integers as a list such that this list is in a circular sorted order meaning if you rotate it,
# you will get to a point where it is in sorted order, use binary search to search for a target
# Eg: cirBinSearch([5,6,7,8,9,1,2,3],9) should return the index 4
# runtime O(log n)


def cirBinSearch(li,target):
    start = 0
    end = len(li) - 1
    while start <= end:
        mid = (start + end)/2
        if li[mid]==target:
            return mid

        elif li[start]<li[mid]:
            print 'First Half Sorted'
            # This means that first half is sorted
            if target>=li[start] and target<li[mid]:
                # This means that target can only be in the first half
                return binSearchRec(li,target,start,mid-1)
            else:
                print 'Check unsorted second half'
                # Need to check the unsorted second half and repeat
                start = mid + 1
        else:
            print 'Second Half Sorted'
            # THis means that second half is sorted
            if target>li[mid] and target<=li[end]:
                # This means that targed can onlt be in the second half
                return binSearchRec(li,target,mid+1,end)
            else:
                print 'Check unsorted first half'
                # Need to check the first unsorted half and repeat
                end = mid - 1
        
    return None

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

print cirBinSearch([5,6,7,8,9,1,2,3],9)
print cirBinSearch([5,6,7,8,9,1,2,3],10)
print cirBinSearch([5],9)
print cirBinSearch([5],5)
print cirBinSearch([],9)
