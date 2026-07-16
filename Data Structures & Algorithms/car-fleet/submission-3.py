class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [[p, s] for p, s in zip(position, speed)]

        fleets.sort(reverse=True)

        stack = []
        for car in fleets:
            arrival = (target - car[0])/car[1]

            
            stack.append(arrival)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        
        return len(stack)