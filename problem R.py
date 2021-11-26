def primes():
    number = 2
    while True:
        flag = False
        for i in range(1, (number // 2) + 1):
            if number % i == 0 and i != 1:
                flag = True
            if flag:
                break
        if not flag:
            number += 1
            yield number - 1
        else:
            number += 1
