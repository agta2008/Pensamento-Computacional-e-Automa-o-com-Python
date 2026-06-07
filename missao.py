# ==========================================
# MISSION CONTROL AI
# ==========================================

nome_missao = "Orion Test Alpha"
nome_equipe = "Equipe Apollo"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


# ==========================================
# FUNÇÕES DE ANÁLISE
# ==========================================

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável."


def identificar_area_mais_afetada(pontos):
    maior = max(pontos)
    indice = pontos.index(maior)
    return areas_monitoradas[indice]


def gerar_recomendacao(classificacoes):
    recomendacoes = []

    if classificacoes[0] == "CRÍTICO":
        recomendacoes.append("Verificar controle térmico")

    if classificacoes[1] == "CRÍTICO":
        recomendacoes.append("Restabelecer comunicação")

    if classificacoes[2] == "CRÍTICO":
        recomendacoes.append("Ativar economia de energia")

    if classificacoes[3] == "CRÍTICO":
        recomendacoes.append("Acionar suporte à vida")

    if classificacoes[4] == "CRÍTICO":
        recomendacoes.append("Reduzir operações não essenciais")

    if not recomendacoes:
        return "Operação normal."

    return " | ".join(recomendacoes)


# ==========================================
# PROCESSAMENTO
# ==========================================

riscos_ciclos = []
pontos_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missão:", nome_missao)
print("Equipe:", nome_equipe)
print()

for i, ciclo in enumerate(dados_missao, start=1):

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    temp_class, temp_pontos = analisar_temperatura(temperatura)
    com_class, com_pontos = analisar_comunicacao(comunicacao)
    bat_class, bat_pontos = analisar_bateria(bateria)
    oxi_class, oxi_pontos = analisar_oxigenio(oxigenio)
    est_class, est_pontos = analisar_estabilidade(estabilidade)

    risco_total = (
        temp_pontos +
        com_pontos +
        bat_pontos +
        oxi_pontos +
        est_pontos
    )

    riscos_ciclos.append(risco_total)

    pontos_areas[0] += temp_pontos
    pontos_areas[1] += com_pontos
    pontos_areas[2] += bat_pontos
    pontos_areas[3] += oxi_pontos
    pontos_areas[4] += est_pontos

    print("-" * 60)
    print(f"CICLO {i}")
    print("-" * 60)

    print(f"Temperatura: {temperatura}°C -> {temp_class}")
    print(f"Comunicação: {comunicacao}% -> {com_class}")
    print(f"Bateria: {bateria}% -> {bat_class}")
    print(f"Oxigênio: {oxigenio}% -> {oxi_class}")
    print(f"Estabilidade: {estabilidade}% -> {est_class}")

    print(f"Pontuação de risco: {risco_total}")
    print(f"Classificação: {classificar_ciclo(risco_total)}")

    recomendacao = gerar_recomendacao([
        temp_class,
        com_class,
        bat_class,
        oxi_class,
        est_class
    ])

    print("Recomendação:", recomendacao)
    print()

# ==========================================
# RELATÓRIO FINAL
# ==========================================

media_temp = sum(linha[0] for linha in dados_missao) / len(dados_missao)
media_com = sum(linha[1] for linha in dados_missao) / len(dados_missao)
media_bat = sum(linha[2] for linha in dados_missao) / len(dados_missao)
media_oxi = sum(linha[3] for linha in dados_missao) / len(dados_missao)
media_est = sum(linha[4] for linha in dados_missao) / len(dados_missao)

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

area_mais_afetada = identificar_area_mais_afetada(pontos_areas)

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

print("=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

print("Missão:", nome_missao)
print("Equipe:", nome_equipe)

print(f"Média Temperatura: {media_temp:.2f}°C")
print(f"Média Comunicação: {media_com:.2f}%")
print(f"Média Bateria: {media_bat:.2f}%")
print(f"Média Oxigênio: {media_oxi:.2f}%")
print(f"Média Estabilidade: {media_est:.2f}%")

print(f"\nCiclo mais crítico: {ciclo_critico}")
print(f"Maior risco: {maior_risco}")

print(f"Risco médio: {risco_medio:.2f}")

print("\nTendência:")
print(analisar_tendencia(riscos_ciclos))

print("\nPontuação por área:")
for area, pontos in zip(areas_monitoradas, pontos_areas):
    print(f"{area}: {pontos} pontos")

print("\nÁrea mais afetada:")
print(area_mais_afetada)

print("\nClassificação Final:")
print(classificar_ciclo(round(risco_medio)))
