import sqlite3

#criar banco:
banco_de_dados = sqlite3.connect("banco_de_dados")

#criando cursosr, permite entrada dos codigos SQL:
cursor = banco_de_dados.cursor()

#criando primeira tabela dentro de "banco_de_dados":
#Não usar o comando create table mais de uma vez...
#cursor.execute("CREATE TABLE CLIENTES ('NOME VARCHAR (100)', 'SEXO CHAR (1)','IDADE VARCHAR (3)','ENDERECO VARCHAR (100)');")


#inserindo valor no banco:
#cursor.execute("INSERT INTO CLIENTES VALUES ('Guilherme da Silva Pessoa Lucas', 'M', '20', 'Terminal rodoviario de Barueri')")


#criando variaveis de entrada
NOME_ENTRADA = input("Digite seu nome: ")
SEXO_ENTRADA = input("Digite seu sexo com M para (Masculino) ou F para (Feminino): ")
IDADE_ENTRADA = input("Digite sua idade: ")
ENDERECO_ENTRADA = input("Digite seu Endereço: ")

#inseindo dados no banco com variavel:
cursor.execute("INSERT INTO CLIENTES VALUES ('"+NOME_ENTRADA+"', '"+SEXO_ENTRADA+"', '"+IDADE_ENTRADA+"', '"+ENDERECO_ENTRADA+"') ")



cursor.execute("SELECT * FROM CLIENTES")
print(cursor.fetchall())

banco_de_dados.commit()