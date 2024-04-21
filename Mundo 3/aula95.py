def area(largura, comprimento):

     return largura * comprimento

largura_terreno = float(input("Digite a largura do terreno em metros: "))
comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))

area_terreno = area(largura_terreno, comprimento_terreno)
print("A área do terreno é:", area_terreno, "metros quadrados.")
