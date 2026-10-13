class Solution(object):
    def backspaceCompare(self, s, t):
        a = ""
        b = ""
        for c in s:
            if c == '#':
                a = a[:-1]
            else:
                a += c

        for c in t:
            if c == '#':
                b = b[:-1]
            else:
                b += c

        return a == b
