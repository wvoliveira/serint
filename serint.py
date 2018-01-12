#!/usr/bin/env python3.5

import selenium.webdriver as webdriver
import time
import random
import logging
import sys
import argparse
import configparser
import json

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="Procura algo em algum mecanismo de busca e tira print. Simples!")
parser.add_argument('-c', '--config', metavar='\b', help='config file', required=True)
args = parser.parse_args()


def parser_dict(section):
    config = configparser.ConfigParser()
    config.read(args.config)

    if config.has_section(section):
        items_dict = dict(config.items(section))
        return items_dict
    else:
        logging.error("Variavel '{0}' inexistente no arquivo de configuracao".format(section))
        sys.exit(1)


def main():

    conf = parser_dict('default')
    vagas = json.loads(conf['vagas'])
    pesquisa = conf['pesquisa']

    browser = webdriver.PhantomJS('drivers/phantomjs', service_log_path='logs/phantomjs.log')
    browser.maximize_window()

    while True:

        try:
            random_vaga = vagas[random.randrange(0, len(vagas) - 1)]
            logging.info('Vaga: ' + random_vaga)

            url = '{0}{1}'.format(pesquisa, '+'.join(random_vaga.split()))
            logging.info('Url: ' + url)

            browser.get(url)

            img = 'images/screenshot-{0}.png'.format(int(time.time()))
            logging.info('Img: ' + img)
            browser.save_screenshot(img)

            time.sleep(20)
            browser.get('https://www.google.com.br')
            time.sleep(5)

        except Exception as error:
            logging.error('Erro: ' + str(error))


if __name__ == '__main__':
    main()