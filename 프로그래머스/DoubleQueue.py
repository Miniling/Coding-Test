def solution(operations):
    answer = []

    queue = []
    # 명령어 판단
    for i in range(len(operations)):
        data = operations[i].split(' ')
        operator = data[0]
        number = int(data[1])
        if (operator == "I"):
            queue.append(number)
        elif (len(queue) > 0 and operator == "D" and number == 1):
            queue.sort()
            queue.pop()
        elif (len(queue) > 0 and operator == "D" and number == -1):
            queue.sort(reverse=True)
            queue.pop()

    if (queue == []):
        answer.append(0)
        answer.append(0)
    else:
        queue.sort(reverse=True)
        answer.append(queue[0])
        answer.append(queue[len(queue) - 1])

    return answer