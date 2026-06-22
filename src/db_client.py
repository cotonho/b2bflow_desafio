import os
from supabase import create_client, Client
from src.contato import Contato

class DatabaseClient:
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        
        # cria conexão
        self.supabase: Client = create_client(url, key)

    def buscar_contatos(self, limite=3):
        contatos_encontrados = []
        try:
            # pega os dados
            resposta = self.supabase.table("contatos").select("nome, telefone").limit(limite).execute()
            
            # transforma em contato
            for item in resposta.data:
                novo_contato = Contato(nome=item['nome'], telefone=item['telefone'])
                contatos_encontrados.append(novo_contato)

        except Exception as erro:
            print(f"[ERRO SUPABASE] Falha ao buscar contatos: {erro}")
            
        return contatos_encontrados