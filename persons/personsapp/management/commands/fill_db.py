from django.core.management.base import BaseCommand
from django.conf import settings
import random
import uuid
import os
from shutil import copy2
from datetime import date, timedelta

from personsapp.models import Document, Person, Image

first_names = ['Иван', 'Петр', 'Федор']
last_names = ['Иванов', 'Петров', 'Федоров']
patr_names = ['Иванович', 'Петрович', 'Федорович']
education_group = ['Первая группа', 'Вторая группа', 'Третья группа']
education_place = ['Заведение 1', 'Заведение 2', 'Заведение 3']

doc_types = ['PASS', 'BIRTH', 'STUD']


def random_birth(start_year=1990, end_year=2000):
    day = random.randrange(1, 32)
    month = random.randrange(1, 13)
    year = random.randrange(start_year, end_year)
    try:
        return date(year, month, day)
    except:
        return date(year, month, day - 5)


class Command(BaseCommand):
    help = '''fills DB'''

    def add_arguments(self, parser):
        parser.add_argument('-amount')

    def handle(self, *args, **options):
        Image.objects.all().delete()
        Document.objects.all().delete()
        Person.objects.all().delete()

        if options['amount']:
            amount = int(options['amount'])
        else:
            amount = 10

        images_path = os.path.join(settings.BASE_DIR, 'test_images')
        images_list = os.listdir(images_path)

        for img in images_list:
            if img.endswith('jpg'):
                try:
                    image = Image(
                        title=img,
                        image=img
                    )
                    image.save()
                    copy2(os.path.join(images_path, img), os.path.join(settings.BASE_DIR, 'media'))
                except Exception as err:
                    print(f'Image {err}')

        images_list = Image.objects.all()

        for i in range(amount):
            start_education = random_birth(2015, 2018)
            finish_education = start_education + timedelta(days=4 * 365)
            try:
                new_person = Person(
                    first_name=random.choice(first_names),
                    last_name=random.choice(last_names),
                    patr_name=random.choice(patr_names),
                    birth_date=random_birth(),
                    gender=random.choice(('M', 'F')),
                    phone=random.randrange(10000000000, 79999999999),
                    start_education=start_education,
                    finish_education=finish_education,
                    education_group=random.choice(education_group),
                    education_place=random.choice(education_place),
                )
                new_person.save()

            except Exception as err:
                print(f'Person error {err}')

            try:
                last_person = Person.objects.latest('id')
                person_age = last_person.age
                if person_age >= 14:
                    doc_number = str(uuid.uuid4())[:20]
                    passport = Document(
                        number=doc_number,
                        issue_date=random_birth(2015, 2018),
                        document_type='PASS',
                        scan=random.choice(images_list),
                        person=last_person
                    )
                    passport.save()
                doc_number = str(uuid.uuid4())[:20]
                birth_cert = Document(
                    number=doc_number,
                    issue_date=random_birth(2015, 2018),
                    document_type='BIRTH',
                    scan=random.choice(images_list),
                    person=last_person
                )
                birth_cert.save()

                doc_number = str(uuid.uuid4())[:20]
                student_card = Document(
                    number=doc_number,
                    issue_date=random_birth(2015, 2018),
                    document_type='STUD',
                    scan=random.choice(images_list),
                    person=last_person
                )
                student_card.save()

            except Exception as err:
                print(f'Document error {err}')
