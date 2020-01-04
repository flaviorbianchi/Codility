# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    result = 0
    
    binaryN = list(bin(N)[2:])

    for i in range(len(binaryN)):
        if (binaryN[i] == '1') and (i < len(binaryN)-1):
            pointer = i+1
            longest = 0
            while(pointer < len(binaryN)):
                if (binaryN[pointer] == '1'):
                    if (longest > result):
                        result = longest
                    longest = 0
                else:
                    longest = longest + 1
                pointer += 1

    return result


print(solution(32))

# or example, given N = 1041 the function should return 5,
# because N has binary representation 10000010001 and so its 
# longest binary gap is of length 5. Given N = 32 the function 
# should return 0, because N has binary representation '100000' 
# and thus no binary gaps.
