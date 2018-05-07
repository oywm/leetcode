import time
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        nums = []
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        for i in range(n):
            #这里直接用字符而不用列表是因为时间复杂度的原因
            #temp = [s[i]]
            temp = s[i]
            for j in range(i + 1, n):
                if s[j] not in temp:
                    #这里的append是用列表来更新，可是时间通不过。
                    # temp.append(s[j])
                    temp += (s[j])

                    #这里是如果已经到最后一位了就不用再执行查找了，因为该字串已经是最长的了没必要再进行往后面找了
                    if j == (n - 1):
                        nums.append(len(temp))
                        return max(nums)
                else:
                    nums.append(len(temp))
                    break
        return max(nums)




#
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         if s == '':
#             return 0
#         if len(s) == 1:
#             return 1
#         subcount = set()
#         substrings = set()
#         for i in range(len(s)-1):
#             substring = s[i]
#             for j in range(i+1, len(s)):
#                 if s[j] not in substring:
#                     substring += s[j]
#                     if j == len(s)-1:
#                         substrings.add(substring)
#                         subcount.add(len(substring))
#                         return max(subcount)
#                 else:
#                     substrings.add(substring)
#                     subcount.add(len(substring))
#                     break
#         return max(subcount)


start = time.time()
s = Solution()
a = s.lengthOfLongestSubstring('pwwkew')
end = time.time()
print(a)
print(end - start)