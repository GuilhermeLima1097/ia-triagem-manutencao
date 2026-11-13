from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from src import config


def aplicar_limiar(probabilidades, limiar):
    # urgente quando a probabilidade e >= limiar
    pass


def custo_medio(y_real, y_prev):
    # (CUSTO_FN * FN + CUSTO_FP * FP) / total de pedidos
    pass


def taxa_sinalizacao(y_prev):
    # pedidos previstos como urgentes / total de pedidos
    pass


def todas_as_metricas(y_real, y_prev):
    # matriz de confusao com labels [0, 1], accuracy, precision, recall, f1
    # (zero_division=0), taxa de sinalizacao e custo medio
    pass
