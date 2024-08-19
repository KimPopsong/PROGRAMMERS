import heapq


def solution(cacheSize, cities):
    runTime = 0  # 실행 시간

    cache = dict()  # 시간 : 도시
    cacheValues = dict()  # 도시 : 시간

    for time in range(len(cities)):
        city = cities[time].upper()  # 대소문자 구분 X, 모두 대문자로 치환

        if city in cacheValues:  # 캐시에 이미 있다면
            runTime = runTime + 1

            value = cacheValues[city]
            cacheValues[city] = time
            cache[time] = city
            del cache[value]

        else:  # 캐시에 없다면
            runTime = runTime + 5

            if (cacheSize):  # 캐시의 크기가 0이 아니라면
                if (len(cache) < cacheSize):  # 캐시에 빈 공간이 있다면
                    cache[time] = city
                    cacheValues[city] = time

                else:  # 캐시에 빈 공간이 없다면
                    minTime = min(cache.keys())  # 가장 오래된 캐시를 삭제하고
                    delCity = cache[minTime]
                    del cache[minTime]
                    del cacheValues[delCity]

                    cache[time] = city  # 새로운 값 추가
                    cacheValues[city] = time

    return runTime
