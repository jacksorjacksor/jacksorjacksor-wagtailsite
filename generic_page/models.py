from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail_utils.blocks import BodyBlock

from wagtail.admin.edit_handlers import StreamFieldPanel


class GenericPage(Page):
    body = StreamField(BodyBlock(), blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
