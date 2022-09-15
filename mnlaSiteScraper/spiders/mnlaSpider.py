import scrapy


class MnlaSpider(scrapy.Spider):
    name = 'mnla'
    start_urls = ['https://mn-la.com/collections/new-arrivals']
    

    def parse(self, response):
        # will loop through each object from the array and will be stored within products
        for products in response.css('a.grid-view-item__link'):
            # yield = return in Scrapy
            yield {
                # gets the name of the card listing of currently looped object
                'name': products.css('div.h4.grid-view-item__title::text').get(),
                #  gets the price of the card listing of currently looped object and replacing the '₱' with '' 
                'price': products.css('span.product-price__price::text').get().replace('₱', ''),
                #  gets the href link of the card listing of currently looped object
                'link': 'https://mn-la.com' + products.css('a.grid-view-item__link').attrib['href'],
            }
        
        # searches for next button then gets the link and then enters link when 
        # all products of current page is already parsed
        
        # next_page = 'https://mn-la.com' + response.css('a.grid-view-item__link').getall().extract[-1]()
        # # 
        # if next_page is not None:
        #     # enter next page if there is a link for it
        #     # callback = go back and run the function defined above called parse on the page entered
        #     yield response.follow(next_page, callback=self.parse)