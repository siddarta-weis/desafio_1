A máquina utilizada deve ter python 3, de preferência 3.8, pois foi testado neste

Para rodar o projeto é necessário ter o pip do python 3
    pip install python3-pip

Deve-se instalar pacote para criar virtual environments 
    sudo apt install python3-venv

Em seguida, criar o virtual environment
    python3 -m venv venv

Ativar o virtual environment
    source venv/bin/activate

Clonar projeto
    git clone <url>

Instalar requirements
    pip3 install -r requirements.txt

Rodar o serviço 
    python3 manage.py runserver 