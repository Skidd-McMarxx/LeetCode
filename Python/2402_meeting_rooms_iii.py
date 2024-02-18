import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        available_rooms = [i for i in range(n)]
        used_rooms = []
        meetings_count = [0] * n

        for start_time, end_time in meetings:
            while used_rooms and start_time >= used_rooms[0][0]:
                _, room_number = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room_number)
            # Not available
            if not available_rooms:
                used_end_time, room_number = heapq.heappop(used_rooms)
                end_time = used_end_time + (end_time - start_time)
                heapq.heappush(available_rooms, room_number)
            # available
            room_number = heapq.heappop(available_rooms)
            heapq.heappush(used_rooms, (end_time, room_number))
            meetings_count[room_number] += 1

        return meetings_count.index(max(meetings_count))
