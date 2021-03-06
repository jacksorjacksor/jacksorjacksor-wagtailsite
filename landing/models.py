from django.db import models
from wagtail.core.models import Page
from main_card_container.models import ListPage, DetailPage

# Create your models here.


class LandingPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["music_list_page"] = ListPage.objects.filter(title="music")[0]
        context["tech_list_page"] = ListPage.objects.filter(title="tech")[0]

        return context
