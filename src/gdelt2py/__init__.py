__version__ = 'v0.1.0'

from .task import Task
from .gdelt2 import Gdelt2
from .gdelt2event import Gdelt2Event

__title__ = 'gdelt2py'
__author__ = 'RakerZh'

__all__ = [
        "__version__",
        "Task",
        "Gdelt2",
        "Gdelt2Event"]
