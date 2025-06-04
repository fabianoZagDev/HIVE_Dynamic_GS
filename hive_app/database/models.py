class Area:
    def __init__(self, id, descricao, latitude, longitude, nivel_confiabilidade, area_hectares):
        self.id = id
        self.descricao = descricao
        self.latitude = latitude
        self.longitude = longitude
        self.nivel_confiabilidade = nivel_confiabilidade
        self.area_hectares = area_hectares

class Base:
    def __init__(self, id, nome, latitude, longitude, capacidade_drone_hectares, email_contato):
        self.id = id
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.capacidade_drone_hectares = capacidade_drone_hectares
        self.email_contato = email_contato