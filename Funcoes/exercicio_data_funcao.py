
##Exercicio2
def data(data):
    meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho'
        , 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    data_cortada = data.split("/")
    mes_extenso = int(data_cortada[1])
    mes = meses.get(mes_extenso)
    data_extenso = data_cortada[0] + ' de ' + mes + ' de ' + data_cortada[2]
    print(data_extenso)


data(input('Digite uma data no valor xx/x/xxxx'))

