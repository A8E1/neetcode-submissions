class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]

        cars.sort(reverse=True)
        first_arrival = (target-cars[0][0])/cars[0][1]
        fleets = []
        fleets.append(first_arrival)

        for car in cars:
            arrival_time = (target - car[0])/car[1]
            if fleets and arrival_time > fleets[-1]:
                fleets.append(arrival_time)
        

        return len(fleets)