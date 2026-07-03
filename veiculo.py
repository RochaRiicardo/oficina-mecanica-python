from banco import conectar


class Veiculos:

    def __init__(self, placa="", modelo="", marca="", ano="", cliente_id=""):

        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cliente_id = cliente_id

    def cadastrar_veiculo(self):

        self.cliente_id = input("Qual o ID do cliente? ").strip()

        if self.cliente_id == "":
            print("ID do cliente não pode estar vazio!")
            return

        self.placa = input("Placa do veículo: ").strip().upper()
        self.modelo = input("Modelo do veículo: ").strip().title()
        self.marca = input("Marca do veículo: ").strip().title()
        self.ano = input("Ano do veículo: ").strip()

        with conectar() as conexao:

            cursor = conexao.cursor()

            # Verifica se o cliente existe
            cursor.execute(
                "SELECT id FROM clientes WHERE id = ?",
                (self.cliente_id,)
            )

            cliente = cursor.fetchone()

            if cliente is None:
                print("Cliente não encontrado.")
                return

            # Cadastra o veículo
            cursor.execute("""
                INSERT INTO veiculos
                (
                    cliente_id,
                    placa,
                    modelo,
                    marca,
                    ano
                )
                VALUES (?, ?, ?, ?, ?)
            """,
            (
                self.cliente_id,
                self.placa,
                self.modelo,
                self.marca,
                self.ano
            ))

            conexao.commit()

        print(f"\nVeículo '{self.placa}' cadastrado com sucesso!")