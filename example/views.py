# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Escola de Robôs</h1>
            <p>Atualizando o frontend...</p>
        </body>
    </html>
    '''
    return HttpResponse(html)