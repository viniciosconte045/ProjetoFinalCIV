 Sistema de Gestão Escolar

Desenvolvido por: Vinicios, Igor e Cecília



 Objetivo do Sistema

O Sistema de Gestão Escolar foi desenvolvido em Python com o objetivo de facilitar o gerenciamento de alunos e notas escolares. O projeto aplica os conhecimentos adquiridos nas disciplinas de Desenvolvimento de Algoritmos, Requisitos e Banco de Dados, utilizando o MySQL para armazenamento permanente das informações.


 Banco de Dados

O banco de dados foi desenvolvido utilizando MySQL e é responsável por armazenar todas as informações do sistema.

Foram criadas as seguintes tabelas:

Usuários: armazena nome de usuário, senha e tipo de acesso.
Alunos: armazena nome, idade e turma dos estudantes.
Professores: registra informações dos professores e suas disciplinas.
Notas: registra as notas lançadas para cada aluno.

O sistema cria automaticamente o banco de dados, as tabelas e os usuários padrões na primeira execução, caso ainda não existam.

Todas as informações permanecem salvas no banco de dados, permitindo que sejam acessadas novamente sempre que o sistema for utilizado.



 Sistema de Login

O login é a primeira etapa do sistema.

O usuário informa seu nome de usuário e senha para acessar o programa. O sistema verifica os dados informados e identifica o tipo de usuário.

Existem dois níveis de acesso:

 Administrador
 usuário: adm   
 senha: josefa

 
 Professor
 usuário: prof   
 senha: josealdo
 
Cada tipo de usuário possui permissões diferentes dentro do sistema.

Caso o usuário ou senha estejam incorretos, o acesso é negado e uma nova tentativa pode ser realizada.



 Como Utilizar o Sistema

Ao iniciar o programa, é exibido um menu principal com as opções:

* Fazer login;
* Encerrar o sistema.

Após realizar o login, o usuário deverá selecionar a turma que deseja acessar.

As turmas disponíveis são:

* 1º EM Desenvolvimento de Sistemas;
* 1º EM Multimídia;
* 1º EM Jogos Digitais;
* 2º EM Multimídia;
* 2º EM Jogos Digitais;
* 3º EM Jogos Digitais.

Depois da seleção da turma, o sistema apresenta o menu correspondente ao tipo de usuário.

Todas as operações realizadas ficam vinculadas à turma selecionada.



Funcionalidades do Administrador

O administrador é responsável pelo gerenciamento dos alunos.

Suas funções são:

 Cadastrar alunos;
 Listar alunos cadastrados;
 Editar informações dos alunos;
 Excluir alunos;
 Trocar de turma;
 Voltar ao menu de login.

Durante o cadastro são solicitados o nome e a idade do aluno.

O sistema realiza validações para impedir o cadastro de informações inválidas.

Na edição, é possível alterar o nome e a idade do aluno.

Antes de salvar as alterações, o sistema apresenta um resumo das modificações e solicita confirmação.

Na exclusão, são exibidos os dados do aluno selecionado e é solicitada uma confirmação antes da remoção definitiva.



Funcionalidades do Professor

O professor é responsável pelo gerenciamento das notas e pelo acompanhamento do desempenho dos alunos.

Suas funções são:

 Listar alunos da turma;
 Adicionar notas;
 Editar notas;
 Remover notas;
 Listar todas as notas cadastradas;
 Gerar o boletim geral da turma;
 Trocar de turma;
 Voltar ao menu de login.

Para adicionar uma nota, o professor seleciona o aluno pelo ID e informa uma nota entre 0 e 10.

Na edição, é possível alterar qualquer nota cadastrada.

Na remoção, o sistema apresenta as notas existentes do aluno e solicita confirmação antes da exclusão.

Também é possível visualizar todas as notas cadastradas de cada aluno da turma.



Boletim Geral

O sistema calcula automaticamente a média de cada aluno utilizando todas as notas cadastradas.

Além da média, é exibida a situação do aluno conforme os seguintes critérios:

Aprovado: média maior ou igual a 7,0.
Recuperação: média entre 5,0 e 6,9.
Reprovado: média inferior a 5,0.

Ao final, também é apresentada a média geral da turma.



 Validações do Sistema

Para garantir a integridade dos dados, o sistema realiza diversas validações, como:

Nome contendo apenas letras;
Idade maior que zero;
Nota entre 0 e 10;
Verificação da existência de alunos e notas antes de editar ou excluir;
Confirmação antes da exclusão de alunos e notas;
Validação de IDs informados pelo usuário.


Arquivos do Projeto

O repositório contém os seguintes arquivos:

`main.py`
`banco.py`
`login.py`
`menus.py`
`alunos.py`
`notas.py`
`README.md`



Como Executar

Execute o arquivo `main.py`.

Na primeira execução, o banco de dados e todas as tabelas serão criados automaticamente.
