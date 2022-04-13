#if ():
# 조건이 False인 경우
# 1. 0 일때
# 2. [], {}... 빈 컨테이너일 때
# 3. "" 빈 문자열 일 때
# 4. None
# 5. False
# 6. 표현식이 안맞을 때

# if "0":
# print("이거 나옴")

# else:
# if 조건에 해당되지 않을 때 실행

# money = 10000
# if money > 100
#   print("돈이 참 많으시군요")
# else:
#   print("저축하자 저축")

# elif
# else if
# score = 88
# if score >= 90:
#   print("A")
# else:
#   if score >= 80:
#       print("B")
#   else:
#       if score >= 70:
#           print("C")
#       else:
#           print("F")

# nums = [5, 5, 5, 5, 5, 5]
# max_value = 0
# min_value = 987654321

# for i in nums:
#   if max_value <= i:
#       max_value = i
#   elif mmin_value >= i:
#       min_value = i

# print(max_value, min_value)
# if / if 무조건 전부 확인
# if / elif  선행 if 가 아닐때만 확인

# 조건식 ? 참 : 거짓

# 조건표현식 참 if 조건 else 거짓
# money = 10000
# happy = True if money >= 1000000 else "False"
# print(happy)

# happy2 = "나는 부자야" if money >= 1000000 else "나는 돈이 많아"

# print(happy2)

# 논리연산자
# and (&&) : 두 조건문 다 True일때만 True
# or (||) : 두 조건문 중 하나라도 True이면 True

def T():
    print("트루")
    return True

def F():
    print("펄쓰")
    return True

if T() and T():
    print("실행!")
if T() and T():
    print("실행!")
if T() and T():
    print("실행!")
if T() and T():
    print("실행!")

if T() or T():
    print("실행!")
if T() or F():
    print("실행!")
if F() or T():
    print("실행!")
if F() or F():
    print("실행!")

arr = [1, 2, 3, 4]
idx = 4

if F() and arr[idx]:
    print(arr[idx])

if arr[idx] and F():
    print(arr[idx])

print( 3 or 5)
print( 3 and 5)
print( 0 or 3)
print( 0 and 5)