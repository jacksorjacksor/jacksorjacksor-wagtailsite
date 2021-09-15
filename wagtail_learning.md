# Wagtail Learning

Here is a list of the things I need to remember when starting off

# Models

## Core wagtail packages:

```python
from django.db import models
```

### Code

```python
from wagtail.core.models import Page
```

### Admin

```python
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
```

---

## Making a page class (boiler plate)

```python
class HomePage(Page):
    lead_text = models.CharField(
        max_length=100,
        blank=False,  # whether you're allowed to not have an image
        null=True,  # whether it can be null in the database
        help_text="Lead text help")
```

### Content panels

Used to edit fields via the admin page

```python
    content_panels = Page.content_panels + [
        FieldPanel("foo_text"),
        PageChooserPanel("foo_button"),
        ImageChooserPanel("foo_image"),
    ]
```

### get_context

```python
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        hello_world = "hello world 123"
        context['hello_world'] = hello_world
        return context
```

### Quick notes

-   images are Foreign keys:

```python
class FooPage(Page):
    foo_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,  # you MUST have an image
        null=True,  # can be nothing in the Database
        on_delete=models.SET_NULL,
        help_text='This image will be used on the Service Listing Page',
        related_name='+',
    )
```
