from dataclasses import dataclass, field, fields
from typing import Generator


@dataclass(frozen=True)
class Extensions:
    txt: str = field(default=".txt", init=False)
    py: str = field(default=".py", init=False)
    png: str = field(default=".png", init=False)
    js: str = field(default=".js", init=False)
    html: str = field(default=".html", init=False)
    css: str = field(default=".css", init=False)
    kt: str = field(default=".kt", init=False)
    java: str = field(default=".java", init=False)
    xml: str = field(default=".xml", init=False)
    json: str = field(default=".json", init=False)
    jpg: str = field(default=".jpg", init=False)
    jar: str = field(default=".jar", init=False)
    war: str = field(default=".war", init=False)
    sql: str = field(default=".sql", init=False)
    config: str = field(default=".config", init=False)

    @classmethod
    def get_ext(cls) -> Generator[str, None, None]:
        return (getattr(cls, field_obj.name) for field_obj in fields(cls))
