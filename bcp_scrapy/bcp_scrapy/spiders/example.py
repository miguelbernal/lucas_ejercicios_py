# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['bcp.gov.py']
    start_urls = ['https://bcp.gov.py/webapps/web/cotizacion/monedas']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'example-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        
        tabla = response.css('#cotizacion-interbancaria').get()
        with open('example-table.html', 'wb') as f2:
            tabla_b = tabla.encode()
            print(type(tabla_b))
            f2.write(tabla_b)
            
        tabla = response.css('#cotizacion-interbancaria thead').get()
        titulos = response.css('#cotizacion-interbancaria tbody tr th').getall()
        monedas = response.css('#cotizacion-interbancaria tbody tr td').getall()
        print(tabla)
        print(titulos)
        print(monedas)
        
