#!/usr/bin/env python3

import json
import locale
import sys
import collections
import os
import operator
import reports
import emails


def load_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):

    locale.setlocale(locale.LC_ALL, "C.UTF-8")
    max_sales = {"total_sales": 0}
    max_revenue = {"revenue": 0}
    car_year_sales = collections.defaultdict(int)

    for item in data:

        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item

        car_year_sales[item["car"]["car_year"]] += item["total_sales"]

    popular_car_year = max(car_year_sales.items(), key=operator.itemgetter(1))
    popular_year, popular_sales = popular_car_year

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(popular_year, popular_sales)]

    return summary


def cars_dict_to_table(car_data):
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(
            item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    data = load_data(os.path.expanduser("~") + "/car_sales.json")
    summary = process_data(data)
    attachment = "/tmp/cars.pdf"
    title = "Sales summary for last month"
    paragraph = "<br/>".join(summary)
    table_data = cars_dict_to_table(data)
    reports.generate(attachment, title, paragraph, table_data)

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get("USER"))
    subject = "Sales summary for last month"
    body = "\n".join(summary)
    message = emails.generate(sender, recipient, subject, body, attachment)
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
