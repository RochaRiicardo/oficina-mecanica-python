from datetime import datetime
from banco import conectar
from constantes import STATUS_ABERTO, STATUS_FINALIZADO


class OrdemDeServico:

    def __init__(
        self,
        veiculo_id="",
        defeito="",
        servico="",
        valor=0.0,
        status=STATUS_ABERTO,
        data=""
    ):

        self.veiculo_id = veiculo_id
        self.defeito = defeito
        self.servico = servico
        self.valor = valor
        self.status = status
        self.data = data

    def abrir_ordem(self):

        self.veiculo_id = input("Qual o ID do veículo? ").strip()

        if self.veiculo_id == "":
            print("ID do veículo inválido.")
            return

        self.defeito = input("Qual o defeito do veículo? ").strip().title()
        self.servico = input("Qual serviço será realizado? ").strip().title()

        try:
            self.valor = float(input("Valor do serviço: R$ "))
        except ValueError:
            print("Digite apenas números.")
            return

        if self.valor <= 0:
            print("O valor deve ser maior que zero.")
            return

        self.status = STATUS_ABERTO
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with conectar() as conexao:

            cursor = conexao.cursor()

            # Verifica se o veículo existe
            cursor.execute(
                "SELECT id FROM veiculos WHERE id = ?",
                (self.veiculo_id,)
            )

            veiculo = cursor.fetchone()

            if veiculo is None:
                print("Veículo não encontrado.")
                return

            # Cadastra a Ordem de Serviço
            cursor.execute("""
                INSERT INTO ordem_de_servico
                (
                    veiculo_id,
                    defeito,
                    servico,
                    data,
                    status,
                    valor
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                self.veiculo_id,
                self.defeito,
                self.servico,
                self.data,
                self.status,
                self.valor
            ))

            conexao.commit()

        print("\nOrdem de serviço aberta com sucesso!")
    
    
    def finalizar_ordem(self):

        id_ordem = input("ID da Ordem: ").strip()

        if id_ordem == "":
            print("ID não pode ser vazio")
            return

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("""
                SELECT status
                FROM ordem_de_servico
                WHERE id = ?
            """, (id_ordem,))

            ordem = cursor.fetchone()

            if ordem is None:
                print("Ordem não encontrada")
                return

            if ordem[0] == STATUS_FINALIZADO:
                print("Essa ordem já está finalizada.")
                return

            confirmar = input("Deseja finalizar esta ordem? (S/N): ").strip().upper()

            if confirmar != "S":
                print("Operação cancelada.")
                return

            cursor.execute("""
                UPDATE ordem_de_servico
                SET status = ?, data_finalizacao = datetime('now')
                WHERE id = ?
            """, (STATUS_FINALIZADO, id_ordem))

            conexao.commit()

        print("\nOrdem finalizada com sucesso!")