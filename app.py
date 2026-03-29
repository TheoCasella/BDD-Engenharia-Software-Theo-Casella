from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados de livros (Model)
livros_db = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "preco": 45.90},
    {"id": 2, "titulo": "Memórias Postumas", "autor": "Machado de Assis", "preco": 39.90},
    {"id": 3, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "preco": 35.00}
]


@app.route('/')
def index():
    """Rota principal que serve o Front-end"""
    return render_template('index.html')


@app.route('/api/buscar', methods=['GET'])
def buscar_livro():
    """API de busca para validar a User Story de pesquisa"""
    query = request.args.get('q', '').lower()

    if not query:
        return jsonify(livros_db)

    resultados = [l for l in livros_db if query in l['titulo'].lower() or query in l['autor'].lower()]
    return jsonify(resultados)


@app.route('/api/checkout', methods=['POST'])
def checkout():
    """Simulação do endpoint de pagamento via QR Code"""
    # Aqui entraria a lógica de integração com gateway de pagamento
    return jsonify({"status": "sucesso", "mensagem": "Pagamento processado via QR Code!"})


if __name__ == '__main__':
    # Roda o servidor localmente
    app.run(debug=True)