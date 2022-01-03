# PWEB 2

Projeto para a matéria de programação web 2 do IFAL.


## Como usar
**Requisitos:** 

 - Python 3.8.10 ou superior
 - Git
 
**Configurando o ambiente**

Abra o terminal e clone o repositório:

``` git clone https://github.com/fernandogfleite/pweb2.git ```

Entre na pasta do repositório:
``` cd pweb2 ```

Instale a virtualenv:
``` python -m pip install virtualenv ```

Vá até o terminal de comando e crie uma virtualenv:

``` python -m venv venv ```

Após isso ative a sua virtualenv:
 - Linux: ```source venv/bin/activate```
 - Windows: ```.\venv\Scripts\activate.bat```

Após ativar a sua virtualenv, instale os requirements.txt:
```pip install -r requirements.txt```

Rode as migrations:

```python manage.py migrate```

Após isso a aplicação está pronta para rodar:

```python manage.py runserver```

Vá no seu navegador e acesse 127.0.0.1:8000 ou localhost:8000
