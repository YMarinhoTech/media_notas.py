import time

print("Vamos calcular sua média!\nPara remover uma avaliação digite (0)")
time.sleep(2.5)

while True:
    a = float(input("Sendo objetivo, quanto você tirou na AV1? "))
    b = float(input("Sendo objetivo, quanto você tirou na AV2? "))
    c = float(input("Sendo objetivo, quanto você tirou na TB1? "))
    d = float(input("Sendo objetivo, quanto você tirou na TB2? "))
    print()

    notas = [a, b, c, d]

    if a == 0:
        notas.remove(a)

    if b == 0:
        notas.remove(b)

    if c == 0:
        notas.remove(c)

    if d == 0:
        notas.remove(d)

    elif any(n < 1 or n > 10 for n in notas):
        print("Trabalhamos apenas com notas de 1 a 10!")
        continue  # volta ao início do while

    media = a + b + c + d
    media_final = media / len(notas)

    print('Suas notas são:', notas)

    confirmacao = int(input("\n1 - caso esteja correto\n0 - caso esteja errado errado\nR. "))
    print()
     
    if confirmacao == 1:
        print("Ok, calculando média...\n")
        time.sleep(1)
        print('Você tirou', round(media_final, 2))
        print("Quer ver se foi aprovado ou reprovado?")
        quer = int(input("\n1 - ver aprovação\n0 - ignorar resultado final\nR. "))
        print()
        if quer == 1 and media_final >= 7:
            print("Você foi aprovado, Parabens!\n")
            continuar = int(input("1 - continuar\n0 - encerrar codigo\nR. "))
            print()
            if continuar == 1:
                continue
            elif continuar ==0:
                break
            else:
                ("as opções eram apenas 1 ou 0")
        elif quer == 1 and media_final <= 6:
            print("Infelizmente você foi reprovado\n")
            continue
        elif quer == 0:
            print("Então vamos encerrar o codigo por aqui")
            break

    else:
        print("Digite apenas 1 se está correto ou 0 se está incorreto!")
        continue
