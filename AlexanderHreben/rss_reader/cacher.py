"""Storage module for Cacher class"""

import json
import logging
from datetime import datetime

logger = logging.getLogger('app.cacher')


class Cacher:
    """
    Class for saving and retrieving news from the repository (db.json)
    if the variable source == None it means that we use all the sources available in the storage (db.json)
    """

    def __init__(self, source):
        self.source = source
        self.cache_file_path = "db.json"
        """
        :param source: URL of the RSS resource
        """
        
    def cache(self, feed: dict):
        """
        Saves news from rss_parser to the repository (db.json)
        :param feed: dictionary containing news from rss_parser
        """
        
        with open(self.cache_file_path, "r+", encoding="utf-8") as cache_file:
            json_content = cache_file.read()
            json_dicts = json.loads(json_content)

            url_list = []
            counter = 0
            
            for elem in json_dicts:
                url_list.append([key for key in elem.keys()])
                if self.source in elem:
                    for item in feed.get('item'):
                        if item not in json_dicts[counter].get(self.source)[0].get('item'):
                            json_dicts[counter].get(self.source)[0].get('item').append(item)
                counter += 1

            logger.debug(f'URL used list - {url_list}')
            if [self.source] not in url_list:
                json_dicts.append({self.source: [feed]})

        with open(self.cache_file_path, "w", encoding="utf-8") as cache_file:
            json.dump(json_dicts, cache_file, indent=4, ensure_ascii=False)

    def get_cache_data(self, date: int) -> dict:
        """
        Creates dictionary of news from the repository (db.json) published on a specific date.
        :param date: value date in %Y%m%d format
        :return: dict containing news from repository (db.json)
        """
        out_dict_source = {'item': []}
        out_dict_all = {'item': []}
        
        with open(self.cache_file_path, "r", encoding="utf-8") as cache_file:
            json_content = cache_file.read()
            json_dicts = json.loads(json_content)
            
            if self.source:
                counter_dict_source_pos = 0
                for elem in json_dicts:
                    if self.source in elem:
                        for item in json_dicts[counter_dict_source_pos].get(self.source)[0].get('item'):
                            if date == Cacher.get_convert_date(item['pubDate']):
                                out_dict_source.get('item').append(item)
                    counter_dict_source_pos += 1
                logger.debug(f'Out dict with source news from cache - {out_dict_source}')
                return out_dict_source
            else:
                counter_dict_all_pos = 0
                for elem in json_dicts:
                    for key in elem.keys():
                        key_url = key
                    for item in elem.get(key_url)[0].get('item'):
                        if date == Cacher._get_convert_date(item['pubDate']):
                            out_dict_all.get('item').append(item)
                    counter_dict_all_pos += 1
                logger.debug(f'Out dict with all news from cache - {out_dict_all}')
                return out_dict_all

    @staticmethod
    def _get_convert_date(date: str) -> int:
        """
        Convert date to %Y%m%d format
        :param date: date in RFC 822 format
        :return: parsed date in %Y%m%d format
        """
        allowed_date_formats = [
            "%a, %d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S %Z",
            "%Y-%m-%dT%H:%M:%SZ",
        ]
        temp_date = None

        for date_format in allowed_date_formats:
            try:
                temp_date = datetime.strptime(date, date_format)
            except ValueError:
                pass
        parsed_date = int(f"{temp_date.year}{temp_date.month:02d}{temp_date.day:02d}")
        return parsed_date
