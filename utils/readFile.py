from yaml import load, FullLoader
from os import path
from collections import ChainMap

def loadAndParse(filename: str):
    
    # verifica se arquivo existe
    assert path.isfile(filename), "Arquivo não encontrado"

    # lendo conteudo do arquivo
    with open(filename) as f:
        preprocessed = load(f, Loader=FullLoader)
    
    
    # lendo a 5-upla de entrada
    m = preprocessed["M"]

    parsed_delta = dict()
    delta_pre = dict(ChainMap(*m["Delta"]))
    for key in delta_pre:
        # convertendo chave em tupla
        parsed_delta[tuple(i.strip() for i in key.split(","))] = set(delta_pre[key]) if isinstance(delta_pre[key], list) else delta_pre[key]

    return {
        "M": {
            "q": set(str(i) for i in m["Q"]),
            "sigma": set(str(i) for i in m["Sigma"]),
            "delta": parsed_delta,
            "q0": m["q0"],
            "f": set(str(i) for i in m["F"])
        },

        "type": preprocessed["type"]
    }