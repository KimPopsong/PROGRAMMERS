def solution(routes):
    camera = 1

    routes.sort(key=lambda x: x[1])

    nod = routes[0][1]
    for index, route in enumerate(routes):
        if route[0] > nod:
            camera += 1
            nod = route[1]

    return camera
