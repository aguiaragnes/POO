class Empregado:
    def __init__(self , nome, salario = 1100.00):
        self.nome = nome
        self.salario_base = salario

    def desconto_vale_transporte(self):
        return salario_base * 0.06

empregado1 = Empregado("João")
print(empregado1.nome)
print(empregado1.salario_base)
print(f'Desconto vale transporte: {desconto_vale_transporte}')
