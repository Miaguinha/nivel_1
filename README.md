# PDV com Descontos

Este projeto implementa um PDV (Ponto de Venda) simples em Python. Ele recebe o valor de uma compra e a idade do cliente, aplica os descontos previstos nas regras e informa o valor final. É possível registrar várias compras durante o atendimento e, ao encerrar, consultar o resumo do dia.

## Como funciona

1. O programa pede o valor da compra e a idade do cliente.
2. Se a idade for 65 anos ou mais, aplica 20% de desconto.
3. Depois, se o valor já descontado for maior que R$ 100,00, aplica mais 10% sobre esse novo valor.
4. A compra é guardada em uma lista com `.append()` e o valor final é mostrado.
5. Ao digitar `0` como valor da compra, o programa encerra e exibe a quantidade de compras, os totais bruto, de descontos e final.
6. Valores e idades negativos são recusados e solicitados novamente.

## Como rodar

No terminal, dentro da pasta `nivel_1`, execute:

```bash
python pdv.py
```

## Casos de teste

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

No caso 5, R$ 125,00 com idade 70 passa a valer R$ 100,00 após o desconto de idade; como a regra exige valor **maior** que R$ 100,00, o desconto extra não é aplicado.
