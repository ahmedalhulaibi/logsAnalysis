# "Database code" for the DB News.

import psycopg2

DBNAME = "news"


def get_popular_articles(num_of_articles):
    """Return most popular articles and number of views."""
    db = psycopg2.connect(dbname=DBNAME)
    curs = db.cursor()
    curs.execute("""select title, logviews.vws
                    from articles left join (
                      select substr(l."path",10) as log_slug, count(*) as vws
                      from log l
                      group by log_slug
                    ) as logviews on logviews.log_slug like slug
                    order by vws desc
                    limit %s;""",
                 (num_of_articles,))
    articles = curs.fetchall()
    curs.close()
    db.close()
    return articles


def get_popular_authors(num_of_authors):
    """Return most popular authors and number of views."""
    db = psycopg2.connect(dbname=DBNAME)
    curs = db.cursor()
    curs.execute("""select au.name, count(*) as vws
                    from authors as au
                    join articles as ar on au.id = ar.author
                    join log as l on substr(l."path",10) like ar.slug
                    group by au.name
                    order by vws desc
                    limit %s;""",
                 (num_of_authors,))
    authors = curs.fetchall()
    curs.close()
    db.close()
    return authors


def get_errs_day_pct(pct):
    """Return days where errs exceed given percentage."""
    db = psycopg2.connect(dbname=DBNAME)
    curs = db.cursor()
    curs.execute("""select errs."day" as "day",
    cast(errs.err_count as decimal) / cast(l.all_count as decimal) * 100
    as percentage
    from (
          select date_trunc('day',"time") as "day", count(*) err_count
          from log
          where log.status like '4%%' or
          log.status like '5%%'
          group by "day"
          order by "day"
        ) as errs
    join (
      select date_trunc('day',"time") as "day", count(*) all_count
      from log
      group by "day"
      order by "day"
    ) as l on l."day" = errs."day" and
    cast(errs.err_count as decimal) / cast(l.all_count as decimal) >= %s;""",
                 (pct,))
    errs = curs.fetchall()
    curs.close()
    db.close()
    return errs
