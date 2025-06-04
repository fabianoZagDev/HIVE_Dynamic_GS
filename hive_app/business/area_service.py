from database.repository import inserir_area, buscar_bases
from utils.geo_utils import distancia_aproximada
import math

def cadastrar_areas(areas):
    for area in areas:
        inserir_area(area)

def encontrar_base_mais_proxima(area):
    bases = buscar_bases()
    base_mais_proxima = None
    menor_dist = float('inf')
    for base in bases:
        dist = distancia_aproximada(area.latitude, area.longitude, base.latitude, base.longitude)
        if dist < menor_dist:
            menor_dist = dist
            base_mais_proxima = base
    return base_mais_proxima, menor_dist

def calcular_drones_necessarios(area_hectares, capacidade_por_drone):
    return math.ceil(area_hectares / capacidade_por_drone)