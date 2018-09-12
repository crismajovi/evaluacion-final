import scrapy
import codecs

class QuotesSpider(scrapy.Spider):
    name = "examen"
    def start_requests(self):
        """
        urls = [
            'https://es.fifa.com/worldcup/teams/',
        ]
        """
        archivo = open("data/url.csv", "r")
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        l = response.css('.mw-parser-output')
        tablas = l.xpath('//div/table[1]')
        tr = tablas.xpath('tbody/tr')
        for x in tr:
            lista = x.xpath('td')
            if len(lista) > 0:
                prefe = lista[2].xpath('a/text()')
                provin = lista[3].xpath('a/text()')
                prede = lista[4].xpath('a/text()')
                part = lista[5].xpath('a/text()')
                poseci = lista[6].xpath('a/text()')
                if len(prefe) > 0:
                    prefe = lista[2].xpath('a/text()').extract()[0].strip()
                else:
                    prefe = lista[2].xpath('text()').extract()[0].strip()
                if len(provin) > 0:
                    provin = lista[3].xpath('a/text()').extract()[0].strip()
                else:
                    provin = lista[3].xpath('text()').extract()[0].strip()
                if len(prede) > 0:
                    prede = lista[4].xpath('a/text()').extract()[0].strip()
                else:
                    prede = lista[4].xpath('text()').extract()[0].strip()
                if len(part) > 0:
                    part = lista[5].xpath('a/text()').extract()[0].strip()
                else:
                    part = lista[5].xpath('text()').extract()[0].strip()
                if len(poseci) > 0:
                    poseci = lista[6].xpath('a/text()').extract()[0].strip()
                else:
                    poseci = lista[6].xpath('text()').extract()[0].strip()
                yield {
                    'prefe': prefe,
                    'provin': provin,
                    'prede': prede,
                    'part': part,
                    'poseci': poseci,

                        }