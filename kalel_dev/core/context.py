from fastapi import Request
from kalel_dev.core.enums.page import Page
from typing import TypedDict


class NavigationItem(TypedDict):
    name: str
    url: str
    active: bool


def navigation_context(page: Page) -> list[NavigationItem]:
    nav_items = [
        {
            "name": "Home",
            "url": "/",
            "active": page == Page.HOME
        },
        {
            "name": "Projects",
            "url": "/projects",
            "active": page == Page.PROJECTS
        },
        {
            "name": "About Me",
            "url": "/about",
            "active": page == Page.ABOUT
        },
        {
            "name": "Contact",
            "url": "/contact",
            "active": page == Page.CONTACT
        },
        {
            "name": "Blog",
            "url": "/blog",
            "active": page == Page.BLOG
        },
    ]

    return nav_items


def create_context(
    request: Request,
    page: Page,
    extra_context: dict = None
) -> dict:

    keywords =[
        "Kalel",
        "Kalel Martinho"
        "Kalel Leonardo Martinho",
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
        "Software Engineer"
    ]

    base_context = {
        "request": request,
        "title": f"Kalel Software Engineer - {page.value}",
        "description": "Kalel - Software Engineer",
        "author": "Kalel L. Martinho",
        "keywords": ', '.join(keywords),
        "navigation": navigation_context(page)
    }

    base_context.update(extra_context or {})

    return base_context


