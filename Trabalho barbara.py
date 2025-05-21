def main():
    avaliação = []

    for i in range(3):
        while True:
            print(f"\nAvaliação {i + 1}")
            avaliador = input("Digite seu nome: ")
            nomef = input("Digite o nome do filme: ")
            nota1 = input("Digite sua nota para o filme entre 0 e 10: ")
            try:
                nota = float(nota1)
                if 0 <= nota <= 10 :
                    avaliação.append([avaliador, nomef, nota])
                    break
                else:
                    print("Nota inválida, tente novamente...")
            except ValueError:
                print("Nota inválida, tente novamente...")

    print("\n--- Dados dos Avaliadores ---")
    for dado in avaliação:
        print(f"NOME: {dado[0]} | NOME DO FILME: {dado[1]} | NOTA: {dado[2]:.2f}")

if __name__=="__main__":
   main()
        
        










