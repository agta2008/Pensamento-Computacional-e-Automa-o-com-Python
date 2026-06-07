#  Mission Control AI

##  Sobre o Projeto

O Mission Control AI é um sistema desenvolvido em Python para simular o monitoramento inteligente de uma missão espacial experimental.

O programa analisa diferentes ciclos de monitoramento da missão, identifica situações de risco, gera alertas automáticos, calcula o nível de risco operacional e produz um relatório final com informações detalhadas sobre o estado da missão.

Este projeto foi desenvolvido para a Global Solution 2026.1 da disciplina de Pensamento Computacional e Automação com Python.

---

##  Objetivo

Criar um sistema capaz de:

- Monitorar dados de uma missão espacial;
- Analisar temperatura, comunicação, bateria, oxigênio e estabilidade;
- Detectar situações de atenção e risco crítico;
- Calcular a pontuação de risco de cada ciclo;
- Identificar a tendência da missão;
- Determinar a área mais afetada;
- Gerar recomendações automáticas;
- Exibir um relatório final da missão.

---

##  Dados Monitorados

Cada ciclo da missão possui as seguintes informações:

| Posição | Informação |
|----------|------------|
| 0 | Temperatura |
| 1 | Comunicação |
| 2 | Bateria |
| 3 | Oxigênio |
| 4 | Estabilidade |

Exemplo:

```python
[24, 92, 88, 96, 90]
```

Onde:

- Temperatura: 24°C
- Comunicação: 92%
- Bateria: 88%
- Oxigênio: 96%
- Estabilidade: 90%

---

##  Estrutura dos Dados

```python
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]
```

---

##  Regras de Classificação

### Temperatura

| Condição | Status |
|-----------|---------|
| < 18°C | Atenção |
| 18°C até 30°C | Normal |
| 31°C até 35°C | Atenção |
| > 35°C | Crítico |

### Comunicação

| Condição | Status |
|-----------|---------|
| < 30% | Crítico |
| 30% a 59% | Atenção |
| ≥ 60% | Normal |

### Bateria

| Condição | Status |
|-----------|---------|
| < 20% | Crítico |
| 20% a 49% | Atenção |
| ≥ 50% | Normal |

### Oxigênio

| Condição | Status |
|-----------|---------|
| < 80% | Crítico |
| 80% a 89% | Atenção |
| ≥ 90% | Normal |

### Estabilidade

| Condição | Status |
|-----------|---------|
| < 40% | Crítico |
| 40% a 69% | Atenção |
| ≥ 70% | Normal |

---

##  Sistema de Pontuação

Cada classificação gera uma pontuação:

| Status | Pontos |
|----------|---------|
| Normal | 0 |
| Atenção | 1 |
| Crítico | 2 |

Pontuação máxima por ciclo:

```text
10 pontos
```

---

##  Funcionalidades

O sistema possui funções responsáveis por:

- Analisar temperatura;
- Analisar comunicação;
- Analisar bateria;
- Analisar oxigênio;
- Analisar estabilidade;
- Classificar cada ciclo;
- Calcular riscos;
- Identificar tendências;
- Gerar recomendações;
- Encontrar a área mais afetada;
- Gerar relatório final.

---

##  Relatório Final

Ao finalizar a execução, o programa apresenta:

- Média de temperatura;
- Média de comunicação;
- Média de bateria;
- Média de oxigênio;
- Média de estabilidade;
- Ciclo mais crítico;
- Maior pontuação de risco;
- Risco médio da missão;
- Tendência da missão;
- Área mais afetada;
- Classificação final da missão.

---

##  Tecnologias Utilizadas

- Python 3
- Listas
- Matrizes
- Estruturas de repetição
- Estruturas condicionais
- Funções

---

##  Licença

Projeto acadêmico desenvolvido para fins educacionais na FIAP.
