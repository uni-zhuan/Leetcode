#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#碰第一个链表题，类上方声明，直接用链表名表示是否为空，链接用next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #合并到的新链表
        head=cur=ListNode(0)
        while list1 and list2:
            print(list1,list2)
            if list1.val>list2.val:
                cur.next=list2
                list2=list2.next
            else:
                cur.next=list1
                list1=list1.next
            #cur向前进一个节点
            cur=cur.next
        # cur.next=list1 or list2
        if list1:   
            cur.next=list1
        elif list2:
            cur.next=list2   
        return head.next 

# @lc code=end

