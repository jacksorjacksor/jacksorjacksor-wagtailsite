# build-blog-with-wagtail-cms-feedback

v3.0.0

To be emailed to:
michaelyin@accordbox.com

## Title

-   Grammar: the title should actually be "Build A Blog With Wagtail CMS" but I feel it may be too late to change that!

## 4.5 Category and Tag

### Notes 2.

-   Grammar: "[...] that ~~can make us~~ [that allow us to] add/edit/delete the model instances"

## 4.6 Intermediary model

-   No file reference for either code snippet

    -   assumed "blog/models.py" but as this was included in previous examples I wanted to highlight!

-   Grammar: "[..] I do not recommend [the] use [of the] ParentalManyToManyField in Wagtail app even [if] it seems more easy to understand"

-   Code: SnippetChooserPanel - when this is first used the import statement is missing. The source code given later in "4.7 Source Code" has the import statement included.

    -   import statement: `from wagtail.snippets.edit_handlers import SnippetChooserPanel`

-   Code: InlinePanel - import statement missing (same as "SnippetChooserPanel" issue mentioned above)

    -   import statement: `from wagtail.admin.edit_handlers import InlinePanel`

-   Grammar: unique_together = ("page", "blog_category") ~~would add~~ adds db constraints to avoid duplicate records.

## 7.4

-   `typing_extensions` needs to be included
