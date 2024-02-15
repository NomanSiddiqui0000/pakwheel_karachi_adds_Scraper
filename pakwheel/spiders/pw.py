import scrapy


class PakSpider(scrapy.Spider):
    name = "pw"
    allowed_domains = ["www.pakwheels.com"]
    start_urls = ["https://www.pakwheels.com/used-cars/karachi/24857"]

    def parse(self, response):

        b_url="https://www.pakwheels.com/used-cars/karachi/24857"
        # This spider will scrape 55 pages or 1400 records at a time then the website will block the Spider .You need to change range given the loop below then after combining the data you can run the spider again to scrape the remaining data.In this way you can scrape all the data from the website. For example (2,55),(55,100),(100,150) and so on.
        for page in range(1,457):
 
            r_rul=f"{b_url}?page={page}"
            yield scrapy.Request(url=r_rul,callback=self.parse_add_page)


    def parse_add_page(self, response):
            
            yield{
                "Title":response.css("a.car-name.ad-detail-path>h3 ::text").get(),
                "Price_in_lacs":response.css("div.price-details.generic-dark-grey ::text").get(),
                "Auction-rating":response.css("span.auction-rating ::text").get(),
                "img": response.xpath("//div[@class='total-pictures-bar fs12']/preceding-sibling::img/@src").get(),
                "Model": response.css("ul.list-unstyled.search-vehicle-info-2.fs13 li:nth-child(1) ::text").get(),
                "driven-in_kms":response.css("ul.list-unstyled.search-vehicle-info-2.fs13 li:nth-child(2) ::text").get(),
                "Type":response.css("ul.list-unstyled.search-vehicle-info-2.fs13 li:nth-child(3) ::text").get(),
                "Engine":response.css("ul.list-unstyled.search-vehicle-info-2.fs13 li:nth-child(4) ::text").get(),
                "Transmission_type":response.css("ul.list-unstyled.search-vehicle-info-2.fs13 li:nth-child(5) ::text").get()

            }
