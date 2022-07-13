def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    for a in range(0, len(str), 1):
        if str[a] == str[len(str) - 1 - a]:
            continue
        else:
            return False
    return True    
    

sentence1 = 'never odd or even.'
ret1 = solution(sentence1)
print(ret1)

sentence1 = 'palindrome'
ret1 = solution(sentence1)
print(ret1)