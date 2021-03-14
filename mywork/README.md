# Step 1: Creating Virtual Environments
    python -m venv venv

# Step 2: Install Scrapy
    pip install scrapy

# Step 3: With Scrapy installed, let’s create a new folder for our project. You can do this in the terminal by running:
    mkdir mywork

# Step 4: Creating a project
    scrapy startproject mywork

# Step 5: How to run our spider
    scrapy crawl mywork -O job_detail.json

# Result crawl data in file job_detail.json
