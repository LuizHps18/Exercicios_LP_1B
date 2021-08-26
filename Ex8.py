n = input("Digite algo: ")

print("É um número?", n.isnumeric())
print("É uma letra/palavra?", n.isalpha())
print("É algo vazio?", n.isspace())
print("É um alpha númerico?", n.isalnum())
print("Se for letra, está em maíusculo?", n.isupper())
print("Se for letra, está em minusculo?", n.islower())
print("Se for letra, está em modelo capitalizado?", n.istitle()) 