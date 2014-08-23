# Given a list of integers as an input find the powerset
# Eg: [1,2,3] should return
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

def dtob(num):
    binary = ''
    while num>0:
        binary = '0' + binary if num%2==0 else '1' + binary
        num = num/2
    return binary

def powerset(numSet):
    powerSet = []
    li = map(dtob,range(2**len(numSet)))
    for binary in li:
        binary = '0'*(len(numSet)-len(binary)) + binary
        powerSet.append(makeSet(numSet,binary))
    return powerSet

def makeSet(numSet,binary):
    tempSet=[]
    for i,val in enumerate(binary):
        if val=='1':
            tempSet = tempSet + [numSet[i]]
    return tempSet

print powerset([1,2,3])
print powerset([])
print powerset([1])


