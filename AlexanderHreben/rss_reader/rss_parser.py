"""Storage module for classes RssParser and Printer"""

import json
import xmltodict
import logging
import config

from getter import GetterXml
import cacher

logger = logging.getLogger('app.rss_parser')


class Printer:
    """Class for printing info"""
    
    @staticmethod
    def print_info(data_to_print: dict):
        """
        Print info in stdout
        :param data_to_print: data for printing
        """

        for item in data_to_print['item']:
            print('\n', "- " * 10, '\n')
            print(f'Title: {item.get("title")}\nData: {item.get("pubDate")}\nLink: {item.get("link")}')
            # if item.get("description"):
            #     print(f'\nDescription: {item.get("description")}')
            # print(f'\n\nLinks:\n[1]: {item.get("link")}\n[2]: {item.get("media:thumbnail").get("@url")}')

    @staticmethod
    def print_info_json(data_to_print: dict):
        """
        Print info in json format
        :param data_to_print: data for printing
        """

        for item in data_to_print['item']:
            item_in_json = json.dumps(item, ensure_ascii=False).encode('utf8')
            print('\n', "- " * 10, '\n')
            print(item_in_json.decode())


class RssParser:
    """Class for parsing response received by getter.py and printing result"""

    @staticmethod
    def parse_xml(args) -> dict:
        """
        Transform XML data to dict
        :arg args: set of arguments
        :return: dictionary with XLM data
        """
        data_dict_input = xmltodict.parse(GetterXml().get_response(args.source).text, encoding='utf-8')
        logger.debug(data_dict_input)
        data_dict_out = {"item": []}

        for item in data_dict_input['rss']['channel']['item']:
            data_dict_out['item'].append(
                {"title": item.get("title"), "pubDate": item.get("pubDate"),
                 "link": item.get("link")})  # "description": item.get("description")
        logger.debug(f'Out dict - {data_dict_out}')
        return data_dict_out

    @staticmethod
    def limit(data: dict, limit: int) -> dict:
        out_dict = dict()
        out_dict['item'] = (data['item'][:limit])
        return out_dict

    @staticmethod
    def start():
        """ Start work with rss_parser"""

        args = config.AppArgParser().get_args()

        if args.verbose:
            config.AppLogger.activate_verbose()
            logger.info(f'Verbose mode activated.')

        logger.debug(f'Argparse sent these arguments - {args.__dict__}')

        parser = RssParser()
        logger.info("Module rss_parser is starting.")

        if args.date:
            cache = cacher.Cacher(args.source).get_cache_data(args.date) # все новости из кеша по датам
            limited_cache = RssParser.limit(cache, args.limit) # лимитим и принтим
            Printer().print_info(limited_cache)
        else:
            feed = parser.parse_xml(args)  # тут все новости из рсс
            limited_feed = RssParser.limit(feed, args.limit) # лимитим
            cacher.Cacher(args.source).cache(limited_feed) # кэшируем
            if args.json:
                logger.info(f'Json mode activated.')
                Printer().print_info_json(limited_feed)
            else:
                Printer().print_info(limited_feed)
