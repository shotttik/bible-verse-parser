import random
import string
from bs4 import BeautifulSoup
import re
from webdriver import Browser
import json
from logger import CustomLogger

LOGGER = CustomLogger.get_logger(__name__)


class BibleChapter:
    def __init__(self, file):
        self.id = 0
        self.file = file

    def prepare_full_verse_file(self):
        LOGGER.info("Preparing fullverse file")
        fv = {'verses': []}
        with open(self.file, 'w') as f:
            json.dump(fv, f)
            f.close()

    def _read_full_verses_file(self) -> dict:
        LOGGER.info("Reading fullverse file")
        with open(self.file) as f:
            dictObj = json.load(f)
            f.close()
        return dictObj

    def _write_full_verses_file(self, dictObj: dict) -> bool:
        LOGGER.info("Writing fullverse file")
        with open(self.file, 'w') as f:
            json.dump(dictObj, f)
            f.close()

    def _prepare_verses_text(self, chapter_soup):
        verses_num = int(chapter_soup.find_all(
            'span', class_='label')[-1].text)
        clean_verses = []
        for n in range(1, verses_num+1):
            span_verses = chapter_soup.find_all(
                'span', class_=f"verse v{n}")
            verse_text = ''
            for v in span_verses:
                if v.text == ' ':
                    continue
                verse_text += v.text
            clean_verses.append(verse_text)
        return clean_verses

    def _parse_chapter(self, html):
        LOGGER.info("Started Parsing")
        soup = BeautifulSoup(html, "html.parser")
        chapter_header = soup.find('div', class_='reader').h1.text
        LOGGER.info(f"Parsing {chapter_header}")
        chapter_soup = soup.find('div', class_="chapter")
        # in some chapters we have headers and we are going to remove them
        headings: list = chapter_soup.find_all('span', class_='heading')
        if headings:
            css = str(chapter_soup)
            for heading in headings:
                css = css.replace(str(heading), '')
            chapter_soup = BeautifulSoup(css, 'html.parser')
        clean_sv = self._prepare_verses_text(chapter_soup)
        clean_verses = []
        LOGGER.info("Started cleaning verses")
        for cl in clean_sv:
            part_num = re.search(r"\d+", cl).group()
            description = re.sub(r'^[\d.-]+\s*', '', cl)
            clean_verses.append({
                'id': self.id,
                'title': chapter_header + ':' + part_num,
                'description': description,
            })
            self.id += 1

        return clean_verses

    def full_verses(self):
        dictObj = self._read_full_verses_file()
        html = Browser.getInstance().page_source
        chapter_verses = self._parse_chapter(html)
        dictObj['verses'] += chapter_verses
        self._write_full_verses_file(dictObj)
