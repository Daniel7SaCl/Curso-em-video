def main():
    pesos = []

    for i in range(5):
        peso = float(input(f"Digite o peso da pessoa {i+1} em kg: "))
        pesos.append(peso)

    maior_peso = max(pesos)
    menor_peso = min(pesos)

    print(f"\nMaior peso lido: {maior_peso} kg")
    print(f"Menor peso lido: {menor_peso} kg")

if __name__ == "__main__":
    main()
