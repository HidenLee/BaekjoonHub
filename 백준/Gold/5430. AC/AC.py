for _ in range(int(input())):
    cmd = input()
    M = int(input())
    
    arr_input = input()[1:-1]
    if arr_input:
        arr = list(map(int, arr_input.split(',')))
    else:
        arr = []

    isReverse = False
    left = 0
    right = M - 1
    error_flag = False

    for elm in cmd:
        if elm == "R":
            isReverse = not isReverse
        elif elm == "D":
            if left <= right:
                if isReverse:
                    right -= 1
                else:
                    left += 1
            else:
                print("error")
                error_flag = True
                break

    if not error_flag:
        result = arr[left:right+1]
        if isReverse:
            result.reverse()
        print("[" + ",".join(map(str, result)) + "]")