from main_card_container.models import Category
from django.template import Library

"""
Notes:
1. The logic is very simple, we get all Category instances from the DB and display it in template.
2. The "components/category_list_template.html" is the template which will be used to render HTML
3. You can check Custom template tags and filters
"""

register = Library()  # Necessary as per Django docs


@register.inclusion_tag("components/category_list_template.html", takes_context=True)
def categories_list(context):
    # Instead of context["list_page"] this may have to be the direct child - BUT it might not be! We'll find out!
    categories = Category.objects.filter(discipline=context["list_page"].discipline)
    try:
        if context["category"]:
            category_to_filter = context["category"]
    except:
        category_to_filter = None
    return {
        "request": context["request"],
        "categories": categories,
        "category_to_filter": category_to_filter,
        "list_page": context["list_page"],
    }
