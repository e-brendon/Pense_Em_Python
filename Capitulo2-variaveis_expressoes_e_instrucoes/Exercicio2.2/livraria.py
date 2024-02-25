'''
Suponha que o preço da capa de um livro seja R$ 24,95, mas as livrarias
recebem um desconto de 40%. O transporte custa 3,00 para o primeiro exemplar
e 75 centavos para cada exemplar adicional. Qual o custo total de atacado para
60 cópias ? 
'''
valor_livro = 24.95
desconto    = 0.4
transporte_1= 3
transporte_v= 0.75
quant_cop   = 60
#
valor_frete = ((quant_cop-1)*transporte_v)+transporte_1 # definindo valor frete
#
valor_desconto = valor_livro*desconto
valor_pos_desconto = valor_livro - valor_desconto
valor_tot_livros = valor_pos_desconto * quant_cop

#definindo valor total de atacado
total_atacado = valor_tot_livros + valor_frete
print(f"O valor de todos os: {quant_cop} livros é um total de: \n{round(total_atacado, 2)}, sendo gastos: \n{round (valor_frete, 2)} gastos em frete \n{round(valor_tot_livros, 2)} nas capas de livros")
