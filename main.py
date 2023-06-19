import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user='root',
    password='1234',
    database='bdyoutube'
)

cursor = conexao.cursor()

comando = """INSERT INTO bdyoutube.Vendas
        (
            nome_produto,
            valor
        )
        VALUES
        (
            'shampoo anticaspa',
            90.5
        );
    """

cursor.execute(comando)

conexao.commit()
# Fechar cursor e conexão
cursor.close()
conexao.close()