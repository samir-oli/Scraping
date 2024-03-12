import pandas as pd
import scrapy

class data_analyst(scrapy.Spider):
    name = "dataanalyst"
    allowed_domains = ["www.reed.co.uk"]
    start_urls = ["https://www.reed.co.uk/jobs/data-analyst-jobs?hideTrainingJobs=true"]

    def parse(self, response):
        base_url = "https://www.reed.co.uk"
        
        # Extracting job cards
        job_cards = response.css('article.job-card_jobCard__MkcJD')
        
        for job_card in job_cards:
            # Extracting detail URL
            detail_url = base_url + job_card.css('a::attr(href)').get()
            
            # Extracting title
            title = job_card.css('a::text').get().strip()

            # Extracting salary, location, contract type, and job type
            

            metadata_items = job_card.css('.job-card_jobMetadata__gjkG3 li')
            salary = metadata_items[0].css('::text').get()

            location = metadata_items[1].css('::text').get()
            contract_type, job_type = metadata_items[2].css('::text').get().split(', ')

            yield {
                'URL': detail_url,
                'Title': title,
                'Salary': salary,
                'Contract Type': contract_type,
                'Job Type': job_type,
                'Address': location
            }

        # pagination for the jobs 
        next_page = response.css('[aria-label="Next page"]::attr(href)').get()
        if next_page:
            next_page_url = base_url + next_page
            yield response.follow(next_page_url, callback=self.parse)
