from banco import conectar
from constantes import STATUS_ABERTO, STATUS_FINALIZADO



class Relatorios:

    def resumo_oficina(self):

        with conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute("SELECT COUNT(*) FROM clientes")
            clientes = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM veiculos")
            veiculos = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM ordem_de_servico")
            ordens = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM ordem_de_servico WHERE status = ?", (STATUS_ABERTO,))
            abertas = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM ordem_de_servico WHERE status = ?", (STATUS_FINALIZADO,))
            finalizadas = cursor.fetchone()[0]

            cursor.execute("SELECT SUM(valor) FROM ordem_de_servico WHERE status = ?", (STATUS_FINALIZADO,))
            faturamento = cursor.fetchone()[0]

        faturamento = faturamento if faturamento else 0

        print("\n===== RELATÓRIO =====")
        print(f"Clientes: {clientes}")
        print(f"Veículos: {veiculos}")
        print(f"Ordens: {ordens}")
        print(f"Abertas: {abertas}")
        print(f"Finalizadas: {finalizadas}")
        print(f"Faturamento: R$ {faturamento:.2f}")