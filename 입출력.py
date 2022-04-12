# 입력
# input() 문자열의 형태로 입력, 한줄을 통으로 입력 받는다.

# split()은 넣어준 인자를 기준으로 list를 반환해준다. 기본값은 공백
# list()는 리스트로 바꿔준다
# 공백을 기준으로 쪼개서 넣고 싶을때
# 가 나 다 라 마 바
# input().split()

#가나다라마바사 처럼 공백없이 붙어서 들어오는 경우 리스트로 쪼개고 싶다면
# list(input())

#첫번째로 전체 테스트케이스 수 T가 주어진다.(정수1개)
# T = int(input())

# map(함수, 반복할 수 있는 것) 맵 객체를 반환함.
# 실제 반환하는 개수만큼의 변수를 지정하게 되면 각각의 변수에 집어 넣게 됨.

# 정수를 두개 입력 받는 방법
# 좌표의 값이 주어진다 / 행의크기와 열의크기가 주어진다.
# 5 9
# 두개 정도는 변수를 저징하여 사용하는 경우가 많음.

# N, M = map(int, input().split())
# print(N, M)

# 여러개의 공백으로 구분이 되는 정수를 입력 받자
# 1 2 3 4 5 6 7 8
# arr = list(map(int, input().split()))
# print(arr)

# 전부 한자리 수이다. 리스트로 입력을 받아보자!!
# 1234567
# arr =list(map(int, input()))
# print(arr)

#def minus(N):
#   return int(N) - 1

# arr = list(map(minus, input().split()))
#print(arr)

#이차원 입력
# 3 * 3 크기의 2차원리스트가 주어진다.
# 1 2 3
# 4 5 6
# 7 8 9

# N = 3
# 리스트 내포 방식
# arr = [list(map(int, input().split())) for - in range(N)]

# 리스트 추가
# arr = []
# for i in range(N):
#   tmp = list(map(int, input().split()))
#   arr.append(tmp)

# print(arr)

# 출력
# print() 기본적으로 end라는 속성에 \n

# arr = [1, 2, 3]
# 1 2 3 으로 출력해보세요.

# print(*arr)
# T = 3
# for tc in range(1, T + 1):
#   # 블라블라 출력을 하자
#      print('#{}'.format(tc))
#      for i in arr:
#           print(i, end=" ")
#       print()

# 1 1 2 3
# 2 1 2 3
# 3 1 2 3

# print(arr[0], arr[1], arr[2])

