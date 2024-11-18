DJANGO YANDEX DISK

Тестовое задание, выполненное мной для компании Mycego.

## 🚀 Функционал

- Django-приложение с настройками кеширования через Redis.
- Использование Docker и Docker Compose для запуска проекта.
- Разделение статических и медиафайлов в отдельные тома.

 ## 📋 Требования

Перед началом убедитесь, что на вашем компьютере установлены:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## 📦 Установка и запуск

1. **Склонируйте репозиторий**:

   ```
   git clone https://github.com/Ktulhu777/test_mycego.git
   cd test_mycego
   ```

2. **Добавьте в файл .env необходимые переменные окружения**:
```
  SECRET_KEY=your_secret_key
  YANDEX_TOKEN=your_yandex_token
```
  
3. **Запустите проект**:
```
  docker-compose up --build
```  

4. **Откройте приложение**:
```
  http://localhost:8000
```

