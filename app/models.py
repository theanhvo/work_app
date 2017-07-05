from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



@python_2_unicode_compatible
class Post(models.Model):
    HN = 'hn'
    SG = 'sg'
    SG = 'sg'
    CITY_CHOICES = (
        (HN, 'Hà Nội'),
        (SG, 'Tp.Hồ Chí Minh')
    )
    logo_restaurant = models.ImageField(
        upload_to='logo'
    )
    restaurant_namme = models.CharField(
        _('Restaurant_namme'),
        max_length=100
    )

    address = models.CharField(
        _('Address'),
        max_length=100
    )

    city = models.CharField(
        _('City'),
        max_length=50,
        choices=CITY_CHOICES,
        default=SG,
        blank=True,
        null=True
    )
    wage = models.CharField(
        _('Wage'),
        max_length=20
    )

    employer_mail = models.EmailField(
        _('Employer_mail'),
    )

    contact_employer = models.CharField(
        _('Contact_employer'),
        max_length=30,
        null=True
    )
    position = models.CharField(
        _('Position'),
        max_length=36
    )

    created = models.DateTimeField(
        _('Created'),
        auto_now_add=True
    )

    updated = models.DateTimeField(
        _('Updated'),
        auto_now=True
    )

    job_description = models.TextField(
        _('Job_description'),
        null=True
    )

    job_requirements = models.TextField(
        _('Job_requirements'),
    )

    why_love_this_job = models.TextField(
        _('Why_love_this_job'),
    )

    deadline = models.CharField(
        _('Deadline'),
        max_length=20,
        null=True
    )


    def __str__(self):
        return self.restaurant_namme

@python_2_unicode_compatible
class Job(models.Model):
    post = models.ManyToManyField(
        Post
    )

    name = models.CharField(
        _('Name'),
        max_length=30
    )

    def __str__(self):
        return self.name


from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from userena.models import UserenaBaseProfile


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)
