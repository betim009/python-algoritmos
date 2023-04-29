# Complexidade quadrática

# def multiply_arrays(array1, array2):
#     result = []
#     number_of_iterations = 0

#     for number1 in array1:
#         print(f'Array 1: {number1}')
#         for number2 in array2:
#             print(f'Array 2: {number2}')
#             result.append(number1 * number2)
#             number_of_iterations += 1

#     print(f'{number_of_iterations} iterações!')
#     return result


# n = 1000  # onde n será o número total de elementos dentro do array
# meu_array = list(range(1, n))

# multiply_arrays(meu_array, meu_array)
# Tempo de execução: time python3 meu_programa.py

# 0(n²) = 999 * 999 = 998001


# Exercício 3
# Faça um algoritmo qualquer com três loops aninhados um dentro do outro.
# Entenda como ele terá uma complexidade de O(n³)!

# Solução

# Podemos alterar o algoritmo do exercício anterior pra isso:

def multiply_arrays(array1, array2, array3):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        for number2 in array2:
            for number3 in array3:
                result.append(number1 * number2 * number3)
                number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


# Usar arrays de tamanho 1000 aqui pode ser muito lento!
meu_array = list(range(1, 100))
multiply_arrays(meu_array, meu_array, meu_array)
