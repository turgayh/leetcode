[Problem Link](https://leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
```
Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```
```
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```


## Solution

```Python
class Solution:

    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        n1 = len(arr1)
        n2 = len(arr2)
        arr3 = [None] * (n1 + n2) 
        i = 0
        j = 0
        k = 0

        # Traverse both array 
        while i < n1 and j < n2: 

            # Check if current element  
            # of first array is smaller  
            # than current element of  
            # second array. If yes,  
            # store first array element  
            # and increment first array 
            # index. Otherwise do same  
            # with second array 
            if arr1[i] < arr2[j]: 
                arr3[k] = arr1[i] 
                k = k + 1
                i = i + 1
            else: 
                arr3[k] = arr2[j] 
                k = k + 1
                j = j + 1


        # Store remaining elements 
        # of first array 
        while i < n1: 
            arr3[k] = arr1[i]; 
            k = k + 1
            i = i + 1

        # Store remaining elements  
        # of second array 
        while j < n2: 
            arr3[k] = arr2[j]; 
            k = k + 1
            j = j + 1
        n3 = len(arr3)
        if(n3%2 == 0):
            return (arr3[n3 // 2 - 1 ] + arr3[n3 // 2 ]) / 2
        else:
            return arr3[n3 // 2]
```
