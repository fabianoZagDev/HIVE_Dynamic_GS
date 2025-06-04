#Calculadara que trás a distância entre dois pontos de coordenada

def distancia_euclidiana(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def graus_para_radianos(graus):
    pi = 3.141592653589793
    return graus * (pi / 180)

def cos_aprox(x):
    x2 = x * x
    return 1 - x2/2 + (x2*x2)/24 - (x2*x2*x2)/720

def distancia_aproximada(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = graus_para_radianos(lat2 - lat1)
    dlon = graus_para_radianos(lon2 - lon1)
    lat1_rad = graus_para_radianos(lat1)
    lat2_rad = graus_para_radianos(lat2)
    x = dlon * (R * cos_aprox((lat1_rad + lat2_rad) / 2))
    y = dlat * R
    return (x**2 + y**2)**0.5