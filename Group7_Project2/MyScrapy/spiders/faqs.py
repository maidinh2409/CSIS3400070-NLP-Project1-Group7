import scrapy
from ..items import DouglasFAQItem

class DouglasFAQSpider(scrapy.Spider):
    name = "faqs"
    allowed_domains = ["douglascollege.ca", "www.douglascollege.ca"]

    start_urls = [
        "https://www.douglascollege.ca/current-students/important-dates-information/exam-schedule/final-exam-faq"
    ]

    def parse(self, response):
        questions = response.css("div.douglas-accordion h3.heading")

        for q in questions:
            question = q.xpath("normalize-space(.)").get()

            answer = q.xpath(
                "normalize-space(following-sibling::div[contains(@class, 'panel')][1])"
            ).get()

            if question and answer:
                yield {
                    "question": question,
                    "answer": answer
                }