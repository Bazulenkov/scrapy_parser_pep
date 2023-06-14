import csv
import datetime as dt
import logging

from settings import RESULTS_DIR, DATETIME_FORMAT, BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = {}
        self.total = 0

    def process_item(self, item, spider):
        self.total += 1
        try:
            self.counter[item["status"]] += 1
        except KeyError:
            self.counter[item["status"]] = 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f"status_summary_{now_formatted}.csv"
        file_path = BASE_DIR / RESULTS_DIR / file_name
        result = list(self.counter.items())
        result.append(("Total", self.total))
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["Статус", "Количество"]
            writer = csv.DictWriter(f, fieldnames=fieldnames, dialect="unix")
            writer.writeheader()
            for key, value in self.counter.items():
                writer.writerow({"Статус": key, "Количество": value})

        logging.info(f"Файл с результатами был сохранён: {file_path}")
