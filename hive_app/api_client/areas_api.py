def buscar_areas_danificadas():
    # Simulando resposta da API como lista de dicionários
    return [
        {"id": 1, "descricao": "Foco de incêndio detectado", "latitude": -15.7801, "longitude": -47.9292,
         "nivel_confiabilidade": 0.85, "area_hectares": 120},
        {"id": 2, "descricao": "Desmatamento recente", "latitude": -16.7769, "longitude": -48.0103,
         "nivel_confiabilidade": 0.90, "area_hectares": 250}
    ]