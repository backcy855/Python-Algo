
'''
1
6
1 1 1 1 1 1
1 1 1 3 3 3 
4 1 1 3 3 3
4 1 1 3 3 3
1 2 2 2 1 1
1 2 2 2 1 1
3
1 3
3 3 
6 3
'''
dr = [-1 ,1 ,0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 입력 인덱스를 맞추어 주기 위해서 띠를 들렀다
    city = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    city.append([0] * (N+2))
    M = int(input())
    ans = 0
    for _ in range(M):
        r, c = map(int, input().split())
        # 입력 받은 좌표에 대해서 상하좌우 돌면서 ans에 누적시키기
        ans += city[r][c]
        city[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 띠를 두르면 맵 범위 검사가 필요없어짐
            if 0 < nr <= N and 0 < nc <= N:
                ans += city[nr][nc]
                city[nr][nc] = 0
        for i in city:
            print(*i)
        print("#{} {}".format(tc, ans))

'''
N * N 크기의 맵, 각 칸은 해당 도시의 자원이라고 한다.
폭탄맨은 폭탄을 터뜨릴 수 있다.
폭탄은 해당위치 포함 상하좌우 4방향으로 길이는 1만큼만 터진다
폭탄맨이 오늘밤 이곳에 M개의 폭탄을 터뜨리겠다고 예고를 날려왔다.
총 피해는 어느정도 인가?
'''
# 만약 폭탄의 폭발범위가 1이 아니라 특정 정수가 주어진다면?????