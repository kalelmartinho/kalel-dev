from typing import Optional, TypedDict

from fastapi import Request

from kalel_dev.core.enums.page import Page
import datetime


class NavigationItem(TypedDict):
    name: Page | str
    url: str
    active: bool


def navigation_context(page: Page) -> list[NavigationItem]:
    nav_items = [
        NavigationItem(name=page.HOME.value, url="/", active=page == Page.HOME),
        NavigationItem(
            name=page.PORTFOLIO.value, url="/projects", active=page == Page.PORTFOLIO
        ),
        NavigationItem(name=page.ABOUT.value, url="/about", active=page == Page.ABOUT),
        NavigationItem(name=page.CONTACT.value, url="/contact", active=page == Page.CONTACT),
        NavigationItem(name=page.BLOG.value, url="/blog", active=page == Page.BLOG),
    ]

    return nav_items


def create_context(
    request: Request, page: Page, extra_context: Optional[dict] = None
) -> dict:
    keywords = [
        "Kalel",
        "Kalel Martinho" "Kalel Leonardo Martinho",
        "Dev",
        "Python",
        "Python Developer",
        "Python Engineer",
        "Python Software Engineer",
        "Python Software Developer",
        "FastAPI",
        "FastAPI Developer",
        "Python Specialist",
        "Python Backend Developer",
        "Python Full Stack Developer",
        "Full Stack Developer",
        "Developer",
        "Software Engineer",
        "Software Developer",
        "Software Engineer",
        "Software Developer",
        "Software Engineer",
    ]

    base_context = {
        "request": request,
        "page_title": f"Kalel - Software Engineer - {page.value}",
        "page_description": "Kalel Martinho personal website, including portfolio projects, blog posts and contact information.",
        "author": "Kalel L. Martinho",
        "role": "Software Engineer",
        "keywords": ", ".join(keywords),
        "navigation": navigation_context(page),
        "current_year": datetime.datetime.now().year,
    }

    base_context.update(extra_context or {})

    return base_context
