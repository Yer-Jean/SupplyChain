from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = ('Create a superuser with the specified email\n'
            'Usage: python manage.py create_super_user [john@example.com] [password]')

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='SuperUser email address')
        parser.add_argument('password', type=str, help='SuperUser password')

    def handle(self, *args, **options):
        superuser_email = options['email']
        superuser_password = options['password']

        # Проверка наличия суперпользователя с таким email
        if User.objects.filter(email=superuser_email):
            self.stdout.write(self.style.ERROR(f'Superuser with email "{superuser_email}" already exists.'))
            return

        user = User.objects.create(
            email=superuser_email,
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password(superuser_password)
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Superuser with email "{superuser_email}" successfully created.'))
