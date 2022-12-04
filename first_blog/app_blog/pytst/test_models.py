import pytest
from faker import Faker
from ..factories import *
from ..models import *

fake = Faker()


def test_product_instance(db, review_factory):
    review = review_factory.create()
    item = FilmReview.objects.all().count()
    print(review.cat, item)
    assert True
