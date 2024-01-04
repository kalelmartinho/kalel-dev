from typing import Optional, TypedDict

from fastapi import Request

from kalel_dev.core.enums.page import Page


class NavigationItem(TypedDict):
    name: Page | str
    url: str
    active: bool


def navigation_context(page: Page) -> list[NavigationItem]:
    nav_items = [
        NavigationItem(name=page.HOME.value, url="/", active=page == Page.HOME),
        NavigationItem(
            name=page.PROJECTS.value, url="/projects", active=page == Page.PROJECTS
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
        "title": f"Kalel Software Engineer - {page.value}",
        "description": "Kalel - Software Engineer",
        "author": "Kalel L. Martinho",
        "role": "Software Engineer",
        "keywords": ", ".join(keywords),
        "navigation": navigation_context(page),
    }

    base_context.update(extra_context or {})

    return base_context
