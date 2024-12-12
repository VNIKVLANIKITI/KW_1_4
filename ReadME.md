В данном репозитории содержится Курсовой проект на тему сераиса рассылок
Требования:
1) список рассылок, отчет проведенных рассылок отдельно, создание рассылки, удаление рассылки,
2) создание пользователя, удаление пользователя, редактирование пользователя.
3) логика работы системы:
- После создания новой рассылки, если текущие дата и время больше даты и времени начала и меньше даты и времени окончания, должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки и запущена отправка для всех этих клиентов.
- Если создается рассылка с временем старта в будущем, отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя сервиса.
- По ходу отправки рассылки должна собираться статистика (см. описание сущностей «Рассылка» и «Попытка» выше) по каждой рассылке для последующего формирования отчетов. Попытка создается одна для одной рассылки. Формировать попытки рассылки для всех клиентов отдельно не нужно.
- Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.
4) Интерфейс понятен и соответствует базовым требованиям системы.
5) Все интерфейсы для изменения и создания сущностей, не относящиеся к стандартной админке, реализовали с помощью Django-форм.
6) Все настройки прав доступа реализовали верно.
7) Приложены фикстуры или созданы команды для заполнения базы данных

!!!!!!Отработка замечаний (3 итерация) !!!!!:
[x] 1) Корректно собран шаблон файла .env. = Все еще не полный шаблон для переменных окружения, необходимо перенести все переменные из файла env, который ты используешь для запуска приложения.
[x] 2) На главной странице выводится необходимая информация по ТЗ.
[x] 3) В шаблон главной страницы передается контекст с необходимыми данными по ТЗ.
[x] 4) Шаблон главной страницы отображает данные корректно. = По ТЗ на главной странице должны отображаться показатели количества рассылок всего, уникальных клиентов и количество запущенный рассылок.
[х] 5) И сейчас при запуске рассылки через интерфейс приложение падает с ошибкой (во вложении) 