
def main ():
    dados1 = [ ]
    for i in range(3):
        while True:
            print(f"\Dados {i+1}")
            avaliador = input("Digite seu nome: ")
            nomef = input("Digite o nome do filme: ")
            nota1 = int(input("Digite sua nota para o filme entre 0 e 10: "))
            if nota.isdigit():
                nota = int(nota1)
                if 0 <= nota <= 10:
                    break
                else:
                    print("Nota invalida, tente novamente...")
            dados1.append([avaliador, nomef, nota])
            print("\n---Dados dos Avaliadores---")
            for dados1 in nota:
                print(f"NOME: {avaliador[0]} | NOME DO FILME:{nomef[1]:.2f} | NOTA:{nota[2]:.2f}")
if __name__=="__main__":
   main()

        
        










