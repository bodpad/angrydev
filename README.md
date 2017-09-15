### Развертывание и запуск

    git clone https://github.com/bodpad/angrydev.git
    cd angrydev
    
    # Устанавливаем виртуальное окружение
    # и все необходимые для работы пакеты
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    # Запускаем сервер
    python3 server.py dictionary.txt 5000
    
    # Запускаем клиент
    python3 client.py 127.0.0.1 5000
