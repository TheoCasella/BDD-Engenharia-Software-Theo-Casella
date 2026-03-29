# language: pt
Funcionalidade: Fluxo de Compra no MVP
  Como um leitor que não gosta de filas
  Quero buscar um livro e pagar via QR Code
  Para ter uma experiência de compra rápida

  Cenário: Buscar um livro e abrir o checkout
    Dado que eu acesso a página inicial da livraria
    Quando eu digito "Dom Casmurro" no campo de busca
    E clico no botão de buscar
    Então eu devo ver o livro "Dom Casmurro" nos resultados
    Quando eu clico no botão "Comprar"
    Então a seção de "Pagamento via QR Code" deve aparecer