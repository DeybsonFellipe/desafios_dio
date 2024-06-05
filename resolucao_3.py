capacidade_atual, aumento_percentual = map(int, input().split())
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)


nova_capacidade = round(nova_capacidade)

print(nova_capacidade)