# 델타를 이용한 이동 (햔재 위치기준)
# 문제에서 방향이 주어진다면 해당 방향을 따르고 그게 아니라면 내가 설계한대로 할것

# 상하좌우

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
# 여기 값 바꿔가면서 해보자
r = 1
c = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0] * 3 for _ in range(3)]
# drc = [[-1, 0 ],[1, 0],[0, -1], [0, 1]]
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    # nr2 = r + drc[i][0]
    # nc2 = c + drc[i][1]

    # X
    # if visited[nr][nc] == 0 and 0 <= nr < 3 and 0 <= nc < 3:
    #   print(arr[nr][nc])

    # O 범위검사를 먼저 해야함.
    # if 0 <= nr < 3 and 0 <= nc < 3 and visited[nr][nc] == 0:
    #   print(arr[nr][nc])

    # 쳐내기
    if 0 > nr or nr >= 3 or 0 > nc or nc >=3: continue
    if visited[nr][nc]: continue
    print(arr[nr][nc])
