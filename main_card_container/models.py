# IMPORTS
from django.db import models
from django.db.models.fields import Field

## Content
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail_utils.blocks import BodyBlock

## Admin / Edit Handlers
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

## Categories & Tags
from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag

## Intermediary models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.tags import ClusterTaggableManager
from wagtail.admin.edit_handlers import InlinePanel


@register_snippet
class Category(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(
        # could this be self.name? Or just name.. it's a SlugField, that's the only difference.
        unique=True,
        max_length=80,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("icon"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


## Pages
class ListPage(Page):
    description = models.CharField(
        max_length=255,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
    ]


class DetailPage(Page):
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    description = models.CharField(max_length=255, blank=True, null=True)

    body = StreamField(BodyBlock(), blank=True)

    hero_content_bool = models.BooleanField(default=False, blank=False, null=False)

    hero_super_title = models.CharField(max_length=255, blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("description"),
        StreamFieldPanel("body"),
        InlinePanel("categories", label="categories"),
        FieldPanel("hero_content_bool"),
        FieldPanel("hero_super_title"),
    ]


## Intermediary models
class DetailPageCategory(models.Model):
    page = ParentalKey("main_card_container.DetailPage", on_delete=models.CASCADE, related_name="categories")
    category = models.ForeignKey(
        "main_card_container.Category", on_delete=models.CASCADE, related_name="category", blank="True", null="True"
    )

    panels = [SnippetChooserPanel("category")]

    class Meta:
        unique_together = (
            "page",
            "category",
        )  # https://docs.djangoproject.com/en/3.2/ref/models/options/#unique-together
