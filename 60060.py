from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    wordsByNumber = [[] for n in range(10001)]  # Make list for Number of characters
    wordsByNumberReverse = [[] for k in range(10001)]  # Make list for Number of characters By reverse

    for w in words:
        wordsByNumber[len(w)].append(w)  # Append to wordsByNumber by Number of characters
        wordsByNumberReverse[len(w)].append(''.join(list(reversed(w))))  # Append to wordsByNumberReverse with reversed character

    for i in range(10001):  # sort to use 
        wordsByNumber[i].sort()
        wordsByNumberReverse[i].sort()

    for query in queries:
        count = 0
        length = len(query)

        if query[0] == '?':  # start with '?'
            query = query[::-1]  # reverse query

            left = bisect_left(wordsByNumberReverse[length], query.replace('?', 'a'))
            right = bisect_right(wordsByNumberReverse[length], query.replace('?', 'z'))

        else:  # end with '?'
            left = bisect_left(wordsByNumber[length], query.replace('?', 'a'))
            right = bisect_right(wordsByNumber[length], query.replace('?', 'z'))

        count += right - left
        answer.append(count)

    return answer
