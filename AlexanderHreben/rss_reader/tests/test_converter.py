"""This module contains tests for module converter.py."""

import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.getcwd())

from grebarss_reader.converter import Converter


@pytest.fixture
def converter_instance(tmpdir):
    """
    Initialization object class Converter
    :param tmpdir: object temp catalog
    :return: object class Converter
    """
    feed = {}
    return Converter('https://people.onliner.by/feed', feed, str(tmpdir))


def test_to_pdf_create_file(converter_instance):
    """
    Verifies that method to_pdf of class Converter creates a file
    :param converter_instance: object class Converter
    """
    converter_instance.to_pdf()
    assert (os.path.exists(Path(converter_instance.folder_path, "news.pdf")) is True)


def test_to_html_create_file(converter_instance):
    """
    Verifies that method to_html of class Converter creates a file
    :param converter_instance: object class Converter
    """
    converter_instance.to_html()
    assert (os.path.exists(Path(converter_instance.folder_path, "news.html")) is True)
