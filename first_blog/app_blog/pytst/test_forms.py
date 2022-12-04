from ..forms import RegisterUserForm
from django.test import TestCase
import unittest
import pytest
from django.contrib.auth import authenticate
from ..views import *


@pytest.mark.skip
class TestRegisterForms(unittest.TestCase):
    """Test Form with captcha"""
    def test_form_true(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertTrue(is_valid)

    def test_form_email(self):
        form_data = {
            'username': 'user123',
            'email': 'a@.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)

    def test_form_password_mismatch(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)

    def test_form_short_password(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123-!',
            'password2': '123-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)

    def test_form_invalid_captcha(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "a",
            'captcha_1': "",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)


@pytest.mark.skip
class LogInTest(TestCase):

    def setUp(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
        }
        form = RegisterUserForm(data=form_data)
        if form.is_valid():
            form.save()

    def test_correct(self):
        user = authenticate(username='user123', password='123456789a-!')
        self.assertTrue((user is not None) and user.is_authenticated)


if __name__ == "__main__":
    unittest.main()


#####################################################
#####################################################
# PYTEST

@pytest.mark.parametrize(
    "username, email, password1, password2, captcha_0, captcha_1, validity",
    [
        ("user12", "a@a.com", "12345678a-!", "12345678a-!",
         "dummy_value", "", False),  # captcha
        ("user1", "a@a.com", "12345a", "", "dummy_value", "PASSED", False),  # no second password
        ("user1", "a@a.com", "1234567899", "12345678a", "dummy_value", "PASSED", False),  # password mismatch
        ("user1", "a@a.com", "12345", "12345", "dummy_value", "PASSED", False),  # password is short
        ("user1", "a@.com", "12345a", "12345a", "dummy_value", "PASSED", False),  # email
    ],
)
@pytest.mark.django_db
def test_create_account(username, email, password1, password2, captcha_0, captcha_1, validity):
    form = RegisterUserForm(
        data={
            "username": username,
            "email": email,
            "password1": password1,
            "password2": password2,
            "captcha_0": captcha_0,
            "captcha_1": captcha_1,
        },
    )
    assert form.is_valid() is validity


@pytest.mark.parametrize(
    "username, password, validity",
    [
        ("user12", "12", False),
        ("user1", "", False),  # email
    ],
)
@pytest.mark.django_db
def test_login(username, password, validity):
    form = RegisterUserForm(
        data={
            "username": username,
            "password": password,
        },
    )
    assert form.is_valid() is validity
