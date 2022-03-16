# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         temp = head.next
#         head2 = ListNode()
#         while temp != None: # temp  = 2
#             # print(temp.val)
#             next_node = temp.next # next_node = 3
#             # if (next_node != None):
#             if next_node == None:
#                 head2.next = temp
#                 # next_node.next =  temp
#                 break
#             # next_temp = next_node.next # next_temp = 
#             next_node.next = temp #next_node.next = 2
#             temp = next_node 

#         head.next = temp
#         return head2
    
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """   
        prev = None
        curr = head # curr = 1
        while curr is not None: #curr = 2
            next_ = curr.next # next_ = 3
            curr.next = prev
            prev = curr # prev = 1
            curr = next_
        
        # head = ListNode()
        # head.next = prev
        head = prev
        return head
    
    
    
head = ListNode()
one = ListNode(1)
two = ListNode(2)
thr = ListNode(3)
head.next = one
one.next = two
two.next = thr
thr.next = None
# print(head.val)
sol = Solution()
print(sol.reverseList(head).val)
            # head.next.next = head
            
            
            
# def reverse(self):
#         prev = None
#         current = self.head # current = 1
#         while(current is not None):
#             next = current.next # next = 2
#             current.next = prev #current_next = None
#             prev = current #prev = 1
#             current = next #current = 2
#         self.head = prev