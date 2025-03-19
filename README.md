# 📈 InvestMap - Gerenciador de Investimentos

O **InvestMap** é uma plataforma web desenvolvida com **Flask** para gerenciamento de investimentos, permitindo o acompanhamento de ativos, cotações em tempo real, gráficos interativos, notícias financeiras e exportação de dados em **CSV e PDF**.

---

## 🚀 Funcionalidades

✅ **Cadastro e gerenciamento de investimentos**
✅ **Cotações em tempo real (Yahoo Finance)**
✅ **Gráficos interativos (Chart.js)**
✅ **Modo escuro e design moderno (Tailwind CSS)**
✅ **Notícias financeiras em tempo real (NewsAPI)**
✅ **Exportação de dados em CSV e PDF**

---

## 🛠️ Tecnologias Utilizadas

- **Python** + **Flask** (Backend)
- **SQLite** (Banco de Dados)
- **Chart.js** (Gráficos interativos)
- **Tailwind CSS** (Estilização moderna)
- **yFinance** (Cotações em tempo real)
- **NewsAPI** (Notícias financeiras)
- **FPDF** (Geração de PDF)
- **CSV** (Exportação de dados)

---

## 📥 Instalação e Execução

1️⃣ Clone o repositório:
```bash
git clone https://github.com/seuusuario/InvestMap.git
cd InvestMap
```

2️⃣ Crie um ambiente virtual e ative:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

4️⃣ Execute o projeto:
```bash
python app.py
```

🔗 Acesse no navegador: **http://127.0.0.1:5000/**

---

## 📁 Estrutura do Projeto
```
InvestMap/
│── static/                  # Arquivos estáticos (CSS, JS, imagens)
│── templates/               # Templates HTML
│   ├── index.html           # Página principal
│── app.py                   # Código principal Flask
│── investmap.db             # Banco de dados SQLite
│── requirements.txt         # Dependências do projeto
│── README.md                # Documentação do projeto
```

---

## 📄 API Keys Necessárias
O projeto usa **NewsAPI** para buscar notícias financeiras e **yFinance** para cotações em tempo real. Substitua sua **API Key** no arquivo `app.py`:
```python
apiKey = "SUA_API_KEY_AQUI"  # Substitua pela sua chave NewsAPI
```
Você pode obter uma chave gratuita em [NewsAPI](https://newsapi.org/).

---

## 📤 Exportação de Dados
- **CSV**: Clique no botão "📄 Exportar CSV" para baixar um arquivo `.csv` com os investimentos.
- **PDF**: Clique no botão "🖨️ Exportar PDF" para gerar um relatório formatado.

---

## 🛠️ Melhorias Futuras
🚀 **Histórico de preços dos ativos** 📊  
🚀 **Alertas de volatilidade do mercado** 🔔  
🚀 **Metas de investimento** 🎯  
🚀 **Autenticação de usuários (login)** 🔐  

---

## 📜 Licença
Este projeto é de código aberto e pode ser utilizado para fins educacionais e de aprendizado.

---

💡 **Criado por Gabriel Felipe Santana & Akira 🤖** - Sinta-se à vontade para contribuir! 😊

