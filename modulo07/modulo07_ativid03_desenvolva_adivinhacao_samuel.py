# Dados do aluno e da instituição
escola = "Colégio Integração"
aluno = "Carlos Eduardo"
turma = "3º Ano A"
disciplina = "Matemática"

# Notas das avaliações (com pesos diferentes)
prova1 = 8.5    # Peso 3
prova2 = 6.5    # Peso 3
trabalho = 9.5  # Peso 4

# Cálculo da média ponderada
media = (prova1 * 3 + prova2 * 3 + trabalho * 4) / 10

# Frequência
aulas_dadas = 80
faltas = 8
presenca = ((aulas_dadas - faltas) / aulas_dadas) * 100

# Validação de situação (Média >= 7.0 E Presença >= 75%)
if media >= 7.0 and presenca >= 75:
    situacao = "APROVADO"
elif media >= 5.0 and presenca >= 75:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "REPROVADO"

# Exibição do Boletim Completo
print("=" * 45)
print(f"{escola.upper():^45}")
print(f"{'BOLETIM ESCOLAR COMPLETO':^45}")
print("=" * 45)
print(f"Aluno: {aluno:<22} Turma: {turma}")
print(f"Disciplina: {disciplina}")
print("-" * 45)
print(f"{'Avaliação':<20} | {'Nota':<8} | {'Peso':<6}")
print("-" * 45)
print(f"{'Prova 1':<20} | {prova1:<8.1f} | {'3':<6}")
print(f"{'Prova 2':<20} | {prova2:<8.1f} | {'3':<6}")
print(f"{'Trabalho Final':<20} | {trabalho:<8.1f} | {'4':<6}")
print("-" * 45)
print(f"Média Ponderada: {media:.2f}")
print(f"Frequência:      {presenca:.1f}% ({faltas} faltas em {aulas_dadas} aulas)")
print("-" * 45)
print(f"Status Final:    [{situacao}]")
print("=" * 45)