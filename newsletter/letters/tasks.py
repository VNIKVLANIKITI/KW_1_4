from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import random
from django.apps import apps
from django.utils import timezone


def send_email(param1, param2, param3, param4):
    MailingAttempt = apps.get_model('letters', 'MailingAttempt')

    # Логика отправки email
    print(f"Адресат: {param1}, тема {param4} , сообщение: {param2}")

    feedback = send_yandex_email (param1, param2, param4) #random.choice([True, False]) #def send_yandex_email(recipient_email, subject, message):

    # Создание записи для MailingAttempt
    mailing_attempt = MailingAttempt(
        attempt_time = timezone.now(),
        status='successful' if feedback else 'failed',
        server_response='ok'
    )
    mailing_attempt.save()
    # Добавим +1 к попыткам данной рассылки
    MailingModel = apps.get_model('letters', 'Mailing')
    mailing = MailingModel.objects.get(id=param3)
    
    # Добавление новой попытки в связь ManyToMany
    mailing.attemtps.add(mailing_attempt)
    
    mailing.save()
    return feedback

   
def add_mytask(id, periodicity, customer_emails, message, subject):
    scheduler = BackgroundScheduler(timezone='Europe/Moscow')
    # Логика для добавления задачи
    print(f"Задача добавлена для рассылки: {id} с периодичностью: {periodicity}, "
          f"email-адресами клиентов: {customer_emails}, и сообщением: {message}")
    # Добаввим задачу на рассылку в зависимости от периодичности
    if periodicity == 'daily':
        trigger = CronTrigger(day='*', hour='8', minute='0')
    if periodicity == 'weekly':
        trigger = CronTrigger(day_of_week='sat', hour='12', minute='0')
    if periodicity == 'monthly':
        trigger = CronTrigger(day='1', hour='12', minute='0')
    if trigger == None:
        from datetime import datetime
        trigger = datetime.now  # Задайте нужную дату и время
    for e in customer_emails:
        scheduler.add_job(send_email, trigger=trigger, args=[e, subject, id, message])
    scheduler.start()

#Отправку сообщений рассылок необходимо осуществлять через smtp сервер, например yandex
from django.core.mail import send_mail
from django.conf import settings

def send_yandex_email(recipient_email, subject, message):
    from_email = settings.DEFAULT_FROM_EMAIL  # Используем адрес из настроек

    try:
        send_mail(
            subject,
            message,
            from_email,
            [recipient_email],
            fail_silently=False,
        )
        print(f'Письмо успешно отправлено на {recipient_email}')
        return True
    except Exception as e:
        print(f'Ошибка при отправке письма: {e}')
        return False
