#Importando o flask para podermos usar no nosso programa
from flask import Flask

#Vamos criar uma variavel (nesse caso, um objeto) para representar nossa aplicação web
app = Flask(__name__)

#Vamos criar uma rota para acessar o servidor
@app.route("/")
#Ao acessar essa rota a função abaixo é executada e ela devolve o texto "deu certo!""
def exibir_mensagem():
    return "Deu certo!"

#A linha abaixo executa a aplicação web que foi criada a partir do flask
app.run(debug=True)


