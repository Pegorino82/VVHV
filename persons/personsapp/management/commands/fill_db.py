from django.core.management.base import BaseCommand
import random
from datetime import date, timedelta
import uuid
from personsapp.models import Document, Person

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

    def handle(self, *args, **options):
        for i in range(10):
            doc_number = None
            try:
                doc_number = str(uuid.uuid4())[:20]
                new_doc = Document(
                    number=doc_number,
                    issue_date=random_birth(2015, 2018),
                    document_type=random.choice(doc_types)
                )
                new_doc.save()
            except Exception as err:
                print(f'Document error {err}')

            start_education = random_birth(2015, 2018)
            finish_education = start_education + timedelta(days=4 * 365)

            try:
                new_doc = Document.objects.filter(number=doc_number)[0]

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

                last_person = Person.objects.latest('id')

                last_person.documents.add(new_doc)

            except Exception as err:
                print(f'Person error {err}')
