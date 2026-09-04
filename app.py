nome_aparelho = input("Digite o nome do aparelho: Ex: Chuveiro: ")
potencia_aparelho = float(input("Digite a potência do aparelho em Watts (W): Ex: 1500: "))
tempo_medio_uso_diario = float (input("Digite o tempo médio diário de uso do aparelho em horas: Ex: 4: "))
consumo_mensal = (potencia_aparelho * tempo_medio_uso_diario * 30) / 1000
print(f"O consumo mensal é de {consumo_mensal:.2f} kWh")

