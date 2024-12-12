from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Создание группы Managers с заданными правами'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Managers')
        
        permissions = [
            'can_view_customer',
            'can_edit_customer',
            'can_delete_customer',
            'can_view_message',
            'can_edit_message',
            'can_delete_message'
        ]
        
        for perm in permissions:
            permission = Permission.objects.get(codename=perm)
            group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Группа Managers создана и права назначены.'))
