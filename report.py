#!/usr/bin/env python3
#
# A reporting CLI tool for the news database
from newsdb import get_popular_articles, get_popular_authors, get_errs_day_pct
import sys
import getopt
import datetime

VIEW_TEMPLATE = '''"%s" -- %s views'''
ERR_TEMPLATE = '''%s -- %3.2f%% errors'''


def main(argv):
    print("-----%s Most Popular Articles-----\n" % argv[0])
    articles = "\r\n".join(VIEW_TEMPLATE % (article, views)
                           for article, views in get_popular_articles(argv[0]))
    print(articles)
    print("\n-----%s Most Popular Authors-----\n" % argv[1])
    authors = "\r\n".join(VIEW_TEMPLATE % (author, views)
                          for author, views in get_popular_authors(argv[1]))
    print(authors)
    pct = float(argv[2]) / 100.0
    print("\n-----Days HTTP Error Status Exceeded %3.2f%%-----\n" % (pct*100))
    days = "\r\n".join(ERR_TEMPLATE % (day.strftime("%B %d, %Y"), percentage)
                       for day, percentage in get_errs_day_pct(pct))
    print(days)
    return


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: report.py [num articles] [num authors] [%% errors]")
        quit()
    main(sys.argv[1:])
