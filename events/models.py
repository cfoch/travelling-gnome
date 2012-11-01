# vim: ai ts=4 sts=4 et sw=4
from django.db import models

# Models should be moved out, now it is easier to do it in one single
# file.

class Persona(models.Model):
    OCCUPATIONS = (
            (0, 'Student'),
            (1, 'Professional'),
            (2, 'Retired'),
    )
    SEX = (
            (0, 'Male'),
            (1, 'Female'),
            (2, 'Not important'),
    )

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    airport = models.CharField(max_length=3, verbose_name="3 letter airport code")
    occupation = models.IntegerField(max_length=1, choices=OCCUPATIONS)
    foundation = models.BooleanField(verbose_name="Foundation member")
    sex = models.IntegerField(max_length=1, choices=SEX)
    email = models.EmailField()
    # FIXME: what does django use for phone numbers? this can be "huge"
    # numbers
    phone = models.CharField(max_length=20)
    blog = models.URLField()
    twitter = models.CharField(max_length=20)


class Event(models.Model):
    EVENT_STATUS = (
        (0, 'Event is open for application'),
        (1, 'Applications are being evaluated'),
        (2, 'Event is happening'),
        (3, 'Reimbursements started'),
        (4, 'Nothing else to do'),
    )

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    organization = models.CharField(max_length=50, verbose_name="Organization doing the event")
    contacts = models.ManyToManyField(Persona, verbose_name="Responsible people")
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.CharField(max_length=250)
    url = models.URLField()
    status = models.IntegerField(max_length=1, choices=EVENT_STATUS)


class Sponsorship(models.Model):
    SPONSORSHIP_STATUS = (
        (0, 'Requested'),
        (1, 'Approved'),
        (2, 'Confirmed'),
        (3, 'Reimbursed'),
    )

    event = models.ForeignKey('Event')
    persona = models.ForeignKey('Persona')

    arrival = models.DateField()
    departure = models.DateField()

    requested = models.DecimalField(max_digits=8, decimal_places=2,
                                    verbose_name="Requested amount")
    approved = models.DecimalField(max_digits=8, decimal_places=2,
                                   verbose_name="Approved amount")
    reimbursed = models.DecimalField(max_digits=8, decimal_places=2,
                                     verbose_name="Reimbursed amount")
    status = models.IntegerField(max_length=1, choices=SPONSORSHIP_STATUS)

    transport = models.BooleanField(verbose_name="Requesting travel assistance")
    accommodation = models.BooleanField(verbose_name="Requesting accommodation help")
    other = models.TextField(verbose_name="Other expenses, specify")

    agenda = models.TextField(verbose_name="Tell us about your goals and agenda for this travel")
    reports = models.URLField(verbose_name="Link to blog posts, photos you took")
    receipt = models.FileField(upload_to="receipts/%Y/%m/", verbose_name="Receipts of your approved expenses")

