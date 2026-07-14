class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [[p, s] for p, s in zip(position, speed)]

        fleets.sort(reverse=True)

        #now we have a decreasing list of all the cars based on 
        #their current position

        stack = []
        for car in fleets:
            arrival_time = (target - car[0])/car[1]
            stack.append(arrival_time)


            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()

        
        return len(stack)

        