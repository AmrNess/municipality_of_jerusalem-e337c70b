import time

from behave import *

from infra import logger, reporter

log = logger.get_logger(__name__)
rep = reporter.get_reporter()

use_step_matcher("parse")


@When('I wait for "{wait_time:d}" seconds')
def wait_for_seconds_int(context, wait_time):
    time.sleep(wait_time)
