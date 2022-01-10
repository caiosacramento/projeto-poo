with open('base_de_dados.csv') as arquivo:
    tabela = csv.reader(arquivo, delimiter=';', lineterminator='\n')
    couteudo = list(tabela)
    print(couteudo)