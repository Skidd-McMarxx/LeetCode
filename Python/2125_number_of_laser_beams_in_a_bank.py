class Solution(object):
    def numberOfBeams(self, bank:list[str]) -> int:
        beams, prev = 0, 0
        for row in bank:
            curr = row.count("1")            
            if curr != 0:
                beams += curr * prev
                prev = curr
        return beams