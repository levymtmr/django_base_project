import factory

from accounts.models import UserAccount

class UserAccountFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'tra lala %d' % n)
    email = factory.Sequence(lambda n: 'example_%s@example.com' % n)

    class Meta:
        model = UserAccount
