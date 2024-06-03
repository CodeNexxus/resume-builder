from front.html import generate_html_from_resume_file


if __name__ == '__main__':
    html = generate_html_from_resume_file('input.dsl')
    with open('resume.html', 'w') as f:
        f.write(html)
