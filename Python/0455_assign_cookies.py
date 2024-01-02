class Solution(object):
    def findContentChildren(self, g:list[int], s:list[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        children_feed, cookies_index = 0, 0        
        while children_feed < len(g):
            while cookies_index < len(s) and g[children_feed] > s[cookies_index]:
                cookies_index += 1
            if cookies_index < len(s):
                children_feed += 1
                cookies_index += 1
            elif cookies_index >= len(s):
                break
        return children_feed