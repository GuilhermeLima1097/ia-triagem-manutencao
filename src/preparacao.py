from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def criar_preparacao(numericas, categoricas, com_escala=False):
    # numericas: imputacao; escala so para o MLP
    # categoricas: imputacao e codificacao
    # decidir o que fazer com categorias que nao aparecem no treino
    pass


def criar_pipeline(preparacao, modelo):
    # preparacao + classificador num so objeto
    pass
