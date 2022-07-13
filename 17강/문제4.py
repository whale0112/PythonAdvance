def solution(words):
    answer = ''
    for a in words:
        if len(a) >= 5:
            answer += a
    
    if answer == '':
        return 'empty'

    return answer
words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1)
print(ret1)

words2 = ["yes", "i", "am"]
ret2 = solution(words2)
print(ret2)