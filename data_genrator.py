import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "job_seeker.settings")

import django
django.setup()

from bs4 import BeautifulSoup
import requests
from job.models import Category


class Scapp:
    def __init__(self):
        self.categories = Category.objects.all()
        self.main()

    def main(self):
        for category in self.categories:
            url = f"https://www.careerbuilder.com/jobs?keywords=+{'+'.join(category.category_name.split())}&location="
            print(url)
            break


if __name__ == '__main__':
    Scapp()


