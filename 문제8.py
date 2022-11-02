# 소수점 이하 첫째자리까지 문자열 만들기 : "{:.1f}".format(123.456) # 123.4
# 소수점 이하 둘째자리까지 문자열 만들기 : "{:.2f}".format(123.456) # 123.45
# 소수점형변환 : float(4) # 4.0
# 절대값함수(음수를 넣으면 양수가 나오고, 양수를 넣으면 양수) : 

def solution(hour, minute):
    answer = ''
    if 30 * hour + 0.5 * minute > 6 * minute:
        answer = 30 * hour + 0.5 * minute - 6 * minute
    else:
       answer = 6 * minute - 30 * hour + 0.5 * minute
    answer = "{:.1f}".format(answer)
    return answer

hour = 3
minute = 0
ret = solution(hour, minute)
print("solution 함수의 반환 값은 ", ret, " 입니다.")
