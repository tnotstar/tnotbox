# -*- coding: utf-8 -*-

from pathlib import Path
from confz import ConfZ, ConfZFileSource


DEFAULT_CONFIG_FILENAME = r"getstarted.yaml"

DEFAULT_CONFIG_SOURCE = ConfZFileSource(file=Path(DEFAULT_CONFIG_FILENAME))


class ExampleConfiguration(ConfZ):

    CONFIG_SOURCES = DEFAULT_CONFIG_SOURCE

    name: str

# EOF