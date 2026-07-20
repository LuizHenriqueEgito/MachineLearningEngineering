# Feature Store (FEAST)
## O que é
A `feature store` guarda:
- Definição da Feature;
- Origem;
- Versão;
- Atualização
É um catalogo de feature. Ela ajuda a criar um padrão nas features por exemplo: A feature `avg_transaction_30d` pode ter varios times que a criam de forma diferente, em um `feature store` todos utilizaram a feature no mesmo conceito.

## Qual a diferença entre Feature e uma Tabela (Com todas as Features)
Quando você cruza suas tabelas de features e as cria, a tabela final não sabe como as features foram criadas, quando foi criada, se houve algum tipo de mudança. Usando `Feature Store` nos temos um rastreio bem detalhado de cada feature:
```txt
Name: avg_transaction_30d

Description: Média de transações dos últimos 30 dias.

Orige: transactions_table

SQL: AVG(value) WHERE date >= current_date - 30

Owner: Credit Team

Version: 3.0.0

Update: Once a day
```
Pronto, com isso tudo é `RASTREAVEL` fica fácil reproduzir e utilizar.
- *A Feature Store reduz o risco de Training-Serving Skew (treinar em um conceito e deployar com outro) ao centralizar a definição e o cálculo das features, garantindo que treinamento e inferência utilizem a mesma lógica.*

## Offiline Store
Usado para realizarmos:
- Treinamento de modelos;
- Validação;
- Backtest.

## Online Store
Usado para:
- API;
- Decisão em tempo real.

## Point-in-Time Join
Evita **Data Leakage** (Vazamento de dados) como temos uma coluna de `timestamp` não pegamos dados futuros, apenas os dados existentes naquele ponto (naquele timestemp para aquele id), dai *point-in-time join*.

## Uso
Quando criamos uma `feature store` passamos 2 chaves, um `id` e um `timestamp` essas chaves serão utilizadas para o cruzamento com outras features. Isso evita, erros de cruzamento, e data leakage. Na hora de usar nossa feature store passamos esse `id` e o `timestamp` (se for online não precisamos do `timestamp` pois ele pega o ultimo disponivel) e escolhemos as features que queremos. Então temos dois caminhos:
- **Offline**: Passamos o `id` e `timestamp` para o cruzamento;
- **Online**: Passamos o `id`.

## FeatureView
Nos mostra:
- Quais features existem;
- De onde elas vêm;
- Quais entidades possuem;
- Schema
- TTL (Time to Live): o tempo que podemos usar antes "ttl=timedelta(days=3650)" se o ultimo registro for antes disso não usamos.

## Entity
São as chaves de identificação de cada feature

## Comandos
Após preencher os arquivos `feature_store.yaml` e `features.py`, rode o comando:
```bash
feast apply
```
Isso irá criar a pasta `data` com os arquivos:
- `online_store.db`
- `registry.db`

Ele irá sozinho encontrar os arquivos `feature_store.yaml` e `features.py` e fazer a lógica que queremos.