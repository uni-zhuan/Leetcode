#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
     def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum=0
        last=s[-1]
        for i in reversed(s):
            # reversed返回一个反向的 iterator,从大到小排列因此反向迭代
            if i=="C" and last in["D","M"]:
                sum-=roman[i]
            elif i=="X" and last in["L","C"]:
                sum-=roman[i]
            elif i=="I" and last in["V","X"]:
                sum-=roman[i]
            else:
                sum+=roman[i]
            last=i
        return sum

    # def romanToInt(self, s: str) -> int:
    #     d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
    #     return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

    # def romanToInt(self, s: str) -> int:
    #     sum=0
    #     slist=list(s)
    #     print(slist)
    #     sdict=[0,0,0,0,0,0,0]
    #     i=0
    #     while i < len(slist):
    #         print(slist[i])
    #         if slist[i]=="I":
    #             if(i<len(slist)-1 and slist[i+1]=="V"):
    #                 sum+=4
    #                 i+=2
    #             elif(i<len(slist)-1 and slist[i+1]=="X"):
    #                 sum+=9
    #                 i+=2
    #             else:
    #                 sdict[0]+=1
    #                 i+=1
    #         elif slist[i]=="V":
    #             sdict[1]+=1
    #             i+=1
    #         elif slist[i]=="X":
    #             if(i<len(slist)-1 and slist[i+1]=="L"):
    #                 sum+=40
    #                 i+=2
    #             elif(i<len(slist)-1 and slist[i+1]=="C"):
    #                 sum+=90
    #                 i+=2
    #             else:
    #                 sdict[2]+=1
    #                 i+=1
    #         elif slist[i]=="L":
    #             sdict[3]+=1
    #             i+=1
    #         elif slist[i]=="C":
    #             if(i<len(slist)-1 and slist[i+1]=="D"):
    #                 sum+=400
    #                 i+=2
    #             elif(i+1<len(slist) and slist[i+1]=="M"):
    #                 sum+=900
    #                 i+=2
    #             else:
    #                 sdict[4]+=1
    #                 i+=1
    #         elif slist[i]=="D":
    #             sdict[5]+=1
    #             i+=1
    #         elif slist[i]=="M":
    #             sdict[6]+=1
    #             i+=1
    #     print(sdict)
    #     sum+=sdict[0]
    #     sum+=sdict[1]*5
    #     sum+=sdict[2]*10
    #     sum+=sdict[3]*50
    #     sum+=sdict[4]*100
    #     sum+=sdict[5]*500
    #     sum+=sdict[6]*1000
    #     return sum
  
# @lc code=end





