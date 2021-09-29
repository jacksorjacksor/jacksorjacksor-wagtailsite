from wagtail.core.models import Page

all_pages = Page.objects.all()

detail_page = all_pages.filter(title="show 1")[0].detailpage

category_of_detail_page = detail_page.categories.all()[0].category

category_of_detail_page.name


# GENERIC

from wagtail.core.models import Page

all_pages = Page.objects.all()

detail_page = all_pages.filter(title="foo")[0].detailpage

category_of_detail_page = detail_page.categories.all()[0].category

category_of_detail_page.name
# returns: "bar"
