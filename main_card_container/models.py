# Django
from django.db import models

## Content
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail_utils.blocks import BodyBlock

# Routable Pages
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

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
        unique=True,
        max_length=80,
    )
    discipline = models.ForeignKey(
        "main_card_container.Discipline", on_delete=models.CASCADE, related_name="discipline", blank="True", null="True"
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("icon"),
        FieldPanel("slug"),
        FieldPanel("discipline"),
    ]

    def __str__(self):
        return f"{self.title} ({self.discipline.title})"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


@register_snippet
class Discipline(models.Model):
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"


## Pages
class ListPage(RoutablePageMixin, Page):
    description = models.CharField(
        max_length=255,
        blank=True,
    )
    discipline = models.ForeignKey(
        "main_card_container.Discipline",
        on_delete=models.SET_NULL,
        related_name="discipline_of_list_page",
        blank="True",
        null="True",
    )
    content_panels = Page.content_panels + [FieldPanel("description", classname="full"), FieldPanel("discipline")]

    def get_context(self, request, *args, **kwargs):
        context = super(ListPage, self).get_context(request, *args, **kwargs)
        context["list_page"] = self
        context["posts"] = self.posts
        try:
            context["category"] = self.category
        except:
            pass
        return context

    def get_posts(self):
        return DetailPage.objects.descendant_of(self).live()

    @route(r"^category/(?P<category>[-\w]+)/$")
    def post_by_category(self, request, category, *args, **kwargs):
        self.posts = self.get_posts().filter(categories__category__title=category)
        self.category = category
        return self.render(request)

    @route(r"^$")
    def post_list(self, request, *args, **kwargs):
        self.posts = self.get_posts()
        return self.render(request)


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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["list_page"] = self.get_parent().specific
        return context

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
