from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import yfinance as yf  # Importando a biblioteca para buscar preços em tempo real
import requests  # Para buscar as notícias financeiras
import csv
from fpdf import FPDF
from flask import Response

# Inicializa o app Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investmap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para armazenar investimentos
class Investimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    preco_compra = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_compra = db.Column(db.Date, default=datetime.date.today)

# Função para buscar a cotação atual de um ativo
def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.history(period="1d")["Close"].iloc[-1]  # Último preço de fechamento
    except:
        return None

# Função para buscar notícias financeiras
def get_financial_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": "business",
        "language": "en",  # Alterando para inglês
        "apiKey": "COLOCA_SUA_KEY"
    }
    response = requests.get(url, params=params)
    
    print("Status da API:", response.status_code)  # Verifica se a requisição deu certo
    print("Dados recebidos:", response.json())  # Exibe os dados recebidos no terminal

    if response.status_code == 200:
        return response.json().get("articles", [])
    return []

# Rota principal - exibir investimentos, buscar preços e notícias atualizadas
@app.route('/')
def index():
    investimentos = Investimento.query.all()
    noticias = get_financial_news()  # Buscar notícias financeiras

    labels = []
    valores = []
    precos_atuais = {}

    for investimento in investimentos:
        labels.append(investimento.nome)
        total_investido = round(investimento.preco_compra * investimento.quantidade, 2)
        valores.append(total_investido)

        preco_atual = get_stock_price(investimento.ticker)
        if preco_atual:
            precos_atuais[investimento.ticker] = preco_atual

    return render_template('index.html', investimentos=investimentos, labels=labels, valores=valores, precos_atuais=precos_atuais, noticias=noticias)

# Rota para adicionar um novo investimento
@app.route('/add', methods=['POST'])
def add_investimento():
    nome = request.form['nome']
    ticker = request.form['ticker']
    preco_compra = float(request.form['preco_compra'])
    quantidade = int(request.form['quantidade'])
    
    novo_investimento = Investimento(nome=nome, ticker=ticker, preco_compra=preco_compra, quantidade=quantidade)
    db.session.add(novo_investimento)
    db.session.commit()
    
    return redirect(url_for('index'))

# Rota para editar um investimento
@app.route('/edit/<int:id>', methods=['POST'])
def edit_investimento(id):
    investimento = Investimento.query.get_or_404(id)
    investimento.nome = request.form['nome']
    investimento.ticker = request.form['ticker']
    investimento.preco_compra = float(request.form['preco_compra'])
    investimento.quantidade = int(request.form['quantidade'])
    
    db.session.commit()
    return redirect(url_for('index'))

# Rota para excluir um investimento
@app.route('/delete/<int:id>')
def delete_investimento(id):
    investimento = Investimento.query.get_or_404(id)
    db.session.delete(investimento)
    db.session.commit()
    return redirect(url_for('index'))

# Função para exportar investimentos para CSV
@app.route('/export/csv')
def export_csv():
    investimentos = Investimento.query.all()

    # Criar o arquivo CSV em memória
    csv_data = "Nome,Ticker,Preço de Compra,Quantidade,Data de Compra\n"
    for investimento in investimentos:
        csv_data += f"{investimento.nome},{investimento.ticker},{investimento.preco_compra},{investimento.quantidade},{investimento.data_compra}\n"

    response = Response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=investimentos.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

# Função para exportar investimentos para PDF
@app.route('/export/pdf')
def export_pdf():
    investimentos = Investimento.query.all()

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Relatório de Investimentos", ln=True, align="C")

    pdf.set_font("Arial", "B", 12)
    pdf.cell(40, 10, "Nome", 1)
    pdf.cell(30, 10, "Ticker", 1)
    pdf.cell(40, 10, "Preço", 1)
    pdf.cell(30, 10, "Qtd", 1)
    pdf.cell(40, 10, "Data", 1)
    pdf.ln()

    pdf.set_font("Arial", "", 12)
    for investimento in investimentos:
        pdf.cell(40, 10, investimento.nome, 1)
        pdf.cell(30, 10, investimento.ticker, 1)
        pdf.cell(40, 10, str(investimento.preco_compra), 1)
        pdf.cell(30, 10, str(investimento.quantidade), 1)
        pdf.cell(40, 10, str(investimento.data_compra), 1)
        pdf.ln()

    response = Response(pdf.output(dest="S").encode("latin1"))
    response.headers["Content-Disposition"] = "attachment; filename=investimentos.pdf"
    response.headers["Content-Type"] = "application/pdf"
    return response


# Executar a aplicação
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
