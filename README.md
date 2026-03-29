# 📚 Livraria Digital MVP - Engenharia de Software

Este repositório contém o MVP de um aplicativo de livraria digital, desenvolvido como parte do exercício de BDD e Desenvolvimento Top-Down. O projeto integra uma interface moderna (inspirada no Figma), um backend funcional em Python (Flask) e testes de comportamento automatizados (Behave).

## 🚀 Metodologia Aplicada: Top-Down & BDD

O desenvolvimento seguiu o fluxo **Top-Down**, garantindo que a implementação técnica estivesse sempre alinhada à experiência do usuário:
1.  **Nível Estratégico (UX/UI):** Design e mapeamento de User Stories no Figma.
2.  **Nível Tático (BDD):** Escrita de cenários em Gherkin para definir o comportamento esperado.
3.  **Nível Operacional (Código):** Implementação do front-end (HTML/Tailwind) e backend (Flask/Python).

## 🎯 Funcionalidades Implementadas (User Stories)

O protótipo demonstra o ciclo completo de compra e interação:

### 🔍 Catálogo e Busca
* **Busca Global:** Procura de livros por título, autor ou editora no header.
* **Visualização:** Catálogo completo com detalhes de preço e autor.
* **Filtros:** Sistema de filtragem por gênero e categorias.

### 🛒 Checkout e Pagamentos (Foco do MVP)
* **PIX:** Geração de QR Code para pagamento instantâneo.
* **Cartões:** Simulação de cadastro de cartões de crédito e débito com suporte a parcelamento em até 12x.
* **Fidelidade:** Sistema de acúmulo de pontos em compras no débito.

### 🛡️ Segurança e Interação
* **Confirmação:** Validação de transações via código SMS simulado.
* **Favoritos:** Sistema para favoritar e remover livros da lista de desejos.
* **Feedback:** Avaliações de outros leitores e feedback sobre recomendações.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Web Framework:** Flask (Backend e Rotas)
* **Front-end:** HTML5, Tailwind CSS (Design via CDN)
* **BDD Framework:** Behave (Gherkin)
* **Automação de Testes:** Requests / Selenium

## 📂 Estrutura do Projeto

```text
├── app.py                # Servidor Flask e APIs do sistema
├── templates/            # Front-end (HTML)
├── static/               # Estilização (CSS)
├── features/             # Especificações BDD (Gherkin)
│   └── steps/            # Implementação Python dos testes
└── STORYBOARD.md         # Mapeamento detalhado de telas e fluxos
