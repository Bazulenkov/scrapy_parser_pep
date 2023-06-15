import csv
import datetime as dt
import logging
from collections import defaultdict

from settings import RESULTS_DIR, DATETIME_FORMAT, BASE_DIR, STATUS, QTY


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.count_pep_statuses[item.get(STATUS)] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f"status_summary_{now_formatted}.csv"
        file_path = BASE_DIR / RESULTS_DIR / file_name
        total_qty = sum(self.count_pep_statuses.values())
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            fieldnames = [STATUS, QTY]
            writer = csv.DictWriter(f, fieldnames=fieldnames, dialect="unix")
            writer.writeheader()
            for key, value in self.count_pep_statuses.items():
                writer.writerow({STATUS: key, QTY: value})
            writer.writerow({STATUS: "Total", QTY: total_qty})
        logging.info(f"file with results was saved: {file_path}")
