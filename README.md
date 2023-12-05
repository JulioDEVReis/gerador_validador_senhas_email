# gerador_validador_senhas_email
Funcionalidade em Registo de usuários da opção para gerar Senhas Fortes e validar o email e senha colocados pelo usuário

![Captura de tela 2023-12-03 002325](https://github.com/JulioDEVReis/gerador_validador_senhas_email/assets/142347463/418d78cd-92d9-4e08-8cb0-422f33fded90)

Criei a parte do aplicativo desktop, voltada apenas para autenticação e registo de usuários, com geração de senhas fortes, validação de senhas e email, e criptografia de senhas para envio ao banco de dados SQL.

A idéia era verificar o tempo gasto para criar essas funcionalidades num aplicativo desktop.

Criei então as funções de validação de email, usando a biblioteca validate_email_address e de validação de senha, usando a biblioteca de expressões regulares (re) para verificar se o email está no padrão e se a senha possui tamanho e os caracteres exigidos.

![Captura de tela 2023-12-03 002405](https://github.com/JulioDEVReis/gerador_validador_senhas_email/assets/142347463/f86c0470-576d-4188-b63f-5a33eab9cff7)

Na função de criação de registos dos usuários novos, criei funções para gerar senha automaticamente, respeitando as condições exigidas para a criação da senha, com uso das bibliotecas string e random. Além disso criei a funcionalidade de exibição dos caracteres da senha ao clicar no ícone no lado direito do campo de digitação da senha.

Não poderia deixar de cria uma função para criptografar a senha para envio ao banco de dados SQL (Hash da senha). Usei a biblioteca bcrypt para isso.

## Dificuldades e Soluções:

Meu maior problema foi utilizar o Custom Tkinter, a qual descobri que não possui todas as funcionalidades do Tkinter. Depois de estudar bastante sua documentação e ver vários exemplos no GitHub da sua aplicação, tive que instalar, por exemplo, uma biblioteca para poder ter a funcionalidade de exibir uma janela separada com a mensagem de erro sobre a validação do email ou da senha, por exemplo. Em aplicações futuras, não utilizarei mais essa biblioteca.

## Tecnologias usadas:

- Random (usada para sugerir os caracteres para a funcionalidade da geração de senha)
- Re (expressões regulares, usadas no processo de validação da senha colocada pelo usuário)
- Sqlite3 (biblioteca que usamos para manipular nosso banco de dados SQL)
- String (usada para gerar os caracteres da senha forte)
- Bcrypt (usada para criptografar a senha do usuário no envio para o Banco de dados)
- Custom Tkinter (Framework escolhido para a criação do app desktop, mais estilizada que o Tkinter)
- CTK Message Box (usada para gerar caixas de mensagens suspensas, não existentes no Custom Tkinter)
- Validate Email Address (usada para validar a estrutura de email digitada pelo usuario)
