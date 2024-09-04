def solution(phone_book):
    answer = True

    numberHash = dict()

    phone_book.sort(key=lambda x: len(x))

    for number in phone_book:
        for i in range(len(number)):
            s = number[0:i + 1]

            if s in numberHash.keys():
                answer = False
                break

        numberHash[number] = True

    return answer
