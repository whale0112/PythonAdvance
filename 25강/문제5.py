def reverse(s):
  s2 = ''
  for i in range(len(s)):
      s2 += s[len(s)-i-1]
      return s2

def solution(n):
    answer = ''
    for i in range(n):
        answer += str(1 + i%9)
        answer = reverse(answer)
    return answer

n = 5
ret = solution(n)
print("solution 함수의 반환 값은", ret, "입니다.")
