[Problem Link](https://leetcode.com/problems/add-two-numbers/)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Example:

> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
> Output: 7 -> 0 -> 8
>  Explanation: 342 + 465 = 807.


## Solution : 

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1 = 0
        x2 = 0
        count1 = 0
        count2 = 0
        iter1 = l1
        iter2 = l2 
        while(iter1 != None):
            x1 +=  iter1.val * 10 ** count1
            count1 += 1
            iter1 = iter1.next
        while(iter2 != None):
            x2 +=  iter2.val * 10 ** count2
            count2 += 1
            iter2 = iter2.next
            
        sums = x1 + x2
        l = ListNode(sums%10)
        iter = l
        while(1):
            
            sums = sums // 10
            if sums == 0:
                break
            iter.next = ListNode(sums%10)  
            iter = iter.next
        return l

```
