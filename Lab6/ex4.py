matriz = []
for i in range(3):
    matriz.append(input().split())
print(f"Matriz = [")
print(f"        {matriz[0]},")
print(f"        {matriz[1]},")
print(f"        {matriz[2]},")
print(f"        ]")

ganhador = ''
for j in range(3):
    if matriz[j][0] == matriz[j][1] and matriz[j][1] == matriz[j][2]:
        ganhador = matriz[j][0]
    elif matriz[0][j] == matriz[1][j] and matriz[1][j] == matriz[2][j]:
        ganhador = matriz[0][j]

if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] or matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]:
    ganhador = matriz[1][1]

if ganhador == '':
    print('"Empate"')
else:
    print(f'"{ganhador}" é o vencedor')
    
