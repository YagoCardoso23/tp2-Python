def inclui_imposto(custo, taxa=5):
    imposto = custo * (taxa / 100)
    valor_com_imposto = custo + imposto
    return valor_com_imposto


custo_item = float(input("Digite o custo do item: "))


taxa_imposto = input("Digite a taxa de imposto (em porcentagem), pressione Enter para usar a taxa padrão de 5%: ")


if taxa_imposto:
   
    valor_final = inclui_imposto(custo_item, float(taxa_imposto))
else:
    
    valor_final = inclui_imposto(custo_item)

    
print("O valor do item com o imposto incluído é:", valor_final)
