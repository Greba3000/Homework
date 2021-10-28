"""  """

import os
import sys

import pytest

sys.path.append(os.getcwd())

from grebarss_reader.rss_parser import RssParser


@pytest.fixture
def rss_parser_instance():
    """
    Initialization object class RssParser
    :return: object class RssParser
    """
    return RssParser()


@pytest.mark.parametrize('some_links, expected_links', [
    [{'url': 'https://image1.jpg'}, 'https://image1.jpg'],
    [{'url': [{'link': 'https://image2.jpeg'}]}, 'https://image2.jpeg'],
    [{'url': [{'https://image3.png': 'https://image4'}]}, 'https://image3.png'],
],
                         )
def test_get_image_link_get_valid_link(rss_parser_instance, some_links, expected_links):
    """
    Checks link format validation
    :param rss_parser_instance: object class RssParser
    :param some_links: sample some image link in feed
    :param expected_links: string with image link
    """
    got_links = rss_parser_instance._get_image_link(some_links)
    assert (got_links == expected_links)
