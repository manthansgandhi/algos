# Given an input of list(or arrays) find the sub List such that this sub List
# has the maximum sum. Also return the sum
# eg: input = [4,5,-1,-6,-4,-3,2,3,4,5,-7,-9,10] should return 14 and [2,3,4,5]
# This is O(n) algorithm as it iterates only once through the list

def maxSumSequence(sequence):
    maxSum = 0
    maxSumTillNow = 0
    maxSumSeqTillNow = []
    maxSumSeq = []
    for num in sequence:
        if maxSum+num>0:
            maxSum = maxSum + num
            maxSumSeq = maxSumSeq + [num]
            if maxSum > maxSumTillNow:
                maxSumTillNow = maxSum
                maxSumSeqTillNow = maxSumSeq
        else:
            maxSum = 0
            maxSumSeq = []
    return maxSumTillNow, maxSumSeqTillNow

print maxSumSequence([4,5,-1,-6,-4,-3,2,3,4,5,-7,-9,10])
print maxSumSequence([4,5,-1,-6,-4,-3,2,3,4,5,-7,-5,10])
print maxSumSequence([4,5,-1,-6,-4,-3,2,3,4,5,-7,-5,10,5])
print maxSumSequence([])
print maxSumSequence([-1,-2,-3])
print maxSumSequence([5])
