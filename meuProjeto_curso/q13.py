# Função para ler os nomes dos produtos
def ler_produtos():
    produtos = input("Informe os nomes dos produtos: ").split(", ")
    return produtos

# Função para ler as vendas diárias
def ler_vendas(num_produtos):
    vendas = []
    while True:
        entrada = input("Informe as quantidades de vendas: ")
        if entrada == "":
            break
        vendas_diarias = list(map(int, entrada.split(", ")))
        vendas.append(vendas_diarias)
    return vendas

# Função para calcular o total de vendas por produto
def calcular_totais(vendas):
    num_produtos = len(vendas)
    totais = [0] * num_produtos
    
    for i in range(num_produtos):
        for vendas_diaria in vendas[i]:
            totais[i] += vendas_diaria
            
    return totais

# Função principal
def main():
    produtos = ler_produtos()
    vendas = ler_vendas(len(produtos))
    
    totais = calcular_totais(vendas)
    
    # Encontrar o produto com o maior total de vendas
    produto_selecionado = produtos[0]
    total_vendas_selecionado = totais[0]
    
    for i in range(1, len(produtos)):
        if totais[i] > total_vendas_selecionado:
            produto_selecionado = produtos[i]
            total_vendas_selecionado = totais[i]
    
    # Imprimir resultado
    print(f"Produto selecionado: {produto_selecionado}")
    print(f"Total de vendas de {produto_selecionado}: {total_vendas_selecionado}")

# Chamar a função principal
if __name__ == "__main__":
    main()
