import requests
from bs4 import BeautifulSoup
import re

def git_scraper(username):
	url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={username}"

	page = requests.get(url, verify=False)
	languages = {}

	if page.status_code == 200:
		soup = BeautifulSoup(page.content, 'html.parser')
		test = soup.find('svg')

		temp = test.findAll('text')
		temp = temp[1:]


		for x in range(5):
			lg_temp = str(temp[(x * 2)])
			per_temp = str(temp[(x * 2) + 1])

			language = re.search(r'>(.*?)<', lg_temp).group(1)
			percent = re.search(r'>(.*?)<', per_temp).group(1)[:-1]

			languages[language] = percent

	else:
		print(page.status_code)

	return languages

