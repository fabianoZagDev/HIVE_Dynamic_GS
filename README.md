# Projeto HIVE: Reflorestamento e Prevenção de Queimadas

## Objetivo do Projeto

A aplicação tem como objetivo desenvolver uma solução para o **reflorestamento de áreas danificadas** por queimadas, utilizando **drones autônomos** que semeiam sementes nas áreas devastadas. A aplicação recebe dados sobre áreas danificadas, processa essas informações e envia relatórios com cálculos para as **bases operacionais**.

---

## Estrutura do Projeto

Este repositório contém a implementação de uma aplicação em Python que interage com uma API simulada para obter áreas danificadas, processa essas informações e gera relatórios sobre o que precisa ser feito. A arquitetura está organizada em módulos para facilitar o entendimento e a manutenção do código.

A estrutura de pastas do projeto é a seguinte:
hive_app/

├── api_client/

│ ├── areas_api.py # Requisição para API de áreas danificadas (Simulada)

├── database/

│ ├── models.py # Definição de modelos (Area, Base)

│ └── repository.py # Funções de acesso ao "banco" (simulado)

├── business/

│ ├── area_service.py # Lógica de negócio para áreas

│ └── base_service.py # Lógica de negócio para bases

├── notifications/

│ └── alert_service.py # Envio de alertas sobre áreas danificadas

├── interface/

│ └── cli.py # Interação com o usuário via linha de comando

├── utils/

│ └── geo_utils.py # Funções utilitárias para cálculos geográficos

├── main.py # Ponto de entrada para rodar o 

---

## **Requisitos da Aplicação**

### 1. **Requisição para API de Áreas Danificadas**

A aplicação precisa **capturar as áreas danificadas** para iniciar o processo de reflorestamento. Isso é feito pela função `buscar_areas_danificadas()` que simula uma requisição para uma API externa. Os dados recebidos são então usados para armazenar as áreas no banco de dados.

- **Link para o código:** [api_client/areas_api.py](./hive_app/api_client/areas_api.py)

---

### 2. **Armazenamento das Áreas no Banco de Dados**

Após receber os dados das áreas, elas são armazenadas no "banco de dados" (usando um dicionário para simular a persistência). A função `inserir_area()` é responsável por isso.

- **Link para o código:** [database/repository.py](./hive_app/database/repository.py)

---

### 3. **Encontrar a Base Mais Próxima da Área**

A lógica de encontrar a **base mais próxima** de uma área danificada é baseada no cálculo de distâncias entre coordenadas geográficas utilizando a fórmula **Haversine**. A função `encontrar_base_mais_proxima()` calcula a base mais próxima para cada área utilizando **busca binária** para otimizar a busca.

- **Link para o código:** [business/area_service.py](./hive_app/business/area_service.py)

---

### 4. **Cálculo da Quantidade de Drones Necessários**

A quantidade de drones necessários para cobrir uma área danificada é calculada com base na área total e na **capacidade de cobertura** de cada drone. A função `calcular_drones_necessarios()` realiza esse cálculo.

- **Link para o código:** [business/area_service.py](./hive_app/business/area_service.py)

---

### 5. **Envio de Alertas para a Base**

Depois de calcular a quantidade de drones necessários, um **alerta** é enviado para a base mais próxima, com informações sobre a área danificada e a quantidade de drones que será necessária. O alerta é enviado pela função `enviar_alerta()`.

- **Link para o código:** [notifications/alert_service.py](./hive_app/notifications/alert_service.py)

---

## **Conceitos Utilizados**

### **Conjunto 1: Estruturas de Dados**

#### **Árvore, Listas e Algoritmos de Busca**

O conceito de **Árvore** foi aplicado ao mapeamento das **áreas** e **bases**, considerando cada base como um **nó** e as distâncias entre elas como as **arestas**. Embora não tenha utilizado diretamente estruturas como pilha ou fila, o conceito de **listas** foi amplamente usado para armazenar e processar as áreas e bases.

- **Link para o código:** [business/area_service.py](./hive_app/business/area_service.py)

#### **Notação O Grande**

A complexidade da busca pela **base mais próxima** agora é **O(log N)**, graças à **busca binária**. A ordenação das distâncias tem complexidade **O(N log N)** e a busca binária otimiza a busca para **O(log N)**, o que é eficiente quando lidamos com um grande número de bases.

- **Link para o código:** [utils/geo_utils.py](./hive_app/utils/geo_utils.py)

---

### **Conjunto 3: Análise de Algoritmos**

#### **Busca Binária**

Estamos utilizando **busca binária** para encontrar a **base mais próxima** de uma área. Isso é possível porque **ordenamos as distâncias das bases** antes de realizar a busca binária, o que reduz a complexidade de **O(N)** para **O(log N)**.

#### **Dicionários**


Utilizamos **dicionários** para simular o banco de dados e a API e também usamos para armazenar as áreas e bases, permitindo buscas rápidas com base no ID, o que torna o código eficiente.

- **Link para o código:** [database/repository.py](./hive_app/database/repository.py)

---

### **Conjunto 4: Modelagens com Grafos**

Embora o projeto não tenha usado grafos complexos, podemos visualizar as **bases** e **áreas danificadas** como um grafo, onde as bases são **nós** e as **arestas** são as distâncias entre elas. Isso é um conceito que poderia ser melhor explorado se precisássemos otimizar a escolha das bases.

- **Link para o código:** [business/area_service.py](./hive_app/business/area_service.py)
<<<<<<< HEAD
=======

---
>>>>>>> 5f6fa8efd95e7b30ec192592d9fe964dc545d3a7
