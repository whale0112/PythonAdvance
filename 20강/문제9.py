def solution(password):
    length = len(password)
    for i in range(length - 2):
        first_check = ord(password[i + 1]) - ord(password[i])
        second_check = ord(password[i]) - ord(password[i-1])
        if first_check == second_check and (first_check == 1 or first_check == -1):
            return False
    return True

password1 = "cospro890"
ret1 = solution(password1)
print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "cba323"
ret2 = solution(password2)
print("solution 함수의 반환 값은", ret2, "입니다.")

# ord : 하나의 문자를 인자로 받고 해당 문자에 해당하는 아스키코드를 반환합니다. 
# ord('a')를 넣으면 정수 97을 반환합니다.
