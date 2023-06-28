# Para que o código funcionasse sem erros eu precisei criar um novo usuário:
"""
DROP USER 'userdavid';
CREATE USER 'userdavid'@'%' IDENTIFIED 
WITH mysql_native_password  BY '1234';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, 
RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, 
CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, 
REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, 
CREATE USER, EVENT, TRIGGER ON *.* TO 'userdavid'@'%' WITH GRANT OPTION;
"""

def email_existe(email) -> bool:
    import mysql.connector

    # Inicia a conexão
    conexao = mysql.connector.connect(
        host ='localhost',
        user='root',
        password='1234',
        database='bdclientes'
    )

    cursor = conexao.cursor()
    
    comando = f"""
    SELECT *
        FROM bdclientes.clientes
        WHERE email = '{email}';
        """

    cursor.execute(comando)
    resposta = cursor.fetchall()

    cursor.close()
    conexao.close()

    # Se houver resposta
    # Listas vazias equivalem a False
    if  resposta:
        return True
    # Senão
    else:
        return False
    

def cadastrar(nome, email, senha):
    import mysql.connector

    # Se o email não existe
    if not email_existe(email):

        # Tente
        try:

            # Inicia a conexão
            conexao = mysql.connector.connect(
                host ='localhost',
                user='root',
                password='1234',
                database='bdclientes'
            )

            cursor = conexao.cursor()

            # Comando SQL para inserir usuário na tabela
            comando = f"""INSERT INTO bdclientes.clientes
                    (
                        nome,
                        email,
                        senha
                    )
                    VALUES
                    (
                        '{nome}',
                        '{email}',
                        '{senha}'
                    );
                """
            # Executa o comando
            cursor.execute(comando)
            # Salva as alterações no banco
            conexao.commit()
            # Fechar cursor e conexão
            cursor.close()
            conexao.close()
        # Se der erro
        except:
            print('ERRO! Usuário não cadastrado!')
        # Senão
        else:
            print("Usuário cadastrado com SUCESSO!")
    # Senão, se o email já existe
    else:
        print("Este email já existe!")


def logar(email, senha):
    import mysql.connector

    # Inicia a conexão
    conexao = mysql.connector.connect(
        host ='localhost',
        user='root',
        password='1234',
        database='bdclientes'
    )

    cursor = conexao.cursor()

    comando = f"""
    SELECT *
        FROM bdclientes.clientes
        WHERE email = '{email}'
        AND senha = '{senha}';
        """

    cursor.execute(comando)
    resposta = cursor.fetchall()
    
    # Se houver resposta
    # Listas vazias equivalem a False
    if  resposta:
        print(resposta)
    # Senão
    else:
        print('Email ou senha incorretos!')
    
    cursor.close()
    conexao.close()

email_existe("dav@gmail.com")