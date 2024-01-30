
# Pakwheel Karachi adds Scrapy Project

This is simple and easy scrapy project to scrape adds data from pakwheel website. You don't need to apply any changes in setting.py file or add any other libraries rather than scrapy.Scraped data files are also available in spider folder. Pakwheel url: https://www.pakwheels.com/






## Spiders

This project just contain one spider file.

```bash
  pw.py
```


## Requirements

Python3
```bash
  pip install python
```
Scrapy
```bash
  pip install scrapy
```
## Deployment
Ensure that you must be in project directory.
```bash
  cd <project directory>
```
For crawling the spider you need to use this command
```bash
  scrapy crawl pw
  OR
  scrapy crawl -O pw <file name with file format .csv or .json>
```


## Changes required in spider

This web scraper has a drawback – it might get blocked by a website after scraping 56 pages or around 1300 records. This happens because I designed the scraper to be straightforward and easy to use. To overcome this, you just need to make a small change in how the scraper works. Instead of crawling all 56 pages at once, start by scraping pages 1 through 56. After that, start a new loop from the 57th page and continue this process. By doing this, you'll be able to gather data from more than 400 pages. Once you have all this data, combine it into one file for easier use.
```bash
      for page in range(1,457):
```
```bash
      for page in range(56,457):
```
```bash
      for page in range(112,457):
```
```bash
      for page in range(168,457):
```
```bash
      for page in range(224,457):
```
```bash
      for page in range(280,457):
```
```bash
      for page in range(336,457):
```
```bash
      for page in range(392,457):
```
```bash
      for page in range(448,457):
```
