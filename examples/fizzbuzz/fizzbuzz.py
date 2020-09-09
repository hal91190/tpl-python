def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    return str(number)


if __name__ == '__main__':
    print("Kata FizzBuzz")
    for i in range(1, 101):
        print(fizzbuzz(i), end=', ')
    print()
