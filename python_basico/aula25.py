"""
CONSTANTE - variáveis que não vão mudar ao longo do código, são escritas em letras maiúsculas
Muitas condições no mesmo if - Ruim
    <- Contagem de complexidade - Ruim
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  #local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local do radar 1
RANGE = 1  #  distância em que o radar pega

carro_passou_radar_1 = local_carro == LOCAL_1
carro_acima_velocidade = velocidade > RADAR_1
carro_multado = carro_acima_velocidade and (LOCAL_1 - RANGE <= local_carro <= LOCAL_1 + RANGE)

if carro_passou_radar_1:
    print('Carro passou no radar')

if carro_multado:
    print('Você foi multado')

if not carro_multado:
    print('Você não foi multado')
