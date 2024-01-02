import enum


class Page(str, enum.Enum):

    HOME = "Home"
    ABOUT = "About"
    CONTACT = "Contact"
    PROJECTS = "Projects"
    BLOG = "Blog"
