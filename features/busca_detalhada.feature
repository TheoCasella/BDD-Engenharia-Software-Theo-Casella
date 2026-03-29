 #language: pt
Funcionalidade: Busca Detalhada de Livros
  Como um leitor que procura obras específicas
  Quero buscar por título ou autor
  Para encontrar exatamente o que desejo ler

  Cenário: Buscar livro por título existente
    Dado que eu acesso a página inicial da livraria
    Quando eu digito "O Cortiço" no campo de busca
    E clico no botão de buscar
    Então eu devo ver o livro "O Cortiço" nos resultados

  Cenário: Buscar livros de um autor específico
    Dado que eu acesso a página inicial da livraria
    Quando eu digito "Machado de Assis" no campo de busca
    E clico no botão de buscar
    Então eu devo ver o livro "Dom Casmurro" nos resultados
    E eu devo ver o livro "Memórias Postumas" nos resultados