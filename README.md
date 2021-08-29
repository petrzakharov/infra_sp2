# Наше приложение будет строиться на основе контейнеров из 3х образов

1. Заранее подготовленный кастомный образ (загружен в docker hub, описан в Dockerfile)
2. Стандартный образ postgres:12.4 (загрузится из docker hub)
3. Стандартный образ nginx:1.19.3 (загрузится из docker hub)

## Начало работы

0. Убедитесь, что у вас установлен и запущен Docker
    % docker run ?????
1. Загрузите кастомный образ из docker hub с помощью команды:
    % docker pull zakharovp/yamdb:v.1
Или же соберите образ с помощью инструкций, размещенных в Dockerfile:
    % docker build -t yamdb:v.1 .
2. Собрать из образов контейнеры, которые описаны в файле конфига docker-compose.yaml.
В результате будут загружены еще 2 образа postgres:12.4 и nginx:1.19.3,
будут определены директории для хранения данных и прописан роутинг портов:
    % docker-compose up -d --build
3. Чтобы увидеть какие контейнеры в результате были запущены, наберите:
    docker ps

## Настройка приложения

Приложение стартовало в 3х контейнерах, теперь необходимо произвести миграции, создать суперпользователя(чтобы залогиниться, собрать статику и импортировать тестовые данные)
Эти команды мы будем выполнять из контейнера web (контейнер с Django приложением):
    % docker-compose exec web python manage.py makemigrations --noinput
    % docker-compose exec web python manage.py migrate --noinput
    % docker-compose exec web python manage.py createsuperuser
    % docker-compose exec web python manage.py collectstatic --no-input 
    % docker-compose exec web python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 2 > fixtures.json
Готово, можно перейти по адресу http://127.0.0.1/admin/ и залогиниться.

### Другие полезные команды

1. Остановка контейнеры
    % docker stop container_id
2. Удаление контейнера:
    % docker rm container_id
3. Остановка + отключения контейнера:
    % rm -f container_id
4. Посмотреть сохраненные образы:
    % docker image ls
5. Загрузить кастомный контейнер в Doker Hub (чтобы предоставить доступ):
    % docker push docker_id/proj_name:tag
6. Скачать кастомный контейнер из Docker Hub
    % docker pull docker_id/proj_name:tag
7. Остановить работу всех контейнеров
    % docker-compose down
