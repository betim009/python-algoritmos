# Exercícios de Fixação
# Exercício 1: Qual é a Ordem de Complexidade (complexidade de tempo)
# do algoritmo abaixo? E a complexidade de espaço?

def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result


# Solução:

# Complexidade de Tempo: O(n)

# Complexidade de Espaço: O(1)
