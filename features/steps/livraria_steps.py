from behave import given, when, then
import requests

# Verifica se o servidor Flask está ligado
@given('que eu acesso a página inicial da livraria')
def step_impl(context):
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200

@when('eu digito "{texto}" no campo de busca')
def step_impl(context, texto):
    context.busca_termo = texto

@when('clico no botão de buscar')
def step_impl(context):
    # Simula a busca chamando a API que você criou no app.py
    response = requests.get(f"http://127.0.0.1:5000/api/buscar?q={context.busca_termo}")
    context.response_data = response.json()

@then('eu devo ver o livro "{titulo}" nos resultados')
def step_impl(context, titulo):
    # Verifica se o livro retornado é o que esperávamos
    titulos = [livro['titulo'] for livro in context.response_data]
    assert titulo in titulos

@when('eu clico no botão "Comprar"')
def step_impl(context):
    context.comprou = True

@then('a seção de "Pagamento via QR Code" deve aparecer')
def step_impl(context):
    assert context.comprou is True

@then('eu devo ver o livro "{titulo}" nos resultados')
def step_impl(context, titulo):
    # O context.response_data vem da chamada API feita no @when('clico no botão de buscar')
    titulos_encontrados = [livro['titulo'] for livro in context.response_data]
    assert titulo in titulos_encontrados, f"Esperava encontrar '{titulo}', mas os resultados foram: {titulos_encontrados}"