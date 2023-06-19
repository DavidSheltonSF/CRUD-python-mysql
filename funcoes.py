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
