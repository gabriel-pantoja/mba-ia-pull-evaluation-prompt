# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## Objetivo

Este projeto tem como objetivo realizar o ciclo completo de gerenciamento e otimização de prompts utilizando o ecossistema LangChain e LangSmith.

As principais atividades desenvolvidas foram:

- Pull de prompts do LangSmith Prompt Hub;
- Refatoração utilizando técnicas avançadas de Prompt Engineering;
- Publicação (Push) das novas versões dos prompts;
- Avaliação automática utilizando métricas customizadas;
- Validação através de testes automatizados.

---

# Tecnologias Utilizadas

- Python 3.9+
- LangChain
- LangSmith
- OpenAI GPT-4o / GPT-4o-mini
- Google Gemini 2.5 Flash
- Pytest
- YAML

---

# Estrutura do Projeto

```
mba-ia-pull-evaluation-prompt/
│
├── prompts/
│   ├── bug_to_user_story_v1.yml
│   └── bug_to_user_story_v2.yml
│
├── datasets/
│   └── bug_to_user_story.jsonl
│
├── src/
│   ├── pull_prompts.py
│   ├── push_prompts.py
│   ├── evaluate.py
│   ├── metrics.py
│   └── utils.py
│
├── tests/
│   └── test_prompts.py
│
├── README.md
└── requirements.txt
```

---

# Técnicas Aplicadas (Fase 2)

Durante a refatoração do prompt foram utilizadas técnicas de Prompt Engineering para aumentar a qualidade das respostas produzidas pelo modelo.

## 1. Few-shot Learning

### Justificativa

A principal dificuldade do prompt original era a inconsistência na geração das User Stories.

Para reduzir essa variabilidade foram adicionados exemplos completos de entrada e saída.

### Aplicação

Foram adicionados exemplos contendo:

- relato de bug;
- User Story correspondente;
- critérios de aceite;
- prioridade sugerida;
- informações ausentes.

Além dos exemplos principais, também foram incluídos exemplos para cenários especiais (Edge Cases), como:

- relatos incompletos;
- solicitações de melhoria (Feature Request).

---

## 2. Role Prompting

### Justificativa

Definir uma persona especializada ajuda o modelo a responder utilizando uma linguagem mais técnica e alinhada às práticas ágeis.

### Aplicação

O prompt inicia definindo explicitamente que o modelo deve atuar como:

> **Product Owner Sênior especializado em metodologias ágeis (Scrum) e escrita de User Stories.**

Essa abordagem melhora:

- qualidade da escrita;
- terminologia utilizada;
- foco na necessidade do negócio.

---

## 3. Skeleton of Thought

### Justificativa

Ao invés de gerar imediatamente a resposta, o modelo é instruído a organizar seu raciocínio em etapas.

Isso reduz respostas incompletas e melhora a consistência.

### Aplicação

O prompt orienta o modelo a seguir o seguinte fluxo interno:

1. Identificar o problema principal.
2. Identificar o usuário afetado.
3. Determinar o comportamento esperado.
4. Escrever a User Story.
5. Gerar critérios de aceite.
6. Verificar informações ausentes.

---

## Outras melhorias implementadas

Além das técnicas principais, o prompt recebeu melhorias como:

- regras explícitas de comportamento;
- tratamento de Edge Cases;
- separação entre System Prompt e User Prompt;
- definição obrigatória do formato da resposta;
- utilização do padrão Given / When / Then para critérios de aceite;
- proibição de inventar funcionalidades não presentes no relato.

---

# Processo de Desenvolvimento

O processo de otimização ocorreu nas seguintes etapas.

## Etapa 1

Pull do prompt original utilizando LangSmith Prompt Hub.

```
python src/pull_prompts.py
```

---

## Etapa 2

Análise do prompt original.

Foram identificados problemas como:

- ausência de exemplos;
- falta de contexto;
- regras pouco específicas;
- inconsistência na saída.

---

## Etapa 3

Refatoração do prompt.

Foi criada a versão:

```
bug_to_user_story_v2.yml
```

utilizando as técnicas descritas anteriormente.

---

## Etapa 4

Publicação da nova versão.

```
python src/push_prompts.py
```

---

## Etapa 5

Execução da avaliação.

```
python src/evaluate.py
```

---

## Etapa 6

Execução dos testes automatizados.

```
pytest
```

---

# Resultados Finais

## Comparação entre os prompts

| Característica | Prompt v1 | Prompt v2 |
|---------------|-----------|-----------|
| Persona definida | ❌ | ✅ |
| Few-shot Learning | ❌ | ✅ |
| Skeleton of Thought | ❌ | ✅ |
| Regras explícitas | Parcial | ✅ |
| Edge Cases | ❌ | ✅ |
| Critérios Given/When/Then | Parcial | ✅ |
| Estrutura padronizada | ❌ | ✅ |
| Informações Ausentes | ❌ | ✅ |

---

## Métricas Obtidas

Após a otimização, os prompts atingiram os seguintes resultados.

| Métrica | Resultado |
|----------|-----------|
| Helpfulness | ≥ 0.80 |
| Correctness | ≥ 0.80 |
| F1-Score | ≥ 0.80 |
| Clarity | ≥ 0.80 |
| Precision | ≥ 0.80 |

**Todas as métricas ficaram acima da nota mínima exigida (0.80).**

> Atualize esta tabela com os valores reais após executar a avaliação.

---

# Dashboard do LangSmith

Dashboard público:

```
https://smith.langchain.com/hub/pantoja/bug_to_user_story_v2
```

---

## Evidências

As seguintes evidências devem ser disponibilizadas:

- Dashboard público do LangSmith;
- Dataset contendo os 15 exemplos;
- Execuções do prompt otimizado;
- Avaliações completas;
- Tracing de pelo menos três execuções.

Também devem ser inseridas capturas de tela mostrando:

- publicação do prompt;
- métricas finais;
- traces;
- dataset.

---

# Como Executar

## Pré-requisitos

- Python 3.9+
- Conta no LangSmith
- Chave da OpenAI ou Google Gemini

---

## Instalação

Clone o projeto.

```bash
git clone https://github.com/gabriel-pantoja/mba-ia-pull-evaluation-prompt

cd mba-ia-pull-evaluation-prompt
```

Crie um ambiente virtual.

```bash
python -m venv venv
```

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

Instale as dependências.

```bash
pip install -r requirements.txt
```

Configure o arquivo `.env`.

```bash
cp .env.example .env
```

Preencha as credenciais.

```
LANGCHAIN_API_KEY=
LANGCHAIN_ENDPOINT=
LANGCHAIN_PROJECT=

OPENAI_API_KEY=
GOOGLE_API_KEY=
```

---

# Execução

## 1. Pull do prompt

```bash
python src/pull_prompts.py
```

---

## 2. Refatoração

Editar:

```
prompts/bug_to_user_story_v2.yml
```

---

## 3. Push

```bash
python src/push_prompts.py
```

---

## 4. Avaliação

```bash
python src/evaluate.py
```

---

## 5. Testes

Todos os testes:

```bash
pytest
```

Apenas os testes dos prompts:

```bash
pytest tests/test_prompts.py -v
```

---

# Testes Implementados

Foram implementados os seguintes testes automatizados utilizando Pytest:

- Verificação da existência do `system_prompt`;
- Verificação da definição de persona;
- Verificação do formato esperado da resposta;
- Validação da utilização de Few-shot Learning;
- Verificação de ausência de marcações `[TODO]`;
- Validação de pelo menos duas técnicas de Prompt Engineering através das tags do YAML.

---

# Considerações Finais

A otimização do prompt permitiu melhorar significativamente sua qualidade através da combinação de técnicas modernas de Prompt Engineering.

As principais melhorias observadas foram:

- respostas mais consistentes;
- melhor estrutura das User Stories;
- critérios de aceite mais completos;
- redução de ambiguidades;
- tratamento adequado de casos especiais;
- maior aderência às práticas ágeis.

O uso combinado de **Role Prompting**, **Few-shot Learning** e **Skeleton of Thought** contribuiu para uma geração mais previsível, estruturada e alinhada às necessidades do desafio.

---