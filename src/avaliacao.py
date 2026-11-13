def registar_experiencia(tabela, **dados):
    # id, familia, hiperparametros, atributos, preparacao, semente,
    # limiar, metricas e avisos
    pass


def comparar_limiares(modelo, X_val, y_val, limiares):
    # probabilidade da classe 1 (confirmar com classes_)
    # aplicar os cinco limiares sem voltar a treinar
    pass


def escolher_solucao(resultados):
    # par configuracao e limiar com menor custo medio na validacao
    # desempates pela ordem do enunciado
    pass


def escolher_erros(y_real, y_prev, ids, n=3):
    # n falsos positivos e n falsos negativos da validacao
    pass
