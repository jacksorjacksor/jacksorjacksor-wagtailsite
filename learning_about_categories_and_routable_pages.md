# How to tackle the "Categories" section

## Goals

-   Create Categories for the site. These can:

    -   be assigned to any DetailPage
    -   the category can be printable to any page displaying the DetailPage
        -   i.e. {{ list_page.category }} should work!
    -   can be used for routable pages
        -   i.e. /list_page/<category>/ can work as a filter
    -   make a "category_block" which can be imported into the relevant pages
    -   be able to filter this "category_block" and visually represent this
        -   i.e. /list_page/category-1/ will show 'category-1' is the 'active' category

-   Plan

    -   Go through yesterday's code, remove instances of "tags" as we don't care about them

    *   Re-read through the process to make the Categories
        -   Be _very clear_ on how these are made and what the process is around them
    *   Assess from there

# Step 1

-   Understanding how to get the category associated with the item page

# Step 2

-   Let's try to make the HTML snippets of the 4 grid box (in the PDF)

## Results

    -   Understanding much more clear about relationship between:
        -   Page (DetailPage)
        -   Snippet (Category)
        -   Intermediary (DetailPageCategory)

## Learning sources

-   accordbox

    -   "Build Blog" .pdf: file://mnt/e/OneDrive/buildblogwithwagtailcms.pdf
    -   Wagtail Tutorials:
        -   3. "Add Blog Models": https://www.accordbox.com/blog/add-blog-models-wagtail/
        -   4. "Routable Page" "https://www.accordbox.com/blog/wagtail-tutorials-routable-page/"

-   learnwagtail.com

    -   "Routable Pages": https://learnwagtail.com/tutorials/routable-pages/
    -   "Routable Page Categories And Years": https://learnwagtail.com/tutorials/routable-page-categories-and-years/

    -   "Create a Navigation System from Scratch": https://learnwagtail.com/wagtail-for-beginners/create-navigation-system-scratch/
    -   "Navigation Templates": https://learnwagtail.com/wagtail-for-beginners/navigation-templates/

## Helpful tutorials to check out later

-   learnwagtail.com

    -   "Adding Debug Tools": https://learnwagtail.com/wagtail-for-beginners/adding-debug-tools/

## Asides

-   Git icon!!! Still the AA!
-   Next page in the Admin for child pages specifically?

# ERRORS

1. https://www.accordbox.com/blog/wagtail-tutorials-routable-page/

    - "wagtail.contrib.wagtailroutablepage", does not exist => "wagtail.contrib.routable_page"
    - as per https://docs.wagtail.io/en/stable/reference/contrib/routablepage.html
