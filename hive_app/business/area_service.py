from database.repository import inserir_area, buscar_bases
from utils.geo_utils import distancia_aproximada
import math

def cadastrar_areas(areas):
    for area in areas:
        inserir_area(area)

def calcular_distancias_bases(area, bases):
    distancias = []
    
    for base in bases:
        dist = distancia_aproximada(area.latitude, area.longitude, base.latitude, base.longitude)
        distancias.append((base, dist))
    
    # Ordena as bases pela distância
    distancias.sort(key=lambda x: x[1]) 
    
    return distancias

# Função de busca binária para a base mais próxima
def busca_binaria_bases(distancias, alvo_distancia):
    # Busca binária em uma lista ordenada de distâncias
    esquerda = 0
    direita = len(distancias) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        base_atual, dist_atual = distancias[meio]
        
        if dist_atual == alvo_distancia:
            return base_atual, dist_atual  # Retorna a base e a distância encontrada
        elif dist_atual < alvo_distancia:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    # Aqui retornamos o item da tupla (base, distância)
    return distancias[esquerda][0], distancias[esquerda][1]

def encontrar_base_mais_proxima(area):
    bases = buscar_bases()  # Lista de bases
    distancias = calcular_distancias_bases(area, bases)  # Ordena as bases pelas distâncias
    
    # Aplica a busca binária para encontrar a base mais próxima
    base_mais_proxima, distancia = busca_binaria_bases(distancias, distancias[0][1])
    
    return base_mais_proxima, distancia

def calcular_drones_necessarios(area_hectares, capacidade_por_drone):
    return math.ceil(area_hectares / capacidade_por_drone)