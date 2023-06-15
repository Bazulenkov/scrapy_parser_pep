from pathlib import Path

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = "results"
NUMBER = "number"
NAME = "name"
STATUS = "status"
QTY = "quantity"
DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S"

FEEDS = {
    f"{RESULTS_DIR}/pep_%(time)s.csv": {
        "format": "csv",
        "fields": [NUMBER, NAME, STATUS],
        "overwrite": True,
    },
}
