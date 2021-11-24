import os
from win10toast import ToastNotifier


class ScrapController(object):
    newItems=0
    currentSpider=''

    def startCrawler():
        spiders = ["escobar","ferraro","losCerros","tratoDirecto"]
        for spider in spiders:
            ScrapController.currentSpider=spider
            ScrapController.newItems=0
            os.system('scrapy crawl '+ spider)
        
    def newItem():
        ScrapController.newItems=ScrapController.newItems+1

    def sendNotification():
        if ScrapController.newItems!= 0:
            toaster = ToastNotifier()
            toaster.show_toast("Bariprop","Se encontraron " + str(ScrapController.newItems) + " nuevas propiedades en " + ScrapController.currentSpider)
