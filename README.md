# Desafio B2BFlow - Envio Automatizado de Mensagens

Este projeto consiste em um script em Python desenvolvido para integrar o banco de dados Supabase com a API de WhatsApp Z-API. O sistema realiza a busca de contatos cadastrados em uma tabela, limita a quantidade de registros conforme a regra de negócio e dispara mensagens personalizadas de forma sequencial.

## Estrutura de Arquivos

* src/contato.py: Representação do modelo de dados (Classe Contato).
* src/db_client.py: Conexão com o Supabase e consulta de registros.
* src/zapi_client.py: Integração com a Z-API para envio de mensagens via HTTP POST.
* main.py: Arquivo central responsável por orquestrar a execução do fluxo.

## Pré-requisitos

* Python 3.8 ou superior

## Instalação e Configuração

1. Crie o ambiente virtual na raiz do projeto:

   python -m venv venv

2. Ative o ambiente virtual:

   No Windows (PowerShell):
   .\venv\Scripts\activate

   No Windows (CMD):
   venv\Scripts\activate

   No Linux/Mac:
   source venv/bin/activate

3. Instale as bibliotecas necessárias listadas no arquivo de dependências:

   pip install -r requirements.txt

## Configuração do Banco de Dados

Para estruturar o banco de dados no Supabase, acesse o painel do seu projeto, vá em **SQL Editor** e execute o seguinte comando para criar a tabela necessária:

```sql
create table contatos (
    id bigint generated always as identity primary key,
    created_at timestamp with time zone default now() not null,
    nome text not null,
    telefone text not null
);

-- Exemplo de inserção de dados para teste:
insert into contatos (nome, telefone) 
values ('Marco Antônio', '5532xxxxxxxxx');
```

## Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para gerenciar credenciais sensíveis de forma segura. Crie um arquivo nomeado `.env` na raiz do diretório e preencha as chaves conforme o modelo abaixo:

SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-api-legacy-anon
ZAPI_INSTANCE_ID=seu-id-de-instancia
ZAPI_TOKEN=seu-token-da-instancia

## Execução

Após configurar as variáveis de ambiente e com as dependências instaladas, execute o script principal através do terminal:

python main.py
