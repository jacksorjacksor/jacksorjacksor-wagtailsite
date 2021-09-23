from wagtail.core.models import Page
from django.forms import ModelForm
from hcaptcha.fields import hCaptchaField

# Django
from django.db import models


class MailingListPage(Page):
    pass


class MailingList(models.Model):
    email_address = models.CharField(max_length=100, blank=True, null=True)
    hcaptcha = hCaptchaField()

    def __str__(self):
        return self.email_address


class MailingListForm(ModelForm):
    class Meta:
        model = MailingList
        fields = ["email_address", "hcaptcha"]
