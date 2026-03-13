# exercicio 1
def calc_salary(curr_salary):
    percentual = 0
    if curr_salary <= 280:
        percentual = 20
        new_salary = curr_salary + (curr_salary * 0.2)
    elif curr_salary > 280 and curr_salary <= 700:
        percentual = 15
        new_salary = curr_salary + (curr_salary * 0.15)
    elif curr_salary > 700 and curr_salary <= 1500:
        percentual = 10
        new_salary = curr_salary + (curr_salary * 0.1)
    else:
        percentual = 5
        new_salary = curr_salary + (curr_salary * 0.05)
    print(f"Salário antes do reajuste: R${curr_salary}\nPercentual de aumento aplicado: {percentual}%\nValor do aumento: R${new_salary - curr_salary}\nNovo salário após o aumento: R${new_salary}")
    return new_salary

# exercicio 2
def calc_fatorial(num):
    if num < 0:
        print("Número deve ser positivo.")
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        i = num - 1
        result = num
        while i > 1:
            result *= i
            i -= 1
        print(f"O fatorial de {num} é: {result}")    
        return result

#exercicio 3
def calc_consecutive_odds(m):
    for i in range(1, m + 1):
        sequence = []
        even = i ** 2 - i
        odd = even + 1
        for j in range(odd, odd + i * 2, 2):  # gera i ímpares consecutivos
            sequence.append(j)
        print(f"{i}³ = {i**3} → {sequence}")