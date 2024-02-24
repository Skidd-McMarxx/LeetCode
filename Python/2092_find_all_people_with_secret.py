from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        secrets = set([0, firstPerson])
        timetable = {}
        for p1, p2, t in meetings:
            if t not in timetable:
                timetable[t] = defaultdict(list)
            timetable[t][p1].append(p2)
            timetable[t][p2].append(p1)

        def dfs(p, time):
            if p in visit:
                return
            visit.add(p)
            secrets.add(p)
            for nei in time[p]:
                dfs(nei, time)

        for t in sorted(timetable.keys()):
            visit = set()
            for per in timetable[t]:
                if per in secrets:
                    dfs(per, timetable[t])

        return list(secrets)
