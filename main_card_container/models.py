# IMPORTS
from django.db import models
from django.db.models.fields import Field

## Content
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from .blocks import BodyBlock

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

# MODELS
## Categories & Tags
@register_snippet
class Discipline(models.Model):
    name = models.CharField(max_length=255)

    panels = [FieldPanel("name")]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"


@register_snippet
class CardCategory(models.Model):
    name = models.CharField(max_length=255)
    discipline = models.ForeignKey(
        Discipline,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    slug = models.SlugField(
        # could this be self.name? Or just name.. it's a SlugField, that's the only difference.
        unique=True,
        max_length=80,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("discipline"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


@register_snippet
class Tag(TaggitTag):
    # since Wagtail already has tag support built on django-taggit, so here we create a proxy-model to declare it as wagtail snippet
    class Meta:
        proxy = True


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

    body = StreamField(BodyBlock(), blank=True)

    tags = ClusterTaggableManager(through="main_card_container.DetailPageTag", blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        InlinePanel("categories", label="categories"),
        FieldPanel("tags"),
        StreamFieldPanel("body"),
    ]


## Intermediary models
class DetailPageListCategory(models.Model):
    page = ParentalKey("main_card_container.DetailPage", on_delete=models.CASCADE, related_name="categories")
    card_category = models.ForeignKey(
        "main_card_container.CardCategory", on_delete=models.CASCADE, related_name="card_pages"
    )

    panels = [SnippetChooserPanel("card_category")]

    class Meta:
        unique_together = (
            "page",
            "card_category",
        )  # https://docs.djangoproject.com/en/3.2/ref/models/options/#unique-together


class DetailPageTag(TaggedItemBase):
    content_object = ParentalKey("DetailPage", related_name="detail_tags")
