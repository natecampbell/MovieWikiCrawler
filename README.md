# MovieWikiCrawler
Get movie details from Movie Wikipedia (US) pages and save to CSV

## Usage
```
scrapy crawl movie_details -a urls='https://en.wikipedia.org/wiki/some_film,https://en.wikipedia.org/wiki/some_other_film' -o save_file.csv -t csv
```