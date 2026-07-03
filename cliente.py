from datetime import datetime
from banco import conectar
from constantes import STATUS_ABERTO


class Clientes:

    def __init__(
        self,
        cliente="",
        cpf="",
        telefone="",
        endereco="",
        data_entrada="",
        data_saida="",
        status=STATUS_ABERTO
    ):

        self.cliente = cliente
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.status = status

    def cadastro_clientes(self):

        self.cliente = input("Nome do Cliente: ").strip().title()

        if self.cliente == "":
            print("Nome do cliente não pode ficar vazio.")
            return

        self.cpf = input("CPF: ").strip()
        self.telefone = input("Telefone: ").strip()
        self.endereco = input("Endereço: ").strip()

        self.data_entrada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute(
                "SELECT id FROM clientes WHERE cpf = ?",
                (self.cpf,)
            )

            cpf_existe = cursor.fetchone()

            if cpf_existe:
                print("Já existe um cliente com esse CPF.")
                return

            cursor.execute("""
                INSERT INTO clientes
                (
                    cliente,
                    cpf,
                    telefone,
                    endereco,
                    data_entrada,
                    data_saida,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                self.cliente,
                self.cpf,
                self.telefone,
                self.endereco,
                self.data_entrada,
                self.data_saida,
                self.status
            ))

            conexao.commit()

        print(f"\nCliente '{self.cliente}' cadastrado com sucesso!")