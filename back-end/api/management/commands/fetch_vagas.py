# api/management/commands/fetch_vagas.py
from django.core.management.base import BaseCommand
from api.models import Vaga  # Vamos importar o nosso modelo Vaga
import requests  # Vamos importar o requests

class Command(BaseCommand):
    # Uma pequena ajuda/descrição para o nosso comando
    help = 'Busca vagas de APIs externas e salva no banco de dados'

    # A função principal que será executada
    def handle(self, *args, **options):
        # 1. Avisar que o comando começou
        self.stdout.write(self.style.SUCCESS('Iniciando a busca por vagas...'))
        
        # --- AQUI VAI A NOSSA LÓGICA ---
        # (Por enquanto, vamos apenas testar)
        
        url_teste = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url_teste)
        
        if response.status_code == 200:
            dados = response.json()
            titulo_teste = dados['title']
            
            # Imprime no terminal
            self.stdout.write(f"Título de teste buscado: {titulo_teste}")
        else:
            self.stdout.write(self.style.ERROR('Falha ao buscar dados de teste.'))

        # 2. Avisar que o comando terminou
        self.stdout.write(self.style.SUCCESS('Busca por vagas concluída.'))