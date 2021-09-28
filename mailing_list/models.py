from wagtail.core.models import Page
from django.forms import ModelForm


# Django
from django.db import models


class MailingListPage(Page):
    pass


class MailingList(models.Model):
    email_address = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email_address


class MailingListForm(ModelForm):
    class Meta:
        model = MailingList
        fields = ["email_address"]
