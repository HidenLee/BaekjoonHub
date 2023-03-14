T = int(input())
for test_case in range(T):
    sx, sy, gx, gy = map(int,input().split())
    N = int(input())
    stars = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for star in stars:
        if (star[0]-sx)**2+(star[1]-sy)**2 < star[2]**2:
            if (star[0]-gx)**2+(star[1]-gy)**2 > star[2]**2:
                cnt += 1
        elif (star[0]-sx)**2+(star[1]-sy)**2 > star[2]**2:
            if (star[0]-gx)**2+(star[1]-gy)**2 < star[2]**2:
                cnt += 1
    print(cnt)