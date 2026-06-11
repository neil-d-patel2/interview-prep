'''

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

'''
# Syntax Notes:

'''
- can extract tuples from hashmaps, just iterate using h.items()

- use sorted on tuples 

- .sort is meant for the list class and is nlgn time, thats why sorted is for most other data structures 

- sorted returns a completely new object, .sort modifies the object that it was called with and doesnt return anything

- can access tuples in a list using 2d array notation, eg, first element of the first tuple in a list can be accessed using my_tuple_list[0][0] 
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        h = Counter(nums)

        # h is now a hashmap of integers -> how many times they appear in the array
        all_elements = []
        for key,value in h.items():
            tuple_kvp = (value, key)
            all_elements.append(tuple_kvp)

        sorted_data = sorted(all_elements)
        
        i = -1
        k_elements = []
        for _ in range(k):
            k_elements.append(sorted_data[i][1])
            i -= 1

        print(sorted_data)
        return k_elements

    



