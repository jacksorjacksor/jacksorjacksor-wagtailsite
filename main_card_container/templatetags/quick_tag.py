from django.template import Library

register = Library()


@register.inclusion_tag("main_card_container/random_html.html", takes_context=True)
def my_random_thing(context):
    return {"request": context["request"]}
