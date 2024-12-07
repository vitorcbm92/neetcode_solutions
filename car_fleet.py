
def car_fleet(target, position, speed):

    stack = []

    car_pos_speed = sorted(zip(position, speed), reverse=True)    

    for p, s in car_pos_speed:
        stack.append((target - p)/s)
        if len(stack) >=2 and stack[-1] <= stack[-2]:
            stack.pop()        
    return len(stack)


if __name__ == '__main__':

    target=10
    position=[3,5,7]
    speed=[3,2,1] 

    print(car_fleet(target, position, speed))