class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = []
        l1_num = 0
        l2_num = 0
        i = 1
        j = 1
        while l1:
            if l1:
                l1_num = l1_num + l1.val * i
                l1 = l1.next
                i = 10 * i

        while l2:
            l2_num = l2_num + l2.val * j
            l2 = l2.next
            j = 10 * j

        l3_num = l1_num + l2_num
        l3_num_str = str(l3_num)
        l3_num_list = list(l3_num_str)

        for i in l3_num_list:
            l3.append(int(i))

        return l3[::-1]


l1 = [2, 4, 3]
l2 = [5, 6, 4]
s = Solution()
print(s.addTwoNumbers(l1, l2))

