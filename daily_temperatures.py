
def daily_temp(temperatures):

    # stack

    res = [0] * len(temperatures)

    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, stack_ind = stack.pop()
            res[stack_ind] = i - stack_ind
        stack.append((temp,i))

    return res

        
  
if __name__ == '__main__':

    temps = [30,38,30,36,35,40,28]

    result = daily_temp(temps)

    print(result)