from django.contrib.auth.management.commands.createsuperuser import Command as CreateSuperUserCommand
from django.core.management import CommandError
from django.db import transaction

class Command(CreateSuperUserCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--date_of_birth', dest='date_of_birth', required=True, help='The date of birth for the superuser.')

    def handle(self, *args, **options):
        date_of_birth = options.get('date_of_birth')
        if not date_of_birth:
            raise CommandError('You must provide a date of birth.')
        
        with transaction.atomic():
            self.UserModel._default_manager.db_manager(options.get('database')).create_superuser(
                email=options.get('email'),
                password=options.get('password1'),
                date_of_birth=date_of_birth,
                first_name=options.get('first_name'),
                last_name=options.get('last_name'),
            )
            if options.get('verbosity', 1) >= 1:
                self.stdout.write("Superuser created successfully.")
