""" проверки на дату, форматы даты, структура жсона"""

import json
import logging
from datetime import datetime

logger = logging.getLogger('app.cacher')


class Cacher:
    """  """

    def __init__(self, source):
        self.source = source
        self.cache_file_path = "db.json"

    def cache(self, feed: dict):
        """

        :param feed:
        :return:
        """
        with open(self.cache_file_path, "r+", encoding="utf-8") as cache_file:
            json_content = cache_file.read()  # str
            json_dicts = json.loads(json_content)  # list

            # print(type(json_dicts), json_dicts)

            url_list = []
            counter = 0
            for elem in json_dicts:
                url_list.append([key for key in elem.keys()])
                # print('elem', type(elem), elem)

                if self.source in elem:
                    for item in feed.get('item'):
                        # print('item', type(item), item)
                        # print(json_dicts[counter].get(self.source)[0].get('item'))
                        if item not in json_dicts[counter].get(self.source)[0].get('item'):
                            json_dicts[counter].get(self.source)[0].get('item').append(item)
                counter += 1

            logger.debug(f'URL used list - {url_list}')
            if [self.source] not in url_list:
                json_dicts.append({self.source: [feed]})

            # print(type(json_dicts), json_dicts)

        with open(self.cache_file_path, "w", encoding="utf-8") as cache_file:
            json.dump(json_dicts, cache_file, indent=4, ensure_ascii=False)

    def get_cache_data(self, date: int) -> dict:  # если ниче нету бросить ошибку и написать нету
        """

        :param date:
        :return: Dict contain
        """
        out_dict_source = {'item': []}
        out_dict_all = {'item': []}
        with open(self.cache_file_path, "r", encoding="utf-8") as cache_file:
            json_content = cache_file.read()  # str
            json_dicts = json.loads(json_content)  # list
            # print(json_dicts)
            if self.source:
                counter_dict_source_pos = 0
                for elem in json_dicts:  # элемент это словарь из листа со всеми словарями
                    # print('----', elem)
                    if self.source in elem:  # если юрл в ключе то работаем с этим словарем
                        # print(json_dicts[counter].get(self.source)[0].get('item')) - list
                        for item in json_dicts[counter_dict_source_pos].get(self.source)[0].get(
                                'item'):  # итем это итем нужного нам словаря
                            # print(item['pubDate'])
                            if date == Cacher.get_convert_date(item['pubDate']):
                                out_dict_source.get('item').append(item)
                    counter_dict_source_pos += 1
                logger.debug(f'Out dict with source news from cache - {out_dict_source}')
                # print(out_dict_source)
                return out_dict_source
            else:
                counter_dict_all_pos = 0
                for elem in json_dicts:  # дик кажого юрла
                    # print('----', elem)
                    for key in elem.keys():
                        key_url = key
                    # print(elem.get(key_url)[0].get('item'))
                    for item in elem.get(key_url)[0].get('item'):  # итем словаря
                        if date == Cacher.get_convert_date(item['pubDate']):
                            out_dict_all.get('item').append(item)
                    counter_dict_all_pos += 1
                # print(out_dict_all)
                logger.debug(f'Out dict with all news from cache - {out_dict_all}')
                return out_dict_all

    @staticmethod
    def get_convert_date(date: str):
        """

        :param date:
        :return:
        """
        temp_date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")
        parsed_date = int(f"{temp_date.year}{temp_date.month:02d}{temp_date.day:02d}")
        return parsed_date
