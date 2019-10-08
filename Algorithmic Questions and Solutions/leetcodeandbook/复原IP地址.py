# -*-coding:utf-8 -*-
# @Time :2019/8/1318:53
# @Author : liupengrui
# @FileName :fuyuanIP.py

s = '226111111111'
if len(s) > 12 or len(s) < 4:
    print([])
ls = []
if len(s) % 4 == 0:
    step = len(s) // 4
    k = 0
    while k < len(s):
        ls.append(s[k:k + step])
        k += step
for i in range(len(ls)):
    if ls[i] > '255':
        print([])
        break
print('.'.join(ls))


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def valid(segment):  # 分割segment
            """
            Check if the current segment is valid :
            1. less or equal to 255
            2. the first character could be '0'
               only if the segment is equal to '0'
            """
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):  # 更新当前的位置
            """
            Append the current list of segments
            to the list of solutions
            """
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            """
            prev_pos : the position of the previously placed dot
            dots : number of dots to place
            """
            # The current dot curr_pos could be placed
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed
            # after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):  # 最右边必须有一个数
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed 每次加入的都是dot之前的，最终需要把dot之后的也加入
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot

        n = len(s)
        output, segments = [], []
        backtrack()
        return output


mm = Solution
print(mm.restoreIpAddresses('1111'))
