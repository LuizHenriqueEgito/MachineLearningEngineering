# Feature Store
## O que é
A `feature store` guarda:
- Definição da Feature;
- Origem;
- Versão;
- Atualização
É um catalogo de feature.

## Qual a diferença entre Feature e uma Tabela

## Comandos
Após preencher os arquivos `feature_store.yaml` e `features.py`, rode o comando:
```bash
feast apply
```
Isso irá criar a pasta `data` com os arquivos:
- `online_store.db`
- `registry.db`