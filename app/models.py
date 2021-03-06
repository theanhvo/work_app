from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



@python_2_unicode_compatible
class Post(models.Model):
    HN = 'hn'
    SG = 'sg'
    CITY_CHOICES = (
        (HN, 'Hà Nội'),
        (SG, 'Hồ Chí Minh')
    )

    logo_restaurant = models.CharField(
        _('Logo_restaurant'),
        max_length=256
    )

    restaurant_namme = models.CharField(
        _('Restaurant_namme'),
        max_length=256
    )

    address = models.CharField(
        _('Address'),
        max_length=256
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
        max_length=256
    )

    employer_mail = models.EmailField(
        _('Employer_mail'),
        blank=True,
        null=True
    )

    contact_employer = models.CharField(
        _('Contact_employer'),
        max_length=256,
        null=True
    )

    experience = models.CharField(
        _('Experience'),
        max_length=256,
        null=True
    )

    number_recruits = models.IntegerField(
        _('Number_recruits'),
        null=True
    )

    gender = models.CharField(
        _('Gender'),
        max_length=256,
        null=True
    )

    job_feature = models.CharField(
        _('Job_feature'),
        max_length=256,
        null=True
    )

    type_job = models.CharField(
        _('Type_job'),
        max_length=256,
        null=True
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
        return self.restaurant_namme.encode('ascii', 'ignore').decode('ascii')


@python_2_unicode_compatible
class Job(models.Model):
    post = models.ManyToManyField(
        Post
    )

    name = models.CharField(
        _('Name'),
        max_length=256
    )

    def __str__(self):
        return self.name.encode('ascii', 'ignore').decode('ascii')


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
