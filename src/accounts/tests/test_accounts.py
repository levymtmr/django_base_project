
import pytest
from django.test import TestCase
from django.db import IntegrityError

from accounts.models import UserAccount
from accounts.tests.factories import UserAccountFactory

class TestAccount(TestCase):

    def setUp(self):
        UserAccountFactory.create()

    def test_create_user_account(self):
        UserAccount.objects.create(username='jack', first_name='tequila')
        assert UserAccount.objects.all().count() == 2

    def test_add_same_name_in_two_accounts(self):
        UserAccount.objects.create(username='jack', first_name='tequila')
        with pytest.raises(IntegrityError):
            UserAccount.objects.create(username='jack', first_name='tequila')

