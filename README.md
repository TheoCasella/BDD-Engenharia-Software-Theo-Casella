# 📚 Livraria Digital MVP - Engenharia de Software

Este repositório contém o MVP de um aplicativo de livraria digital, desenvolvido com foco em **BDD (Behavior-Driven Development)** e **Desenvolvimento Top-Down**. O projeto integra uma interface moderna inspirada no Figma, um backend funcional em Python (Flask) e testes de comportamento automatizados (Behave).

## 🚀 Metodologia Aplicada: Top-Down & BDD

O desenvolvimento seguiu o fluxo de Engenharia de Software para garantir o alinhamento entre requisitos e código:
1.  **Nível Estratégico (UX/UI):** Design e mapeamento de User Stories no Figma.
2.  **Nível Tático (BDD):** Escrita de cenários em Gherkin para definir critérios de aceitação.
3.  **Nível Operacional (Código):** Implementação do front-end (HTML/Tailwind) e backend (Flask/Python).

## 🎯 Funcionalidades do MVP

O protótipo demonstra o ciclo essencial de interação do usuário:

### 🔍 Busca Detalhada (Implementada via BDD)
* **Busca por Título:** Localização imediata de obras específicas.
* **Busca por Autor:** Filtragem dinâmica que agrupa múltiplos títulos de um mesmo escritor.
* **Feedback em Tempo Real:** Atualização dinâmica da vitrine de livros via API.

### 🛒 Checkout e Pagamento
* **Fluxo de Compra:** Seleção de itens diretamente da busca.
* **PIX:** Geração de QR Code para simulação de pagamento instantâneo.
* **Interface Responsiva:** Design limpo e focado na conversão (compra).

### 🛡️ Interações Adicionais (Mapeadas no Storyboard)
* **Favoritos:** Sistema para favoritar livros (UX Simulada).
* **Catálogo:** Organização de livros por preço e autoria.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Web Framework:** Flask (Backend e APIs)
* **Front-end:** HTML5, Tailwind CSS
* **BDD Framework:** Behave (Gherkin)
* **Testes de Integração:** Requests

## 📂 Estrutura do Repositório

```text
├── app.py                # Servidor Flask e APIs de Busca/Checkout
├── templates/            # Interface Visual (HTML)
├── static/               # Estilização Personalizada (CSS)
├── features/             # Especificações BDD (Arquivos .feature)
│   └── steps/            # Implementação Python dos Testes
└── STORYBOARD.md         # Documentação de Telas e User Stories

# 🏁 Como Executar o Projeto

## 1. 📌 Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

---

## 2. 📦 Instalação das Dependências

No terminal do projeto, instale os pacotes necessários utilizando o gerenciador **pip**:

```bash
pip install flask behave requests
```

---

## 3. 🚀 Iniciar o Servidor

Execute o comando abaixo para rodar a aplicação:

```bash
python app.py
```

> **Nota:** O app estará disponível em:
> http://127.0.0.1:5000

---

## 4. 🧪 Rodar os Testes BDD

Mantenha o servidor rodando no primeiro terminal.
Em seguida, abra um segundo terminal e execute:

```bash
behave
```

---

## 👨‍💻 Autor

**Theo Casella**

## 🎓 Projeto

**Engenharia de Software - BDD Exercise**
