'''
Se você correr 10 quilometros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milhas em minutos e 
segundos?) Qual sua velocidade média em milhas por hora
'''
# Definindo as variáveis
distancia_milhas = 10000 / 1610  # Conversão de metros para milhas
tempo_segundos = (42 * 60) + 42  # Conversão de minutos e segundos para segundos

# Cálculo da velocidade em metros por segundo
velocidade_m_s = distancia_milhas / tempo_segundos

# Conversão de metros por segundo para milhas por hora
velocidade_mph = velocidade_m_s * 2.23693629  # 1 m/s = 2.23693629 mph

# Cálculo do ritmo em minutos e segundos por milha
ritmo_min_seg_milha = (60 / velocidade_mph) * 60

# Impressão dos resultados
print(f"Em 42 minutos e 42 segundos a pessoa vai correr:")
print(f" - {round(velocidade_mph, 2)} milhas por hora")
print(f" - {ritmo_min_seg_milha} minutos e segundos por milha")
