class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
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

    x = ListNode(2)
    x.next = ListNode(4)
    x.next.next = ListNode(3)

    y = ListNode(5)
    y.next = ListNode(6)
    y.next.next = ListNode(4)

##
    iter = addTwoNumbers(x,y)
    while(iter != None):
        print(iter.val)
        iter = iter.next
