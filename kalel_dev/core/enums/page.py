import enum


class Page(str, enum.Enum):
    HOME = "Home"
    ABOUT = "About"
    CONTACT = "Contact"
    PORTFOLIO = "Portfolio"
    BLOG = "Blog"
