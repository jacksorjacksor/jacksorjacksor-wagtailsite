# Action plan

1. Make `landing page`

This is the most basic page type and will help us to start to understand what is required/remember how to use Wagtail.

2. Assess `detail page` & `list page`

Possibly refactor css (i.e. check over naming conventions based on new layout). Very possible that these can actually be the same page just with different content provided.

3. Make `list page`

4. Make `detail page`

5. Work out how to make `list (filtered) page`

6. Look into PostGres implementation

7. Migrate content

8. Launch by end of weekend

---

# What needs to be done

## Types of page to make [priority to get done]

-   landing [1]
-   list [2]
-   list (filtered) [4]
-   detail [3]

## Base files

-   base.html
-   navigation.html

# Work to be done for each page

## Page: base

---

## Page: navigation

A lot of this can well be hard-coded, and I know there are clever ways for these pages to be made automatically, but for now I'll just make models.

1. hard-code
2. use Django models
3. use Wagtail functionality

### navigation menu

-   menu item
-   menu href
-   sub-menu item
-   sub-menu text

(...I actually am unsure on how to do this at present! It'll be granualised into having a 'menu' class and a 'sub list' thing or whatever...)

### social links

-   title (? unsure if used but good practice. this is a default field anyway I believe)
-   href
-   icon

---

## Page: landing

### landing card

two of these are found on the homepage. these are links to the main two sections of page, in this instance "music" and "tech"

-   site-name (repeated!)
-   class name (used for styling)
-   href
-   page-name-of-href
-   icon-arrow
-   icon-page-name

---

## Page: list

-   title (default)
-   subtitle

### Category card

-   category
-   class
-   href
-   icon
-   discipline (music, tech, both)

### Item card

(I think we can ALSO use this for hero)

-   title (default)
-   img
-   category-icon (can you get the icon, defined in category?)
-   date published (editable)
-   description
-   hero (boolean - if true then is displayed at top and not displayed at bottom? query sets baby)
-   super-title (only shown if hero)
-   discipline (music, tech, both)

---

## Page: detail

This will inherit quite a bit of the "page: list" things.

### hero display

This IS the "Item card" (maybe have different description?)

### Details

-   title (default?)
-   rich_text

(This could well just be built into the item card, but we'll keep it separate for now)

### category

-   this is the same as in page list.

---

## Page: contact

-   rich text

---

## Page: about

-   rich text

---

# Identifying blocks

## Layout for list & detail pages:

{ head }

{ nav }

{ category - on list page }

{ hero }

{ more details - on detail page }

{ category - on detail page }

{ list }

{ footer }

---
