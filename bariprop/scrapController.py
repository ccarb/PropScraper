#from twisted.internet import reactor, defer
#from scrapy.crawler import CrawlerRunner
#from scrapy.utils.log import configure_logging
#from scrapy.utils.project import get_project_settings
import Scraper.spiders
import pkgutil
from win10toast_persist import ToastNotifier
import subprocess

class ScrapController(object):
    newItems=0
    currentSpider='0'
    package=Scraper.spiders
    #configure_logging()
    #runner = CrawlerRunner(get_project_settings())

    #@defer.inlineCallbacks
    #def Crawl():
    #    for importer, spider, ispkg in pkgutil.iter_modules(ScrapController.package.__path__):
    #        ScrapController.currentSpider=spider
    #        yield ScrapController.runner.crawl(str(spider))
    #    reactor.stop()

    def startCrawler():
        print("hello from crawler")
        for importer, spider, ispkg in pkgutil.iter_modules(ScrapController.package.__path__):
            subprocess.run('scrapy crawl ' + spider, shell=True)#MAKE SCRAPER BINARY
        #ScrapController.Crawl()
        #reactor.run()
        #reactor.signalProcess('KILL')


    def newItem():
        ScrapController.newItems=ScrapController.newItems+1

    def sendNotification():
        if ScrapController.newItems!= 0:
            toaster = ToastNotifier()
            toaster.show_toast("Bariprop","Se encontraron " + str(ScrapController.newItems) + " nuevas propiedades en " + ScrapController.currentSpider,duration=None)
            ScrapController.newItems=0