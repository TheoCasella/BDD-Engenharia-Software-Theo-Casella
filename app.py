from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Contém os livros citados no seu Storyboard e nos testes BDD
livros_db = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "preco": 45.90},
    {"id": 2, "titulo": "Memórias Postumas", "autor": "Machado de Assis", "preco": 39.90},
    {"id": 3, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "preco": 35.00},
    {"id": 4, "titulo": "Quincas Borba", "autor": "Machado de Assis", "preco": 42.00}
]


# 2. Rota Principal (View Control)
@app.route('/')
def index():
    """Renderiza a página inicial (HTML)"""
    return render_template('index.html')


# 3. API de Busca Detalhada (Controller)
@app.route('/api/buscar', methods=['GET'])
def buscar_livro():
    """
    Filtra os livros por título ou autor.
    Usado tanto pelo JavaScript do front-end quanto pelo Behave (BDD).
    """
    query = request.args.get('q', '').lower()

    # Se não houver busca, retorna todos os livros
    if not query:
        return jsonify(livros_db)

    # Lógica de busca detalhada (ignora maiúsculas/minúsculas)
    resultados = [
        livro for livro in livros_db
        if query in livro['titulo'].lower() or query in livro['autor'].lower()
    ]

    return jsonify(resultados)


# 4. API de Checkout (Simulação de Pagamento)
@app.route('/api/checkout', methods=['POST'])
def checkout():
    """Simula o processamento do QR Code de pagamento"""
    return jsonify({
        "status": "sucesso",
        "mensagem": "Pagamento via QR Code processado!",
        "codigo_pix": "00020126360014BR.GOV.BCB.PIX..."
    })


if __name__ == '__main__':
    # Roda o servidor no modo Debug para facilitar o desenvolvimento
    app.run(debug=True)