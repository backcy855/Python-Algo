# 반복문은 똑같은 일을 편하게 하려고 씀

arr = [5, 6, 7, 8, 9]
# for
# arr[0] += 1
# arr[1] += 1
# arr[2] += 1
# arr[3] += 1
# arr[4] += 1

# 1. 실제 리스트를 돌려서 가져오기
# for i in arr:
# 일시적으로만 씀임
#   print(i+1)

# 2. range 객체를 사용해 인덱스로 접근하는 방법
# for i in range(len(arr)):
#   arr[i] += 1
#   print(arr[i])

# range
# 인자 1개 (끝+1)
# 인자 2개 (시작, 끝+1)
# 인자 3개 (시작, 끝+1, 간격)

# print(list(range(10)))

# break, continue, pass

# continue를 사용하려면 의미있게 사용하자.
# for i in range(10)
#   if i % 2:
#       print(i)
#   else:
#       continue


# for i in range(10):
#   if i % 2 == 0:
#       continue
#   print(i)

# 이방식은 추천하지 않음...
# for i in range(10):
#   if i % 2:
#       print(i)
#   else:
#       continue

# for i in range(10):
#   if i % 2 == 0:
#       continue
#   print(i)

# 이 방식은 추천하지 않음..
# for i in range(10):
#   if i % 2 == 0:
#       pass
#   else:
#       print(i)

# for-else 구문 반복문을 돌던 중 브레이크에 한번도 걸리지 않으면
# else 구문을 수행하고 한번이라도 걸리면 else는 수행되지 않음.

# for i in range(5):
#   if i > 2:
#       break
#   print(i)
# else:
#   print("중간에 break되지 않는다.")

# while 조건식:
#   코드 내용

# 이건 무조건 해보자...
idx = 0
while True:
    idx += 1
    if idx == 3:
        break
    print(idx)

# while idx < 3:
#   idx += 1
#   print(idx)

