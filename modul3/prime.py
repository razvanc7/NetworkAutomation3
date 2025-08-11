# function for first 100 prime numbers

def prime():
    prime_counter = 0
    nrs = 3
    result_in_function = [1, 2]

    while (prime_counter <= 100):
        for i in range(2, nrs // 2 + 1):
            if not nrs % i:
                break
        else:
            prime_counter += 1
            result_in_function.append(nrs)
        nrs += 1

    return result_in_function

if __name__ == '__main__':
    result = prime()
    print(result)
