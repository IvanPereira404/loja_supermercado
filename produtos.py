import json
from datetime import datetime

FICHEIRO = "produtos.json"

def carregar_dados():
    with open(FICHEIRO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

