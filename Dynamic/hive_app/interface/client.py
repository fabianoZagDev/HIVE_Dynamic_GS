from api_client.areas_api import buscar_areas_danificadas
from database.models import Area
from business.area_service import cadastrar_areas, encontrar_base_mais_proxima, calcular_drones_necessarios
from notifications.alert import enviar_alerta

def converter_areas_dict_para_objetos(lista_dicts):
    return [Area(**area_dict) for area_dict in lista_dicts]

def executar_fluxo():
    areas_dict = buscar_areas_danificadas()
    areas_obj = converter_areas_dict_para_objetos(areas_dict)
    
    cadastrar_areas(areas_obj)
    
    for area in areas_obj:
        base, dist = encontrar_base_mais_proxima(area)
        drones = calcular_drones_necessarios(area.area_hectares, base.capacidade_drone_hectares)
        enviar_alerta(base, area, drones, dist)