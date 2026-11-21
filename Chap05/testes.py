dias_da_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
hoje = 4  # Índice de 'Sex'

# Qual será o dia daqui a 10 dias?
dia_futuro = (hoje + 10) % len(dias_da_semana) 
print(dias_da_semana[dia_futuro])  # Saída: Seg

total_de_segundos = 3665
horas = total_de_segundos // 3600
minutos = (total_de_segundos) % 3600 // 60
segundos = total_de_segundos % 60
print(f'{horas}h {minutos}m {segundos}s') 

largura = 4
for i in range(12):
    linha = i // largura
    coluna = i % largura
    print(f"Índice {i:2d} -> Linha {linha}, Coluna {coluna}")