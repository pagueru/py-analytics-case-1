# Case - Analytics Engineer

> [!IMPORTANT]
> As informações originais relacionadas à empresa e ao case da vaga foram **ocultadas** para preservar a confidencialidade. O conteúdo foi adaptado para manter apenas os elementos técnicos e estruturais do desafio.

Você está participando de uma etapa prática para a posição de **Analytics Engineer**. A ideia é demonstrar suas habilidades técnicas aplicadas a um cenário semelhante ao que ocorre no dia a dia dessa função.

---

## Estrutura do Case

Sua solução deve ser **autoexplicativa**, permitindo que qualquer pessoa técnica ou não-técnica possa compreendê-la.

---

## 1. Ingestão e Transformação de Dados

### Objetivo

1. Crie um **script de ingestão e transformação** dos dados no formato **JSON** e **CSV** utilizando **Python**.
   - Utilize a biblioteca de sua preferência.
   - Realize a ingestão dos dados em um **banco relacional**.
   - Exporte os resultados transformados em arquivos **.csv**.

#### Resultado Esperado – Ingestão e Transformação de Dados

- Arquivos **.csv** exportados com os dados transformados.
- Scripts Python para automação do processo.

---

## 2. Análise de Dados

### Perguntas de Análise

1. **Engajamento**:
   - Qual é a **média semanal** de medições dos clientes? Existe alguma **tendência**?

2. **Performance de Peso e Músculo**:
   - Liste os **Top 5 clientes** que mais **perderam peso** e os **Top 5** que mais **ganharam massa muscular**.
   - Separe os valores por **semana** e **acumulado**.
   - Considere o tratamento de **outliers**.

3. **Variação Significativa**:
   - Quantos clientes apresentaram **variações acima de 10%** no **peso** e no **percentual de gordura** em suas medições?

#### Resultado Esperado – Análise de Dados

- Scripts em **.py** ou queries em **.sql**.
- Resultados exportados em arquivos **.csv**.

---

## 3. Modelagem Dimensional

### Contexto dos Dados

Os dados estão disponíveis nos formatos **JSON** e **CSV**.

### Fontes de Dados

Utilize as seguintes fontes de dados:

- `weighins.json`
- `objectives.csv`
- `customer_objectives.csv`
- `medicines.csv`
- `customer_medicines_prescriptions.csv`
- `meal_plans.csv`
- `customer_meal_plan.csv`
- `customer.csv`

### Entregas Esperadas

1. **Representação visual** da modelagem dimensional proposta.
2. **Explicação detalhada** da modelagem.
3. **Análise de trade-offs** da abordagem escolhida.

---

## 4. Indicadores de Performance

### Definição de KPIs

Sugira **KPIs** relevantes para acompanhar o desempenho com base nos dados apresentados.

#### Resultado Esperado – Modelagem Dimensional

1. Lista dos indicadores com explicações detalhadas.
2. Sugestões de cálculos ou representações visuais.

---

## Observações Finais

- Utilize **SQL** avançado sempre que possível (exemplo: **CTEs** e **Window Functions**).
- Python será um diferencial importante.
- Uma **solução visual** pode agregar valor e facilitar a compreensão do case.
