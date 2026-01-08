class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clock = 0
        counter_clock = 0

        if start < destination:
            clock = sum(distance[start:destination])
            counter_clock = sum(distance[destination:]) + sum(distance[:start])
        
        if destination < start:
            clock = sum(distance[start:]) + sum(distance[:destination])
            counter_clock = sum(distance[destination:start])
        
        return min(clock, counter_clock)