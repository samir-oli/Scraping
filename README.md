This repository contains Scrapy project from the job listings of reed jobs (https://www.reed.co.uk/jobs/data-analyst-jobs). This project is focused on extracting various details such as detailed URL ,title ,contract type,job type and location.
Steps to run this project:
clone this project
python3 -m venv env(Set Virtual Environment)
env\Scripts\activate(Activate Virtual Environment)
pip install scrapy(Install Dependencies)
scrapy crawl dataanalyst -o output.json

