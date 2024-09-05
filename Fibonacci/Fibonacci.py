def fibonacci_sequence(limit):
    sequence = [0, 1]

    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def check_fibonacci(number):
    sequence = fibonacci_sequence(number)

    if number in sequence:
        print(f"{number} Pertence à sequência de Fibonacci.")
    else:
        print(f"{number} Não pertence à sequência de Fibonacci.")


number = int(input("Informe um número: "))
check_fibonacci(number)
