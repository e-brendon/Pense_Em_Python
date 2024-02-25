'''
Se eu sair de casa as 6:52 e correr 1 Km a um certo passo
(8min 15s por KM), então 3 Km a um passo mais rápido
(7min 12s) e 1 km no mesmo passo usado em primeiro lugar,
que horas chego em casa para o café da manhã?
'''
tempo_primeiro_KM   = (60*8)+15         # transformando os minutos em segundos 
tempo_segundo_KM    = ((60*7)+12)*3     # aqui eu pego e transformo os 3km em segundos também
tempo_quint_KM      = tempo_primeiro_KM # como os tempos são igual não precisa recalcular
#
tempo_total_Em_Seg  = tempo_primeiro_KM + tempo_segundo_KM + tempo_quint_KM
tempo_2_minutos     = tempo_total_Em_Seg/60
#

hora_saida  = 6
minuto_saida= 52

resto = (minuto_saida+tempo_2_minutos) - 60
hora_chega = hora_saida + 1
minutos_chego = resto
print(f"Chegou para o café as {hora_chega}h e {round(minutos_chego)}min para o café")
