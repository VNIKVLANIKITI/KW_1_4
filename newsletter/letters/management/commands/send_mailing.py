# myapp/management/commands/send_mailing.py

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from myapp.models import Mailing  # Импортируйте вашу модель Mailing
from myapp.tasks import send_email  # Импортируйте вашу функцию send_email

class Command(BaseCommand):
    help = 'Отправка рассылки сообщений'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID рассылки')

    def handle(self, *args, **options):
        pk = options['pk']
        current_mailing = get_object_or_404(Mailing.objects.prefetch_related('customers', 'messages'), id=pk)
        
        # Извлекаем email клиентов
        customer_emails = [customer.email for customer in current_mailing.customers.all()]
        
        # Извлекаем тело сообщения
        message_body = current_mailing.messages.body if current_mailing.messages else None
        
        # Рассылаем сообщения
        for email in customer_emails:
            send_email(email, message_body, pk)
        
        self.stdout.write(self.style.SUCCESS(f'Рассылка для {len(customer_emails)} клиентов завершена.'))
