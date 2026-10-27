"""Desafio Nível 1 — PDV com Descontos (Python)."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


CENTAVOS = Decimal("0.01")


def ler_valor_compra():
    """Lê um valor não negativo. Zero encerra o atendimento."""
    while True:
        texto = input("Valor da compra (R$ 0 para encerrar): ").strip().replace(",", ".")
        try:
            valor = Decimal(texto)
        except InvalidOperation:
            print("Aviso: digite um valor numérico válido.")
            continue

        if valor < 0:
            print("Aviso: o valor da compra não pode ser negativo.")
            continue
        return valor


def ler_idade():
    """Lê uma idade inteira não negativa."""
    while True:
        texto = input("Idade do cliente: ").strip()
        try:
            idade = int(texto)
        except ValueError:
            print("Aviso: digite a idade como um número inteiro.")
            continue

        if idade < 0:
            print("Aviso: a idade não pode ser negativa.")
            continue
        return idade


def formatar_reais(valor):
    """Formata um Decimal com duas casas decimais."""
    return f"R$ {valor.quantize(CENTAVOS, rounding=ROUND_HALF_UP):.2f}"


def calcular_compra(valor_bruto, idade):
    """Aplica primeiro o desconto de idade e depois o de valor."""
    valor_final = valor_bruto
    desconto_idade = Decimal("0.00")
    desconto_valor = Decimal("0.00")

    if idade >= 65:
        desconto_idade = valor_final * Decimal("0.20")
        valor_final -= desconto_idade

    if valor_final > Decimal("100"):
        desconto_valor = valor_final * Decimal("0.10")
        valor_final -= desconto_valor

    return {
        "bruto": valor_bruto,
        "desconto_idade": desconto_idade,
        "desconto_valor": desconto_valor,
        "final": valor_final,
    }


def mostrar_resumo(compras):
    """Exibe o resumo das compras registradas no dia."""
    total_bruto = sum((compra["bruto"] for compra in compras), Decimal("0.00"))
    total_descontos = sum(
        (compra["desconto_idade"] + compra["desconto_valor"] for compra in compras),
        Decimal("0.00"),
    )
    total_final = sum((compra["final"] for compra in compras), Decimal("0.00"))

    print("\n--- Resumo do dia ---")
    print(f"Quantidade de compras registradas: {len(compras)}")
    print(f"Total bruto: {formatar_reais(total_bruto)}")
    print(f"Total de descontos concedidos: {formatar_reais(total_descontos)}")
    print(f"Total final: {formatar_reais(total_final)}")


def main():
    compras = []

    print("=== PDV com descontos ===")
    while True:
        valor = ler_valor_compra()
        if valor == 0:
            break

        idade = ler_idade()
        compra = calcular_compra(valor, idade)
        compras.append(compra)

        print(f"Valor final: {formatar_reais(compra['final'])}")

    mostrar_resumo(compras)


if __name__ == "__main__":
    main()
