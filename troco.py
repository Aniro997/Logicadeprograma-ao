
notas_e_moedas = [200, 100, 50, 20, 10, 5, 2, 1, 0,50, 0,25, 0.10, 0,5, 0,1]

valor_a_receber = float(input('Qual o valor a receber ?'))

valor_recebido = float(input ('Qual o valor recebido ?'))

diferenca = valor_recebido - valor_a_receber


for valor in notas_e_moedas:
    quantidade = 0
    while valor  <= diferenca:
        quantidade += 1
        diferenca -= valor
        if quantidade > 0:
            print ('para {quantidade}itens de {valor}')
