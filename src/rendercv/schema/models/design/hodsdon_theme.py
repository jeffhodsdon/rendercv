"""Hodsdon theme - Custom theme for Jeff Hodsdon's CV with arrow link suffix."""

from typing import Literal

import pydantic

from rendercv.schema.models.base import BaseModelWithoutExtraKeys
from rendercv.schema.models.design.classic_theme import (
    ClassicTheme,
    Colors,
    Entries,
    Header,
    Page,
    Sections,
    SectionTitles,
    Templates,
    Typography,
)


class HodsdonLinks(BaseModelWithoutExtraKeys):
    """Links configuration for Hodsdon theme."""

    underline: bool = pydantic.Field(
        default=False,
        description="Underline hyperlinks. The default value is `false`.",
    )
    show_external_link_icon: bool = pydantic.Field(
        default=True,
        description=(
            "Show an external link icon next to URLs. The default value is `true`."
        ),
    )


class HodsdonTheme(BaseModelWithoutExtraKeys):
    """Hodsdon theme - extends classic with custom link styling."""

    theme: Literal["hodsdon"] = "hodsdon"
    page: Page = pydantic.Field(default_factory=Page)
    colors: Colors = pydantic.Field(default_factory=Colors)
    typography: Typography = pydantic.Field(default_factory=Typography)
    links: HodsdonLinks = pydantic.Field(default_factory=HodsdonLinks)
    header: Header = pydantic.Field(default_factory=Header)
    section_titles: SectionTitles = pydantic.Field(default_factory=SectionTitles)
    sections: Sections = pydantic.Field(default_factory=Sections)
    entries: Entries = pydantic.Field(default_factory=Entries)
    templates: Templates = pydantic.Field(default_factory=Templates)
