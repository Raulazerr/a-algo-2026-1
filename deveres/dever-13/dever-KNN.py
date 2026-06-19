from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def executar_atividade_knn():
    # 1. Carregar o dataset
    dados = load_breast_cancer()
    X = dados.data
    y = dados.target

    # 2. Separar treino e teste (80% treino, 20% teste)
    # random_state=42 garante que a divisão seja sempre a mesma para podermos comparar
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    # 3. Normalizar os dados (Dica: usando StandardScaler)
    scaler = StandardScaler()
    X_train_norm = scaler.fit_transform(X_train)
    X_test_norm = scaler.transform(X_test)

    # 4 e 5. Configurar os valores de K e as métricas a serem testadas
    valores_k = [1, 3, 5]
    metricas = ['euclidean', 'manhattan']

    print("=== RESULTADOS DA CLASSIFICAÇÃO K-NN ===")
    print(f"{'K':<5} | {'Métrica':<12} | {'Acurácia':<10}")
    print("-" * 35)

    melhor_acuracia = 0
    melhor_modelo = ""

    # 6. Treinar, testar e comparar acurácia entre as combinações
    for k in valores_k:
        for metrica in metricas:
            # Inicializa o modelo
            knn = KNeighborsClassifier(n_neighbors=k, metric=metrica)
            
            # Treina o modelo com os dados normalizados
            knn.fit(X_train_norm, y_train)
            
            # Faz as previsões no conjunto de teste
            previsoes = knn.predict(X_test_norm)
            
            # Calcula a acurácia
            acuracia = accuracy_score(y_test, previsoes)
            
            print(f"{k:<5} | {metrica:<12} | {acuracia:.4f}")

            # Registra o melhor modelo para discussão
            if acuracia > melhor_acuracia:
                melhor_acuracia = acuracia
                melhor_modelo = f"K={k} com distância {metrica}"

    print("-" * 35)
    print(f"Melhor desempenho geral: {melhor_modelo} (Acurácia: {melhor_acuracia:.4f})")

# Executa o script
executar_atividade_knn()
