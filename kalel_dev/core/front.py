from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from kalel_dev.core.config import settings

templates = Jinja2Templates(directory=settings.templates_dir)
static_files = StaticFiles(directory=settings.static_dir)