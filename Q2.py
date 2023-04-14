class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        temp=ans
        while list1 or list2:
            if list1 and not list2:
                while list1:
                    next_value=list1.val
                    list1=list1.next
                    temp.next=ListNode(next_value)
                    temp=temp.next
            elif list2 and not list1:
                while list2:
                    next_value=list2.val
                    list2=list2.next
                    temp.next=ListNode(next_value)
                    temp=temp.next
            else:
                if list1.val>=list2.val:
                    next_value=list2.val
                    list2=list2.next
                    temp.next=ListNode(next_value)
                    temp=temp.next
                else:
                    next_value=list1.val
                    list1=list1.next
                    temp.next=ListNode(next_value)
                    temp=temp.next
        return ans.next