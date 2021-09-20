# Django
from django.db import models

## Content
from wagtail.core.models import Page

## Admin / Edit Handlers
from wagtail.admin.edit_handlers import FieldPanel

## Categories & Tags
from wagtail.snippets.models import register_snippet

## Intermediary models
from modelcluster.fields import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import InlinePanel


@register_snippet
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        max_length=80,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class DetailPage(Page):
    description = models.CharField(max_length=255, blank=True, null=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["category"] = self.category  # This does not work
        return context


## Intermediary models
class DetailPageCategory(models.Model):
    page = ParentalKey("main_card_container.DetailPage", on_delete=models.CASCADE, related_name="categories")
    category = models.ForeignKey(
        "main_card_container.Category", on_delete=models.CASCADE, related_name="category", blank="True", null="True"
    )
