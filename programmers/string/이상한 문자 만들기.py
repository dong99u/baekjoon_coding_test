def solution(s: str):
    answer = []

    for word in s.split(' '):
        new_word = ''
        for i, w in enumerate(word):
            if i % 2 == 0: # 짝수라면
                new_word += w.upper()
            else:
                new_word += w.lower()
        answer.append(new_word)

    return ' '.join(answer)

print(solution('try hello world'))
