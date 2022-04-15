text = "this iss a book~! is"
pt = "iss"
N = len(text)  # 전체 텍스트의 길이
M = len(pt)  # 전체 패턴의 길이
# if pt in text:
#   print("들어 있음")

# 이중 for문으로 얘가 들어있는지 확인하는 코드를 작성해보자
for i in range(N - M + 1):
    # 패턴을 돌면서 실제로 확인을 해보자
    # flag = True
    for j in range(M):
        if pt[j] != text[i + j]:
            # flag = False
            break
        # if flag:
        #   print(i, "에서 시작하면 패턴이 있음")
        else:
            print(i, "에서 시작하면 패턴이 있음")

for i in range(N - M + i):
    # 패턴을 돌면서 실제로 확인을 해보자.
    cnt = 0
    for j in range(M):
        if pt[j] == text[i + j]:
            cnt += 1

    if cnt == M:
        print(i, "에서 시작하면 패턴이 있음")

# while문으로도 한번 작성해보자

p = "is"  # 찾을 패턴
t = "This is a book~!"  # 전체 텍스트
M = len(p)  # 찾을 패턴의 길이
N = len(t)  # 전체 텍스트의 길이


def BruteForce(p, t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M  # 검색 성공
    else:
        return - 1  # 검색 실패


