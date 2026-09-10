print("=" * 45)
print("     SISTEMA DE CONTROLE DE ESTOQUE")
print("=" * 45)

import json

try:
    with open("estoque.json", "r") as arquivo:
        estoque = json.load(arquivo)
except FileNotFoundError:
    estoque = []

while True:

    print("\nMENU PRINCIPAL")
    print("-" * 30)
    print("1 - Cadastrar pallet")
    print("2 - Transferir pallet")
    print("3 - Consultar pallet")
    print("4 - Sair")
    print("-" * 30)

    opcao = input("Digite a opção: ").strip()

    # ==================================================
    # 1 - CADASTRAR PALLET
    # ==================================================

    if opcao == "1":

        print("\nCADASTRO DE PALLET")
        print("-" * 30)

        codigo_pallet = input(
            "Digite o código do pallet: "
        ).strip()

        produto = input(
            "Digite o código do produto: "
        ).strip()

        lote = input(
            "Digite o lote: "
        ).strip()

        try:
            quantidade = int(
                input("Digite a quantidade de caixas: ")
            )

            if quantidade <= 0:
                print("\nQuantidade inválida!")
                print("Digite uma quantidade maior que zero.")
                continue

        except ValueError:
            print("\nDigite apenas números na quantidade.")
            continue

        localizacao = input(
            "Digite a localização: "
        ).strip().upper()

        # Verifica o tipo de localização
        if localizacao == "G1":
            tipo_localizacao = "CHÃO"

        elif localizacao.startswith("G1N"):
            tipo_localizacao = "PORTA-PALETE"

        else:
            print("\nLOCALIZAÇÃO INVÁLIDA!")
            print("Use G1 para chão ou G1Nxxx para porta-palete.")
            continue

        # Verifica se a localização já está ocupada
        localizacao_ocupada = False

        for pallet in estoque:
            if pallet["localizacao"] == localizacao:
                localizacao_ocupada = True
                break

        if localizacao_ocupada:
            print("\nLOCALIZAÇÃO JÁ OCUPADA!")
            print(
                f"A localização {localizacao} "
                "já possui um pallet."
            )
            continue

        # Cria o pallet
        novo_pallet = {
            "pallet": codigo_pallet,
            "produto": produto,
            "lote": lote,
            "quantidade": quantidade,
            "localizacao": localizacao,
            "tipo": tipo_localizacao
        }

        estoque.append(novo_pallet)
        with open("estoque.json", "w") as arquivo:
         json.dump(estoque, arquivo, indent=4)

        print("\nPALLET CADASTRADO COM SUCESSO!")
        print("-" * 30)
        print(f"Pallet: {codigo_pallet}")
        print(f"Produto: {produto}")
        print(f"Lote: {lote}")
        print(f"Quantidade: {quantidade} caixas")
        print(f"Localização: {localizacao}")
        print(f"Tipo: {tipo_localizacao}")

    # ==================================================
    # 2 - TRANSFERIR PALLET
    # ==================================================

    elif opcao == "2":

        print("\nTRANSFERÊNCIA DE PALLET")
        print("-" * 30)

        codigo_pallet = input(
            "Digite o código do pallet: "
        ).strip()

        pallet_encontrado = None

        # Procura o pallet
        for pallet in estoque:

            if pallet["pallet"] == codigo_pallet:
                pallet_encontrado = pallet
                break

        if pallet_encontrado is None:

            print("\nPALLET NÃO ENCONTRADO!")

        else:

            local_atual = pallet_encontrado["localizacao"]

            print(
                f"\nLocalização atual: {local_atual}"
            )

            nova_localizacao = input(
                "Digite a nova localização: "
            ).strip().upper()

            # Verifica o tipo da nova localização
            if nova_localizacao == "G1":

                tipo_destino = "CHÃO"

            elif nova_localizacao.startswith("G1N"):

                tipo_destino = "PORTA-PALETE"

            else:

                print("\nLOCALIZAÇÃO INVÁLIDA!")
                print(
                    "Use G1 para chão ou G1Nxxx para porta-palete."
                )
                continue

            # Verifica se a nova localização já está ocupada
            localizacao_ocupada = False

            for outro_pallet in estoque:

                if outro_pallet != pallet_encontrado:

                    if outro_pallet["localizacao"] == nova_localizacao:

                        localizacao_ocupada = True
                        break

            if localizacao_ocupada:

                print("\nLOCALIZAÇÃO JÁ OCUPADA!")
                print(
                    f"A localização {nova_localizacao} "
                    "já possui outro pallet."
                )
                continue

            # Faz a transferência
            pallet_encontrado["localizacao"] = nova_localizacao
            pallet_encontrado["tipo"] = tipo_destino

            with open("estoque.json", "w") as arquivo:
                json.dump(estoque, arquivo, indent=4)

            print("\nTRANSFERÊNCIA REALIZADA COM SUCESSO!")
            print("-" * 30)
            print(f"Pallet: {codigo_pallet}")
            print(f"Origem: {local_atual}")
            print(f"Destino: {nova_localizacao}")
            print(f"Tipo: {tipo_destino}")

    # ==================================================
    # 3 - CONSULTAR PALLET
    # ==================================================

    elif opcao == "3":

        print("\nCONSULTA DE PALLET")
        print("-" * 30)

        codigo_pallet = input(
            "Digite o código do pallet: "
        ).strip()

        pallet_encontrado = None

        # Procura o pallet
        for pallet in estoque:

            if pallet["pallet"] == codigo_pallet:
                pallet_encontrado = pallet
                break

        if pallet_encontrado is None:

            print("\nPALLET NÃO ENCONTRADO!")

        else:

            print("\nPALLET ENCONTRADO")
            print("-" * 30)
            print(f"Pallet: {pallet_encontrado['pallet']}")
            print(f"Produto: {pallet_encontrado['produto']}")
            print(f"Lote: {pallet_encontrado['lote']}")
            print(
                f"Quantidade: "
                f"{pallet_encontrado['quantidade']} caixas"
            )
            print(
                f"Localização: "
                f"{pallet_encontrado['localizacao']}"
            )
            print(
                f"Tipo: "
                f"{pallet_encontrado['tipo']}"
            )

    # ==================================================
    # 4 - SAIR
    # ==================================================

    elif opcao == "4":

        print("\nSistema encerrado.")
        break

    # ==================================================
    # OPÇÃO INVÁLIDA
    # ==================================================

    else:

        print("\nOPÇÃO INVÁLIDA!")
        print("Digite 1, 2, 3 ou 4.")