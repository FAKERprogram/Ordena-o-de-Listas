# Construindo uma matriz com lista

Matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        Matriz[l][c]=int(input(f'Digite um numero para [{l}:{c}] :'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{Matriz[l][c]:^5}]', end="")
    print()
    
