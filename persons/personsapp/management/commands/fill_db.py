from django.core.management.base import BaseCommand
import random
import datetime
from personsapp.models import Document, Person

# class Command(BaseCommand):
#     help = '''fills DB'''
#
#     def handle(self, *args, **options):
#
#         if options['random']:
#
#             if len(categories) == 0:
#                 ctgrs = ['Category_' + str(i) for i in range(1, 11)]
#                 for category in ctgrs:
#                     cat = Category(name=category)
#                     cat.save()
#
#             if len(markers) == 0:
#                 for marker in ['corner_new', 'corner_hot', 'None']:
#                     mark = ProductMarker(corner=marker)
#                     mark.save()
#
#             categories = Category.objects.all()
#             markers = ProductMarker.objects.all()
#
#
#             products = []
#             ammount = options['random']
#
#             for i in range(1, ammount):
#                 products.append(
#                     {
#                         'name': 'Product_' + str(i),
#                         'short_text': 'Product short text',
#                         'long_text': 'Product long text',
#                         'now_price': random.randint(1000, 1500),
#                         'old_price': random.randint(1500, 2000),
#                         'product_marker': random.choice(markers),
#                         'category': random.choice(categories),
#                         'image': random.choice(images),
#                         'quantity': random.randint(5, 15)
#                     }
#                 )
#
#             for prod in products:
#                 try:
#                     product = Product(**prod)
#                     product.save()
#                 except Exception as err:
#                     print(f'Exception: {err}')

if __name__ == '__main__':
    import random
    import re
