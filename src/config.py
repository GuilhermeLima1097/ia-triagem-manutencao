from pathlib import Path

PASTA_DADOS = Path("dados")
FICHEIRO_TREINO = PASTA_DADOS / "treino.csv"
FICHEIRO_VALIDACAO = PASTA_DADOS / "validacao.csv"
FICHEIRO_TESTE = PASTA_DADOS / "teste.csv"

ID = "id_pedido"
ALVO = "urgente"

# os dez atributos preditivos (entre equipamento e periodo)
ATRIBUTOS = [
    "equipamento",
    "contexto",
    "utilizadores_afetados",
    "interrupcao_total",
    "alternativa_disponivel",
    "horas_desde_deteccao",
    "reincidencias_30d",
    "idade_anos",
    "sinal_seguranca",
    "periodo",
]

# preencher depois da auditoria
NUMERICAS = []
CATEGORICAS = []

LIMIARES = [0.20, 0.35, 0.50, 0.65, 0.80]
CUSTO_FN = 4
CUSTO_FP = 1

# fixar antes das experiencias e nao mudar
SEMENTE = None
