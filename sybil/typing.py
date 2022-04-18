from typing import Callable, TYPE_CHECKING, Iterable, Optional, Any

if TYPE_CHECKING:
    from .document import Document
    from .example import Example
    from .region import Region


Evaluator = Callable[['Example'], Optional[str]]
Parser = Callable[['Document'], Iterable['Region']]
