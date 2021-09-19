from main_card_container.models import Category
from django.template import Library

"""
Notes:
1. The logic is very simple, we get all Category instances from the DB and display it in template.
2. The "components/category_list_template.html" is the template which will be used to render HTML
3. You can check Custom template tags and filters
"""

register = Library()  # ??


@register.inclusion_tag("components/category_list_template.html", takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        "request": context["request"],
        "categories": categories,
    }
