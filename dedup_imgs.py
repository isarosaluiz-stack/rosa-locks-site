# -*- coding: utf-8 -*-
# Limpa fotos duplicadas em assets/img.
# NAO apaga nada: move as copias repetidas para assets/img/_duplicados
# e renumera as fotos que ficam para 01, 02, 03... contiguo.
# Roda na pasta do projeto (mesmo lugar do build.py).

import os, re, hashlib, sys

IMG = os.path.join("assets", "img")
LIXO = os.path.join(IMG, "_duplicados")

if not os.path.isdir(IMG):
    print("Nao achei a pasta assets/img. Rode este script dentro da pasta do projeto.")
    sys.exit(1)

def md5(caminho):
    with open(caminho, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# agrupa por prefixo antes do -N.jpg  (tigre-01 -> tigre ; tigre-planta-01 -> tigre-planta)
pat = re.compile(r"^(.*)-(\d+)\.jpg$", re.IGNORECASE)

grupos = {}
for nome in os.listdir(IMG):
    caminho = os.path.join(IMG, nome)
    if not os.path.isfile(caminho):
        continue  # ignora subpastas
    m = pat.match(nome)
    if not m:
        continue  # ignora logo.png, favicon.png etc.
    grupos.setdefault(m.group(1), []).append((int(m.group(2)), nome))

total_movidos = 0
os.makedirs(LIXO, exist_ok=True)

for prefixo in sorted(grupos):
    arquivos = [n for _, n in sorted(grupos[prefixo])]  # ordenados pelo numero original
    vistos = {}      # hash -> nome mantido
    mantidos = []
    for nome in arquivos:
        h = md5(os.path.join(IMG, nome))
        if h in vistos:
            destino = os.path.join(LIXO, nome)
            os.replace(os.path.join(IMG, nome), destino)
            total_movidos += 1
            print(f"  duplicado -> _duplicados: {nome} (igual a {vistos[h]})")
        else:
            vistos[h] = nome
            mantidos.append(nome)

    # renumera os mantidos para 01..NN, via nomes temporarios (evita colisao)
    temporarios = []
    for i, nome in enumerate(mantidos, 1):
        tmp = os.path.join(IMG, f"__tmp__{prefixo}__{i:02d}.jpg")
        os.replace(os.path.join(IMG, nome), tmp)
        temporarios.append(tmp)
    for i, tmp in enumerate(temporarios, 1):
        os.replace(tmp, os.path.join(IMG, f"{prefixo}-{i:02d}.jpg"))

    print(f"{prefixo}: {len(mantidos)} foto(s) unica(s) -> renumeradas 01..{len(mantidos):02d}")

print(f"\nPronto. {total_movidos} arquivo(s) duplicado(s) movido(s) para {LIXO}")
print("Confira a pasta _duplicados; se estiver tudo certo depois do rebuild, pode apaga-la.")
