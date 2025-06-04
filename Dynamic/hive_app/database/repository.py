from .models import Base

#Simulação do banco

#Tabela de areas
areas_db = {}

#Tabela de bases
bases_db = {
    1: Base(1, "Base Central", -15.7795, -47.9293, 50, "basecentral@hive.com"),
    2: Base(2, "Base Regional", -16.5, -48.0, 40, "baseregional@hive.com")
}

#Função para alimentar o banco de dados
def inserir_area(area):
    areas_db[area.id] = area
    print(f"Área {area.id} inserida no banco.")

#Função para fazer uma requisição no banco
def buscar_bases():
    return list(bases_db.values())