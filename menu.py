from cliente import Clientes
from veiculo import Veiculos
from ordem_servico import OrdemDeServico
from consultas import Consultas
from relatorios import Relatorios

cliente = Clientes()
veiculo = Veiculos()
ordem = OrdemDeServico()
consultas = Consultas()
relatorio = Relatorios()


def menu_principal():

    while True:

        print("\n" + "=" * 45)
        print("       SISTEMA OFICINA MECÂNICA")
        print("=" * 45)
        print("1 - Clientes")
        print("2 - Veículos")
        print("3 - Ordem de Serviço")
        print("4 - Relatórios")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        # ===========================
        # CLIENTES
        # ===========================

        if opcao == "1":

            while True:

                print("\n===== CLIENTES =====")
                print("1 - Cadastrar Cliente")
                print("2 - Consultar Cliente")
                print("3 - Listar Clientes")
                print("4 - Remover Cliente")
                print("5 - Voltar")

                op = input("Escolha: ")

                if op == "1":
                    cliente.cadastro_clientes()

                elif op == "2":
                    consultas.consultar_cliente()

                elif op == "3":
                    consultas.listar_clientes()

                elif op == "4":
                    print("Função ainda não implementada.")

                    # futuramente:
                    # cliente.remover_cliente()

                elif op == "5":
                    break

                else:
                    print("Opção inválida.")

        # ===========================
        # VEÍCULOS
        # ===========================

        elif opcao == "2":

            while True:

                print("\n===== VEÍCULOS =====")
                print("1 - Cadastrar Veículo")
                print("2 - Consultar Placa")
                print("3 - Listar Veículos")
                print("4 - Voltar")

                op = input("Escolha: ")

                if op == "1":
                    veiculo.cadastrar_veiculo()

                elif op == "2":
                    consultas.consultar_placa()

                elif op == "3":
                    consultas.listar_veiculos()

                elif op == "4":
                    break

                else:
                    print("Opção inválida.")

        # ===========================
        # ORDENS DE SERVIÇO
        # ===========================

        elif opcao == "3":

            while True:

                print("\n===== ORDEM DE SERVIÇO =====")
                print("1 - Abrir Ordem")
                print("2 - Finalizar Ordem")
                print("3 - Consultar Ordem")
                print("4 - Listar Ordens")
                print("5 - Voltar")

                op = input("Escolha: ")

                if op == "1":
                    ordem.abrir_ordem()

                elif op == "2":
                    ordem.finalizar_ordem()

                elif op == "3":
                    consultas.consultar_ordem()

                elif op == "4":
                    consultas.listar_ordens()

                elif op == "5":
                    break

                else:
                    print("Opção inválida.")

        # ===========================
        # RELATÓRIOS
        # ===========================

        elif opcao == "4":

            while True:

                print("\n===== RELATÓRIOS =====")
                print("1 - Resumo da Oficina")
                print("2 - Voltar")

                op = input("Escolha: ")

                if op == "1":
                    relatorio.resumo_oficina()

                elif op == "2":
                    break

                else:
                    print("Opção inválida.")

        elif opcao == "5":

            print("\nSistema encerrado.")
            break

        else:
            print("Escolha uma opção válida.")