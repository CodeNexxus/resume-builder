import requests
from bs4 import BeautifulSoup
from bidi.algorithm import get_display
import arabic_reshaper

def get_required_skills(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    info_boxes = soup.find_all('ul', class_='c-infoBox')

    skills = []
    for info_box in info_boxes:
        for item in info_box.find_all('li', class_='c-infoBox__item'):
            title = item.find('h4', class_='c-infoBox__itemTitle')
            if title and title.get_text(strip=True) == 'مهارت‌های مورد نیاز':
                skill_tags = item.find('div', class_='tags').find_all('span', class_='black')
                for skill_tag in skill_tags:
                    skill_text = skill_tag.get_text(strip=True)
                    reshaped_text = arabic_reshaper.reshape(skill_text)  # Reshape text for proper display
                    bidi_text = get_display(reshaped_text)  # Apply bidi algorithm for correct text direction
                    skills.append(bidi_text)
                break

    return skills

# job_url = 'https://jobinja.ir/companies/arian-tadbir-1/jobs/As5o/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-back-end-developer-%D8%AF%D8%B1-%D9%85%D8%AF%DB%8C%D8%B1%DB%8C%D8%AA-%D8%B3%D8%B1%D9%85%D8%A7%DB%8C%D9%87-%D8%A2%D8%B1%DB%8C%D9%86-%D8%AA%D8%AF%D8%A8%DB%8C%D8%B1?_ref=28'
# required_skills = get_required_skills(job_url)
# print("Required Skills:", required_skills)
