from banco import conectar
from constantes import STATUS_ABERTO


class Consultas:

    # ===========================
    # LISTAR CLIENTES
    # ===========================

    def listar_clientes(self):

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, cliente, cpf, telefone, endereco, status
                FROM clientes
            """)

            todos_clientes = cursor.fetchall()

        if not todos_clientes:
            print("\nLista de clientes está vazia!")
            return

        total = len(todos_clientes)
        cliente_ativo = 0
        cliente_nao_ativo = 0

        print("\n========== CLIENTES ==========")

        for cliente in todos_clientes:

            id_cliente, nome, cpf, telefone, endereco, status = cliente

            print(f"ID........: {id_cliente}")
            print(f"Cliente...: {nome}")
            print(f"CPF.......: {cpf}")
            print(f"Telefone..: {telefone}")
            print(f"Endereço..: {endereco}")
            print(f"Status....: {status}")
            print("-" * 40)

            if status == STATUS_ABERTO:
                cliente_ativo += 1
            else:
                cliente_nao_ativo += 1

        print("\n========== RESUMO ==========")
        print(f"Total de clientes : {total}")
        print(f"Clientes ativos   : {cliente_ativo}")
        print(f"Clientes inativos : {cliente_nao_ativo}")

    # ===========================
    # LISTAR VEÍCULOS
    # ===========================

    def listar_veiculos(self):

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, placa, modelo, marca, ano, cliente_id
                FROM veiculos
            """)

            todos_veiculos = cursor.fetchall()

        if not todos_veiculos:
            print("\nLista de veículos está vazia!")
            return

        print("\n========== VEÍCULOS ==========")

        for veiculo in todos_veiculos:

            id_veiculo, placa, modelo, marca, ano, cliente_id = veiculo

            print(f"ID........: {id_veiculo}")
            print(f"Placa.....: {placa}")
            print(f"Modelo....: {modelo}")
            print(f"Marca.....: {marca}")
            print(f"Ano.......: {ano}")
            print(f"Cliente ID: {cliente_id}")
            print("-" * 40)

    # ===========================
    # LISTAR ORDENS
    # ===========================

    def listar_ordens(self):

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, veiculo_id, defeito, servico, valor, status, data
                FROM ordem_de_servico
            """)

            todas_ordens = cursor.fetchall()

        if not todas_ordens:
            print("\nLista de ordens está vazia!")
            return

        print("\n========== ORDENS DE SERVIÇO ==========")

        for ordem in todas_ordens:

            id_ordem, veiculo_id, defeito, servico, valor, status, data = ordem

            print(f"OS........: {id_ordem}")
            print(f"Veículo...: {veiculo_id}")
            print(f"Defeito...: {defeito}")
            print(f"Serviço...: {servico}")
            print(f"Valor.....: R$ {valor:.2f}")
            print(f"Status....: {status}")
            print(f"Data......: {data}")
            print("-" * 40)

    # ===========================
    # CONSULTAR CLIENTE
    # ===========================

    def consultar_cliente(self):

        cpf = input("CPF: ").strip()

        if cpf == "":
            print("CPF vazio")
            return

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, cliente, cpf, telefone, endereco, status
                FROM clientes
                WHERE cpf = ?
            """, (cpf,))

            cliente = cursor.fetchone()

        if cliente is None:
            print("Cliente não encontrado.")
            return

        id_cliente, nome, cpf, telefone, endereco, status = cliente

        print("\n========== CLIENTE ==========")
        print(f"ID........: {id_cliente}")
        print(f"Nome......: {nome}")
        print(f"CPF.......: {cpf}")
        print(f"Telefone..: {telefone}")
        print(f"Endereço..: {endereco}")
        print(f"Status....: {status}")

    # ===========================
    # CONSULTAR VEÍCULO
    # ===========================

    def consultar_placa(self):

        placa = input("Placa: ").strip().upper()

        if placa == "":
            print("Placa vazia")
            return

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("""
                SELECT cliente_id, placa, modelo, marca, ano
                FROM veiculos
                WHERE placa = ?
            """, (placa,))

            veiculo = cursor.fetchone()

        if veiculo is None:
            print("Veículo não encontrado.")
            return

        cliente_id, placa, modelo, marca, ano = veiculo

        print("\n========== VEÍCULO ==========")
        print(f"Cliente ID: {cliente_id}")
        print(f"Placa.....: {placa}")
        print(f"Modelo....: {modelo}")
        print(f"Marca.....: {marca}")
        print(f"Ano.......: {ano}")

    # ===========================
    # CONSULTAR ORDEM
    # ===========================

    def consultar_ordem(self):

        id_ordem = input("ID da Ordem: ").strip()

        if id_ordem == "":
            print("ID vazio")
            return

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("""
                SELECT veiculo_id, defeito, servico, valor, status, data
                FROM ordem_de_servico
                WHERE id = ?
            """, (id_ordem,))

            ordem = cursor.fetchone()

        if ordem is None:
            print("Ordem não encontrada.")
            return

        veiculo_id, defeito, servico, valor, status, data = ordem

        print("\n========== ORDEM DE SERVIÇO ==========")
        print(f"Veículo ID: {veiculo_id}")
        print(f"Defeito...: {defeito}")
        print(f"Serviço...: {servico}")
        print(f"Valor.....: R$ {valor:.2f}")
        print(f"Status....: {status}")
        print(f"Data......: {data}")