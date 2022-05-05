/*
 * @lc app=leetcode.cn id=83 lang=cpp
 *
 * [83] 删除排序链表中的重复元素
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *deleteDuplicates(ListNode *head)
    {
        if (head == nullptr)
        {
            return head;
        }
        // if (head->next->next == nullptr)
        // {
        //     return head;
        // }
        ListNode *newlist=new ListNode(head->val);
        ListNode *newp = newlist;
        ListNode *p = head;
        while (p->next != nullptr)
        {

            if (p->val == p->next->val)
            {
                // p = p->next;
                cout << "head,p" << p->val << endl;
            }
            else
            {
                newp->next = p->next;
                newp = newp->next;
                
            }
            // 
            p = p->next;

        }
        cout<<p->val<<endl;
        newp->next=nullptr;
        return newlist;
    }
};
// @lc code=end
