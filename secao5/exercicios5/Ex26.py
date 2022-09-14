"""
while True:
    print('=' * 50, 'CALCULE O CONSUMO DO VEÍCULO', '=' *50)
    quilometros = float(input('Informe quantos quilômetros foram percorridos:'))
    litros = float(input('Informe quantos litros foram consumido no percurso:'))
    kml = quilometros / litros
    print(f'O consumo foi igual a {kml:.2f} quilômetros por litro!')
    if kml < 8:
        print('Venda o carro!')
    elif kml >= 8 or kml > 14:
        print('Carro econômico!')
    elif kml >= 14:
        print('Carro super econômico!')
"""
while True:
    km = float(input('Insira a distância percorrida em km:'))
    litros = float(input('Insira a quantidade de gasoline usada em litros:'))
    consumo = km / litros
    if consumo < 8:
        print(f'Consumo {consumo:.2f} km/l  - Venda o carro!')
    elif consumo >= 8 and consumo <= 12:
        print(f'Consumo {consumo:.2f} km/l - Econômico!')
    elif consumo > 12:
        print(f'Consumo {consumo:.2f} km/l - Super Econômico!')
    else:
        print('Favor inserir números válidos!')
        break
