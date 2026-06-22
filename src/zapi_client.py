import os
import requests
from src.contato import Contato

class ZapiClient:
    
    def __init__(self):
        self.instance_id = os.getenv("ZAPI_INSTANCE_ID")
        self.token = os.getenv("ZAPI_TOKEN")

        self.url = f"https://api.z-api.io/instances/{self.instance_id}/token/{self.token}/send-text"

    def enviar_mensagem(self, contato: Contato, texto: str):
        dados = {
            "phone": contato.telefone,
            "message": texto
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            print(f"enviando mensagem para {contato.nome} ({contato.telefone})")
            
            resposta = requests.post(self.url, json=dados, headers=headers)

            if resposta.status_code == 200:
                print("mensagem enviada")
            else:
                # retorna o erro
                print(f"Erro ZAPI: codigo {resposta.status_code} - {resposta.text}")
                return False
        
        except Exception as erro:
            print(f"Não foi possível conectar ao ZAPI: {erro}")
            return False