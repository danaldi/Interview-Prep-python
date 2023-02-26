##### I'm not sure if it's the best way to do it, but it works, and it's original :D


#### Check wether are two strings isomorphic or not
''' 
Logic:
1. Create two empty dictionary, one for s and one for t (we need 2 because we need to check if 
    the character is already in string 1 or in string 2)
2. Iterate through the two strings, if the character is not in the dictionary, add it
    example s=badc and t=baba
3. If the character is already in the dictionary, check if the value of the character is the same as the value of the character in the other string
    
    example : first iteration dict1 = {b:b} and dict2 = {b:b}, third iteration dict1 = {b:b, a:a, d:b} and dict2 = {b:b, a:a, b:d}
    notice that the value of d in dict1 is b, and the value of b in dict2 is d, hence the return are false,
    we cant check this if we only use 1 dictionary
4. return true if the iteration is done, return false if condition are met
'''
def isIsomorphic(s, t):

    new_dict=dict()
    new_dict2=dict()
    if (len(s)!=len(t)):
        return False
    
    for i,j in zip(s,t):
        if (i in new_dict and j !=new_dict[i] ):
            return False
        if (j in new_dict2 and i !=new_dict2[j] ):
            return False
        new_dict[i]=j
        new_dict2[j]=i
    return True

#### Finding the pivot index, if not found return -1
'''
logic:
1. Create a variable to store the sum of the list
2. Create a variable to store the sum of the left side of the list
3. Iterate through the list, if the sum of the left side is equal to the sum of the right side, return the index
4. If the sum of the left side is not equal to the sum of the right side, add the current number to the left side sum
5. If the iteration is done, return -1
'''
def pivotIndex(self, nums):

    sum_list= sum(nums)
    left_total = 0
    for i, num in enumerate(nums):
        if (left_total==sum_list-num-left_total):
            return i
        left_total+=num
    return -1

#### Running sum of 1d array
'''
logic:
1. Create a new list to store the running sum
2. Create a variable to store the sum of the list
3. Iterate through the list, add the current number to the sum variable
4. Append the sum variable to the new list
5. Return the new list
'''
def runningSum(self, nums):
        new_list= []
        added_nums=0
        for i in range (len(nums)):
            added_nums+=nums[i]
            new_list.append(added_nums)
        return new_list

#### is subsequence , only check are s is a subsequence of t
'''
logic:
1. Create two variables to store the index of the two strings
2. Iterate through the two strings, if the character in the first string is equal to the character in the second string, increment the index of the first string
3. Increment the index of the second string
4. Return true if the index of the first string is equal to the length of the first string, return false if the iteration is done
'''

def isSubsequence(self, s: str, t: str) -> bool:
    index_s=0
    index_t=0
    while (index_s < len(s) and index_t < len(t)):
        if (s[index_s]==t[index_t]):
            index_s+=1
        index_t+=1
    return len(s)==index_s
