import logging
import os

from selenium import webdriver

from api_models.search import SearchAPI


def before_all(context):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        handlers=[
            logging.FileHandler("logs/test_log.log")  # Logs to file
        ]
    )
    context.logger = logging.getLogger("TestLogger")
    context.logger.info("Tests started")


def before_feature(context, feature):
    context.logger.info(f"Feature '{feature.name}' started")
    if 'api' in feature.tags and 'search' in feature.tags:
        context.search = SearchAPI("https://openlibrary.org/search", context.logger)


def before_scenario(context, scenario):
    context.logger.info(f"Scenario '{scenario.name}' started")
    context.driver = None
    if 'ui' in context.feature.tags:
        context.driver = webdriver.Chrome()
        context.base_url = "https://demowebshop.tricentis.com/"


def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()
    context.logger.info(f"Scenario '{scenario.name}' finished")


def after_feature(context, feature):
    context.logger.info(f"Feature '{feature.name}' finished")


def after_all(context):
    context.logger.info("Tests finished")
