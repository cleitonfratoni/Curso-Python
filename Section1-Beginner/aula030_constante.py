"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60 # velociadde atual do carro
local_carro = 100 # local quem que o carro está na estrada

RADAR_1 = 60 # local onde o radar 
LOCAL_1 = 100 # velociade onde o radar 1 está
RADAR_RANGE = 1 # A dsitância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1


if vel_carro_pass_radar_1:
    print('Velociadde carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')