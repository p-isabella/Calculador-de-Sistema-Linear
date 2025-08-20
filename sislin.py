import os
import time
varA = varB = varC = varD = varE = varF = varG = varH = varI = None
R1 = R2 = R3 = None

def resetar_variaveis():
    global varA, varB, varC, varD, varE, varF, varG, varH, varI
    global R1, R2, R3

    varA = varB = varC = varD = varE = varF = varG = varH = varI = None
    R1 = R2 = R3 = None

def exibeequacao2():
    variA, variB, variR1 = varA, varB, R1
    if not variA:
        variA = "A"
    if not variB:
        variB = "B"
    if not R1:
        variR1 = "R1"
    print(f"1° | {variA}x + {variB}y = {variR1}")

    variC, variD, variR2 = varC, varD, R2
    if not variC:
        variC = "C"
    if not variD:
        variD = "D"
    if not R2:
        variR2 = "R2"
    print(f"2° | {variC}x + {variD}y = {variR2}")


def exibeequacao3():
    variA, variB, variC, variR1 = varA, varB, varC, R1
    if not variA:
        variA = "A"
    if not variB:
        variB = "B"
    if not variC:
        variC = "C"
    if not R1:
        variR1 = "R1"
    print(f"1° | {variA}x + {variB}y +  {variC}z = {variR1}")

    variD, variE, variF, variR2 = varD, varE, varF, R2
    if not variD:
        variD = "D"
    if not variE:
        variE = "E"
    if not variF:
        variF = "F"
    if not R2:
        variR2 = "R2"
    print(f"2° | {variD}x + {variE}y + {variF}z = {variR2}")

    variG, variH, variI, variR3 = varG, varH, varI, R3
    if not variG:
        variG = "G"
    if not variH:
        variH = "H"
    if not variI:
        variI = "I"    
    if not R3:
        variR3 = "R3"
    print(f"3° | {variG}x + {variH}y + {variI}z = {variR3}")


def main():
    while True:
        resetar_variaveis()
        print("="*50)
        print("SISTEMAS LINEARES".center(50))
        print("="*50)

        while True:
            try:
                opcao = int(input("Insira com quantas incógnitas vamos trabalhar:\n[2] ou [3]\n>>"))
                if opcao < 2 or opcao > 3:
                    print("Opa! Não consigo trabalhar com esse número de incógnitas, tente novamente com duas ou três.")
                    print("="*50)
                    continue
                break
            except ValueError:
                print("Por favor, digite 2 ou 3.")
                continue

        while True:
            continuar = input(f"Você escolheu trabalhar com [{opcao}] incógnitas! Vamos continuar?\n[Sim] ou [Não]\n>>").lower()
            if continuar in ["sim", "s"]:
                print("="*50)
                break
            elif continuar in ["não", "n", "nao"]:
                print("-"*50)
                print("Poxa! Vamos voltar ao menu.")
                os.system('cls')
                break
            else:
                print("Opa, não entendi o seu comando... Vamos tentar novamente.")
        
        if continuar not in ["sim", "s"]:
            continue  

        if opcao == 2:
            duasincognitas()
        else:
            tresincognitas()

        print("="*50)
        time.sleep(1.2)

        while True:
            resp = input("Você deseja continuar a utilizar o programa?\n[Sim] ou [Não]\n>> ").lower()
            if resp in ["sim", "s"]:
                time.sleep(1.5)
                os.system("cls")
                break  
            elif resp in ["não", "n", "nao"]:
                print("Ok, obrigado por usar o programa! Saindo...")
                return
            else:
                print("Opa, não entendi o seu comando... Vamos tentar novamente.")

def duasincognitas():

    print("Beleza! Agora, vamos montar a primeira equação do nosso sistema linear [2].")
    global varA, varB, R1
    global varC, varD, R2

    matriz = [[0, 0, 0],
              [0, 0, 0]
              ]

    for i in range(1):
        for j in range(2):
            while True:
                try:
                    print("1° | Ax + By = R1")
                    varA = float(input("Insira o valor de A (acompanha o X):\n>>"))
                    matriz[0][0] = varA
                    exibeequacao2()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            
            while True:
                try:
                    varB = float(input("Insira o valor de B (acompanha o Y):\n>>"))
                    matriz[0][1] = varB
                    exibeequacao2()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue
                

            while True:
                try:
                    R1 = float(input("Insira o resultado da nossa equação:\n>>"))
                    matriz[0][2] = R1
                    exibeequacao2()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            
            print("-"*50)
            time.sleep(1.4)
            os.system('cls')
            print("Agora, vamos para a segunda equação...")
            while True:
                try:
                    print("2° | Cx + Dy = R2")
                    varC = float(input("Insira o valor de C (acompanha o X):\n>>"))
                    matriz[1][0] = varC
                    exibeequacao2()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    varD = float(input("Insira o valor de D (acompanha o Y):\n>>"))
                    matriz[1][1] = varD
                    exibeequacao2()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    R2 = float(input("Insira o resultado da nossa equação:\n>>"))
                    matriz[1][2] = R2
                    exibeequacao2()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            time.sleep(0.6)
            os.system('cls')
            print("A equação digitada foi:")
            exibeequacao2()
            print("Vamos calcular a determinante. Se determinante = 0, temos um SI, senão, teremos um SPD.")

            # cálculo da determinante:
            print("-"*50)
            print("A determinante é calculada a partir da regra de Sarrus:\n")
            time.sleep(1.0)
            print(f"| {matriz[0][0]}, {matriz[0][1]} |")
            print(f"| {matriz[1][0]}, {matriz[1][1]} |\n")
            print("-"*50)
            time.sleep(2.0)

            determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
            if determinante == 0:
                print(f"O resultado da determinante é igual a {determinante}")
                print("O sistema apresentado é [IMPOSSÍVEL]. Não há nenhuma solução possível.") 
                print("Voltando ao menu...")
            else:
                print(f"O resultado da determinante é igual a {determinante}")
                print("O sistema apresentado é [POSSÍVEL E DETERMINADO]. Vamos calcular as soluções.")
                print("-"*50)
                time.sleep(3)

                dx = matriz[0][2] * matriz[1][1] - matriz[0][1] * matriz[1][2]
                dy = matriz[0][0] * matriz[1][2] - matriz[0][2] * matriz[1][0]

                print("\nA matriz usada para calcular Dx:\n")
                print(f'''| {matriz[0][2]}, {matriz[0][1]} |\n| {matriz[1][1]}, {matriz[1][2]} |\n''')
                print(f"Dx = | {matriz[0][2]} * {matriz[1][1]} - {matriz[0][1]} * {matriz[1][2]}.\nO resultado de Dx = {dx}.\n")
                print("-"*50)
                time.sleep(4.0)
                print("\nA matriz usada para calcular Dy:\n")
                print(f'''| {matriz[0][0]}, {matriz[0][2]} |\n| {matriz[1][1]}, {matriz[1][2]} |\n''')
                print("Dy = | A * R2 - R1 * C")
                print(f"Dy = | {matriz[0][0]} * {matriz[1][2]} - {matriz[0][2]} * {matriz[1][0]}.\nO resultado de Dy = {dy}.\n")
                print("="*50)
                time.sleep(4.0)

                print("Agora, com os resultados de Dx e Dy, calculamos o X e Y:")
                
                x = dx/determinante
                y = dy/determinante

                print(f"X é calculado: Dx/D.\nX = {dx:.1f}/{determinante}")
                print(f"X é igual a: {x:.2f}")
                print("-"*50)
                time.sleep(2)
                print(f"Y é calculado: Dy/D.\nY = {dy:.1f}/{determinante}")
                print(f"Y é igual a: {y:.2f}")
                break
            break


def tresincognitas():
    print("Beleza! Agora, vamos montar a primeira equação do nosso sistema linear [3].")
    global varA, varB, varC, R1
    global varD, varE, varF, R2
    global varG, varH, varI, R3

    matriz = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]
              ]

    for i in range(1):
        for j in range(2):
            while True:
                try:
                    print("1° | Ax + By + Cz = R1")
                    varA = float(input("Insira o valor de A (acompanha o X):\n>>"))
                    matriz[0][0] = varA
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            
            while True:
                try:
                    varB = float(input("Insira o valor de B (acompanha o Y):\n>>"))
                    matriz[0][1] = varB
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    varC = float(input("Insira o valor de C (acompanha o Z):\n>>"))
                    matriz[0][2] = varC
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue
                
            while True:
                try:
                    R1 = float(input("Insira o resultado da nossa equação:\n>>"))
                    matriz[0][3] = R1
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            
            print("-"*50)
            print("Agora, vamos para a segunda equação...")
            time.sleep(1.4)
            os.system('cls')

            while True:
                try:
                    print("2° | Dx + Ey + Fz = R2")
                    varD = float(input("Insira o valor de D (acompanha o X):\n>>"))
                    matriz[1][0] = varD
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    varE = float(input("Insira o valor de E (acompanha o Y):\n>>"))
                    matriz[1][1] = varE
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    varF = float(input("Insira o valor de F (acompanha o Z):\n>>"))
                    matriz[1][2] = varF
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    R2 = float(input("Insira o resultado da nossa equação:\n>>"))
                    matriz[1][3] = R2
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            print("-"*50)
            print("Agora, vamos para a terceira equação...")
            time.sleep(1.4)
            os.system('cls')

            while True:
                try:
                    print("3° | Gx + Hy + Iz = R3")
                    varG = float(input("Insira o valor de G (acompanha o X):\n>>"))
                    matriz[2][0] = varG
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    varH = float(input("Insira o valor de H (acompanha o Y):\n>>"))
                    matriz[2][1] = varH
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    varI = float(input("Insira o valor de I (acompanha o Z):\n>>"))
                    matriz[2][2] = varI
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            while True:
                try:
                    R3 = float(input("Insira o resultado da nossa equação:\n>>"))
                    matriz[2][3] = R3
                    exibeequacao3()
                    break
                
                except ValueError:
                    print("Opa! Parece que você digitou errado, vamos tentar novamente.")
                    print("-"*50)
                    continue

            time.sleep(0.6)
            os.system('cls')
            print("A equação digitada foi:")
            exibeequacao3()

            # cálculo da determinante:

            print("-"*50)
            print("A determinante é calculada a partir da regra de Sarrus:\n")
            time.sleep(1.0)
            print(f"| {matriz[0][0]}, {matriz[0][1]}, {matriz[0][2]} |")
            print(f"| {matriz[1][0]}, {matriz[1][1]}, {matriz[1][2]} |")
            print(f"| {matriz[2][0]}, {matriz[2][1]}, {matriz[2][2]} |")
            print("-"*50)
            time.sleep(2.0)
            
            determinante = (matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[1][0] * matriz[2][1] * matriz[0][2] + matriz[0][1] * matriz[1][2] * matriz[2][0]) - (
                        matriz[0][2] * matriz[1][1] * matriz[2][0] + matriz[0][1] * matriz[1][0] * matriz[2][2] + matriz[1][2] * matriz[2][1] * matriz[0][0])
            
            if determinante == 0:
                print(f"O resultado da determinante é igual a {determinante}")
                print("O sistema apresentado é [IMPOSSÍVEL]. Não há nenhuma solução possível.") 
                print("Voltando ao menu...")
            else:
                print(f"O resultado da determinante é igual a {determinante}")
                print("O sistema apresentado é [POSSÍVEL E DETERMINADO]. Vamos calcular as soluções.")
                print("-"*50)
                time.sleep(3)   

                print("\n\n\n\nAgora que sabemos a determinante, calcularemos Dx, Dy e Dz.")
                print("-"*50)
                print("Cálculo de Dx: ")
                print("A matriz para calcular Dx será:") 
                print(f''' 
                | {matriz[0][3]:.0f}, {matriz[0][1]:.0f}, {matriz[0][2]:.0f} |
                | {matriz[1][3]:.0f}, {matriz[1][1]:.0f}, {matriz[1][2]:.0f} |
                | {matriz[2][3]:.0f}, {matriz[2][1]:.0f}, {matriz[2][2]:.0f} |
                
    Pois precisamos substituir a primeira coluna pelos termos independentes.
    Agora, faremos como se fossemos calcular uma determinante quaisquer com a regra de Sarrus.
                ''')

                dx = ((matriz[0][3] * matriz[1][1] * matriz[2][2]) + (matriz[1][3] * matriz[2][1] * matriz[0][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][3])) 
                dx = dx - ((matriz[0][2] * matriz[1][1] * matriz[2][3]) + (matriz[0][1] * matriz[1][3] * matriz[2][2]) + (matriz[1][2] * matriz[2][1] * matriz[0][3]))
                
                print(f"\nO resultado de Dx é: {dx}")
                print("-"*50)
                time.sleep(4.0)

                print("\n\nCálculo de Dy: ")
                print("A matriz para calcular Dy será:")
                print(f'''
                | {matriz[0][0]:.0f}, {matriz[0][3]:.0f}, {matriz[0][2]:.0f} |
                | {matriz[1][0]:.0f}, {matriz[1][3]:.0f}, {matriz[1][2]:.0f} |
                | {matriz[2][0]:.0f}, {matriz[2][3]:.0f}, {matriz[2][2]:.0f} |
                
    Pois precisamos substituir a segunda coluna pelos termos independentes.
    Agora, faremos como se fossemos calcular uma determinante quaisquer com a regra de Sarrus.
                ''')

                dy = ((matriz[0][0] * matriz[1][3] * matriz[2][2]) + (matriz[1][0] * matriz[2][3] * matriz[0][2]) + (matriz[0][3] * matriz[1][2] * matriz[2][0])) 
                dy = dy - ((matriz[0][2] * matriz[1][3] * matriz[2][0]) + (matriz[0][3] * matriz[1][0] * matriz[2][2]) + (matriz[1][2] * matriz[2][3] * matriz[0][0]))
                
                print(f"\nO resultado de Dy é: {dy}")
                print("-"*50)
                time.sleep(4.0)
                
                print("\n\nCálculo de Dz: ")
                print("A matriz para calcular Dz será:")
                print(f'''
                | {matriz[0][0]:.0f}, {matriz[0][1]:.0f}, {matriz[0][3]:.0f} |
                | {matriz[1][0]:.0f}, {matriz[1][1]:.0f}, {matriz[1][3]:.0f} |
                | {matriz[2][0]:.0f}, {matriz[2][1]:.0f}, {matriz[2][3]:.0f} |
                
    Pois precisamos substituir a terceiro coluna pelos termos independentes.
    Agora, faremos como se fossemos calcular uma determinante quaisquer com a regra de Sarrus.
                ''')

                dz = ((matriz[0][0] * matriz[1][1] * matriz[2][3]) + (matriz[1][0] * matriz[2][1] * matriz[0][3]) + (matriz[0][1] * matriz[1][3] * matriz[2][0])) 
                dz = dz - ((matriz[0][3] * matriz[1][1] * matriz[2][0]) + (matriz[0][1] * matriz[1][0] * matriz[2][3]) + (matriz[1][3] * matriz[2][1] * matriz[0][0]))
                
                print(f"\nO resultado de Dz é: {dz}")
                print("-"*50)
                time.sleep(4.0)

                print("\n\n\nAgora, vamos calcular os resultados:")

                x = dx/determinante
                y = dy/determinante
                z = dz/determinante

                print(f"\nX é calculado: Dx/D.\nX = {dx:.1f}/{determinante}")
                print(F"X é igual a: {x:.2f}")
                print("-"*50)
                print(f"\nY é calculado: Dy/D.\nY = {dy:.1f}/{determinante}")
                print(f"Y é igual a: {y:.2f}")
                print("-"*50)
                print(f"\nZ é calculado: Dz/D.\nZ = {dz:.1f}/{determinante}")
                print(f"Z é igual a: {z:.2f}")            
                break
            break

'''
00 01 02 03
10 11 12 13
20 21 22 23
'''

main()
