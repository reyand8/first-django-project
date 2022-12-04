import factory
from faker import Faker
from .models import *
fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = 'django'
    slug = fake.slug


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FilmReview
    title = fake.sentence()
    # content = fake.text()
    photo = fake.file_extension(category='image')
    time_create = fake.date()
    time_update = fake.date()
    cat = factory.SubFactory(CategoryFactory)
    slug = ''
    is_published = 'True'
