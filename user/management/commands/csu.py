from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Добавляем админа"""
        user = User.objects.create(
            email='san9nosko8@gmail.com',
            first_name='Admin',
            last_name='тут фамилия',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('qwerty')
        user.save()