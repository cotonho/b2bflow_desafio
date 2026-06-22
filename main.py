import os

from dotenv import load_dotenv

load_dotenv()

from src.db_client import DatabaseClient
from src.zapi_client import ZapiClient

def rodar_teste():
    print("rodando o teste")

    db = DatabaseClient()

    print("procurando contatos")
    lista = db.buscar_contatos(limite=3)
    
    print(f"contatos encontrados: {len(lista)}")

    for i, contato in enumerate(lista, start=1):
        print(f"contato: {i}")
        print(f"nome: {contato.nome}")
        print(f"telefone: {contato.telefone}\n")

def rodar():
    print("Iniciando...")
    zapi = ZapiClient()

    db = DatabaseClient()

    print("procurando contatos")
    contatos = db.buscar_contatos(limite=3)

    print(f"contatos encontrados: {len(contatos)}")

    print("enviando mensagens")

    for contato in contatos:
        # print(f"enviando mensagem para {contato.nome} ({contato.telefone})")
        
        mensagem = f"Olá, {contato.nome}, tudo bem com você?"

        zapi.enviar_mensagem(contato, mensagem)
        # print(f"mensagem enviada para {contato.nome} ({contato.telefone})")
        print("\n")

    print("Finalizando...")

if __name__ == "__main__":
    # rodar_teste()
    rodar()