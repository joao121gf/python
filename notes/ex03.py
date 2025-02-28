


def sum(value1, value2):
    return value1 + value2




while True:
    num1 = int(input('Typer First Number: '))
    num2 = int(input('Typer Second Number: '))
    result = sum(num1, num2)
    print(result)
    awnser = (input('Do you want finish? S/N: ')).upper()
    if awnser == 'S':
        break
    