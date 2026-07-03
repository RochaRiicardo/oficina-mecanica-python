import sqlite3

BANCO_DADOS = "oficina.db"


def conectar():
    return sqlite3.connect(BANCO_DADOS)


def criar_tabelas():
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            cpf TEXT UNIQUE,
            telefone TEXT,
            endereco TEXT,
            data_entrada TEXT,
            data_saida TEXT,
            status TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            placa TEXT UNIQUE,
            modelo TEXT,
            marca TEXT,
            ano TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ordem_de_servico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            veiculo_id INTEGER,
            defeito TEXT,
            servico TEXT,
            valor REAL,
            status TEXT,
            data TEXT,
            data_finalizacao TEXT,
            FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
        )
        """)

        conexao.commit()