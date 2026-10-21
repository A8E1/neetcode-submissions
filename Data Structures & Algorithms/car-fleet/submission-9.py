class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]


        cars.sort(reverse=True)
        fleets = []
        for car in cars:
            arrival = (target - car[0]) / car[1]

            if fleets and arrival > fleets[-1]:
                fleets.append(arrival)
            elif not fleets:
                fleets.append(arrival)
        
        return len(fleets)
            




