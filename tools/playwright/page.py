import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page, Playwright
from typing import Generator
from config import settings, Browser

def initialize_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: str | None = None,
) -> Generator[Page, None, None]:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path=settings.trace_dir.joinpath(f'{test_name}.zip'))


    context.close()
    browser.close()
    allure.attach.file(settings.trace_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=AttachmentType.WEBM)
