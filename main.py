import requests
from bs4 import BeautifulSoup as bs
import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
stklist = []
# url ='https://chartink.com/screener/15minnotbreak'

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        # print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

    def __del__(self):
        pass
        # print("Object destroyed");


def main():
    page = Page('https://chartink.com/screener/15minnotbreak')
    soup = bs(page.html, 'html.parser')
    js_test = soup.find('table', class_='table table-striped scan_results_table dataTable no-footer')
    columns = []

    for tr in js_test.find_all('tr'):
        columns.append([td.text for td in tr.find_all("td")])

    del columns[0]
    for item in columns:
        stklist.append(item[2])

    message = ''
    # Telegram helper
    for item in stklist:
        message = message + str(item).replace("&", "-") + ' \n'

    telegram_url = 'https://api.telegram.org/bot844712370:AAEjiKL-vokOngeyK3u8Z4vHwuO5czq8Y34/sendMessage?chat_id=-490889260&text=' + message
    requests.post(telegram_url)

    del soup
    del pages
    # sys.exit()
    # del Page.callable
    # del Page._on_load_finished


if __name__ == '__main__': main()