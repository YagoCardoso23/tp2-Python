def inclui_imposto(custo, taxa=5):
    """
    Calcula o valor de um item adicionando o imposto especificado.

    Args:
        custo (float): O custo do item antes do imposto.
        taxa (float, opcional): A taxa de imposto sobre vendas expressa em porcentagem. 
            O padrão é 5% se não for fornecida uma taxa.

    Returns:
        float: O valor do item com o imposto incluído.
    """
    imposto = custo * (taxa / 100)
    valor_com_imposto = custo + imposto
    return valor_com_imposto


help(inclui_imposto)
