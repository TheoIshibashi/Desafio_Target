def count_a(input_string):
    count = input_string.lower().count('a')
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Definindo a string a ser verificada
input_string = input("Informe uma string: ")
count_a(input_string)
