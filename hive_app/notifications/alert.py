from datetime import datetime

def enviar_alerta(base, area, drones_necessarios, distancia):
    print("\n--- ALERTA ENVIADO ---")
    print(f"Base: {base.nome}")
    print(f"Email: {base.email_contato}")
    print(f"Área ID: {area.id}")
    print(f"Descrição: {area.descricao}")
    print(f"Nível de Confiabilidade: {area.nivel_confiabilidade}")
    print(f"Área (hectares): {area.area_hectares}")
    print(f"Drones necessários: {drones_necessarios}")
    print(f"Distância: {round(distancia, 2)} km")
    print(f"Data do alerta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("---------------------\n")