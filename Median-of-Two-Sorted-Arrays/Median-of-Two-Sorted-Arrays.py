class Solution:

    def findMedianSortedArrays( arr1, arr2):
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
       
    x1 = [1,3]
    x2 = [2]
    print(findMedianSortedArrays(x1,x2))
        
    x1 = [1,2]
    x2 = [3,4]
    print(findMedianSortedArrays(x1,x2))
