from webdriver import Browser
from conftest import config_browser, get_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.main_page import MainPage
from Pages.chapter_page import ChapterPage
from parsing import BibleChapter

if '__main__' == __name__:
    # Preparig browser
    config_browser_data = config_browser()
    browser_i = Browser(config_browser_data)
    WebDriverWait(browser_i.driver, browser_i.wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    data = get_data()
    main_page = MainPage(browser_i.wait_time, start_url=data['start_url'])
    main_verified = main_page.verify_page()
    main_page.go_to_parsing_page()
    chapter_page = ChapterPage(browser_i.wait_time)
    chapter_verified = chapter_page.verify_page()
    work_chapter = BibleChapter(file=data["save_file"])
    work_chapter.prepare_full_verse_file()
    while chapter_verified:
        work_chapter.full_verses()
        chapter_verified = chapter_page.verify_page()
        chapter_page.go_to_next_chapter()
