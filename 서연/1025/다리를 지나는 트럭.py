from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque([0] * bridge_length)
    
    currentWeight = 0
    while len(truck_weights) > 0:
        time += 1

        currentWeight -= q.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            q.append(truck_weights.pop(0))

        else: 
            q.append(0)
            
    time += bridge_length
    
    return time