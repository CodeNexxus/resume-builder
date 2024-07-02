from .GitScraper import git_scraper
class ResumeDslCodeGenerator:
    def __init__(self):
        self.non_operands = ['resume', 'base_info', 'additional_info', 'git_scraper',
                             'personal_info', 'summary',
                             'skills',
                             'certificates', 'certificate',
                             'socials', 'social_list', 'projects',
                             'languages', 'soft_skills', 'hard_skills',
                             'work_experience', 'educations']
        self.operand_stack = []
        self.code_stack = []
        self.hr_spliter = '<hr class="rounded" />'

    def is_operand(self, item):
        if item in self.non_operands:
            return False
        else:
            return True

    def generate_code(self, post_order_array):

        for item in post_order_array:
            # print(item)
            if not self.is_operand(item["label"]):
                self.generate_code_based_on_non_operand(item["label"])
            else:
                self.operand_stack.append(item["label"])

        result = ''
        for code_string in self.code_stack:
            if code_string is not None:
                result += code_string

        base_html = (
            "<html>\n\n\t<head>"
            "\n\t\t<meta charset=\"utf-8\">\n\t\t<title>Resume</title>\n\t\t"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n\t\t"
            "<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">\n\t</head>"
            "\n\n\t<body class=\"t2 background\">"
            "\n\t\t<section class=\"container\">"
            "\n\n\t\t\t<div class=\"information\">\n\t\t\t\tHERE\n\t\t\t</div>\n\t\t"
            "</section>\n\t</body>\n</html>"
        )
        return base_html.replace("HERE", result)

    def generate_code_based_on_non_operand(self, item):
        if item == "personal_info":
            self.generate_personal_info()

        elif item == "summary":
            self.generate_summary()

        elif item == "git_scraper":
            self.generate_git_scraper()

        elif item == "languages":
            self.generate_languages()

        elif item == "soft_skills":
            self.generate_soft_skills()

        elif item == "hard_skills":
            self.generate_hard_skills()

        elif item == "base_info":
            self.generate_base_info()

        elif item == "additional_info":
            self.generate_additional_info()

        elif item == "certificates":
            self.generate_certificate()

        elif item == "socials":
            self.generate_socials()

        elif item == "projects":
            self.generate_projects()

        elif item == "work_experience":
            self.generate_work_experience()

        elif item == "educations":
            self.generate_educations()

    def generate_base_info(self):
        socials_code = self.code_stack.pop()
        languages = self.code_stack.pop()
        certificate_code = self.code_stack.pop()
        contacts = self.code_stack.pop()
        personal_code = self.code_stack.pop()

        # print(socials_code)

        code_string = (f"\n\t\t\t\t<div class=\"base-info\">"
                       f"{personal_code}\n{certificate_code}\n{socials_code}\n{contacts}"
                       f"\n\t\t\t\t</div>")

        self.code_stack.append(code_string)

    def generate_additional_info(self):
        educations = self.code_stack.pop()
        experience = self.code_stack.pop()
        projects_code = self.code_stack.pop()
        languages = self.code_stack.pop()
        soft_skills = self.code_stack.pop()
        hard_skills = self.code_stack.pop()
        summary = self.code_stack.pop()
        # print(languages)

        code_string = (f"\n\t\t\t\t<div class=\"additional-info\">"
                       f"{summary}\n{languages}\n{soft_skills}\n{hard_skills}\n{projects_code}\n"
                       f"{experience}\n{educations}"
                       f"\n\t\t\t\t</div>")

        self.code_stack.append(code_string)

    def generate_personal_info(self):
        self.operand_stack.pop()
        birth = self.operand_stack.pop()

        self.operand_stack.pop()
        gmail = self.operand_stack.pop()

        self.operand_stack.pop()
        city = self.operand_stack.pop()

        self.operand_stack.pop()
        phone = self.operand_stack.pop()

        self.operand_stack.pop()
        job_title = self.operand_stack.pop()

        self.operand_stack.pop()
        surname = self.operand_stack.pop()

        self.operand_stack.pop()
        name = self.operand_stack.pop()

        name_code = f"<li>\n\t\t\t\t\t\t\t<strong>name:</strong> {name}\n\t\t\t\t\t\t</li>"
        surname_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>surname:</strong> {surname}\n\t\t\t\t\t\t</li>'
        birth_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>birth:</strong> {birth}\n\t\t\t\t\t\t</li>'
        city_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>city:</strong> {city}\n\t\t\t\t\t\t</li>'

        temp = name_code + surname_code + birth_code + city_code

        personal_image = ('\n\t\t\t\t<div class=\"profile-img\">'
                          '\n\t\t\t\t\t<img src=\"face.jpg\" />\n\t\t\t\t</div>')
        personal_base_code = (f'<div>\n\t\t\t\t\t<h2 class="base-item">{job_title}</h2>'
                              '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')
        personal_base_code = personal_base_code.replace("HERE",temp)

        code_string = f"{personal_image}\n\n\t\t\t\t{personal_base_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)

        phone_code = (f'\n\t\t\t\t\t\t<div class="info-title">\n\t\t\t\t\t\t\t'
                      f'<img class="base-info-icon" src="icons/icons8-phone.svg" alt="phone icon">'
                      f'\n\t\t\t\t\t\t\t<a class="link-white" href="{phone}">{phone}</a>\n\t\t\t\t\t\t</div>')

        gmail_code = (f'\n\t\t\t\t\t\t<div class="info-title">\n\t\t\t\t\t\t\t'
                      f'<img class="base-info-icon" src="icons/icons8-gmail.svg" alt="gmail icon">'
                      f'\n\t\t\t\t\t\t\t<a class="link-white" href="{gmail}">{gmail}</a>\n\t\t\t\t\t\t</div>')
        temp = phone_code + gmail_code

        contacts_code = (f'<div>\n\t\t\t\t\t<h2 class="base-item">Contacts</h2>'
                        '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')
        contacts_code = contacts_code.replace("HERE", temp)

        code_string = f"{contacts_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)

    def generate_git_scraper(self):
        # print(self.operand_stack)
        self.operand_stack.pop()
        username = self.operand_stack.pop().replace(" ","")
        languages = git_scraper(username)
        # languages = {}
        cl_start_code = '\n\t\t\t\t\t<div>\n\t\t\t\t\t\t<h2 class="base-item">Top Five Languages</h2>\n\t\t\t\t\t\t<ul>'
        cl_end_code = f'\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t{self.hr_spliter}'

        code_temp = cl_start_code
        for lan in languages:
            number = (float(languages[lan]) % 3) + 1

            element = (f'\n\t\t\t\t\t\t<div class="additional-info-item">\n\t\t\t\t\t\t\t'
                       f'<li>\n\t\t\t\t\t\t\t\t<strong>hard_skills_item</strong>\n\t\t\t\t\t\t</li>'
                       f'\n\t\t\t\t\t\t\t<div class="rate">rating-skill\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>')

            fill_star = '\n\t\t\t\t\t\t\t\t<img class="rate-star" src="icons/filled star.svg" alt="">'
            empty_star = '\n\t\t\t\t\t\t\t\t<img class="rate-star" src="icons/star (1).svg" alt="">'

            temp_code = element.replace("hard_skills_item", lan)
            rating_code = fill_star * int(number) + empty_star * (3 - int(number))
            temp_code = temp_code.replace("rating-skill", rating_code)
            code_temp += temp_code

        code_temp += cl_end_code

        self.code_stack.append(code_temp)

    def generate_socials(self):
        # print(self.operand_stack)

        socials_start_code = '\n\t\t\t\t\t<div>\n\t\t\t\t\t\t<h2 class="base-item">Social</h2>\n\t\t\t\t\t\t<ul>'
        socials_end_code = f'\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t{self.hr_spliter}'

        code_temp = socials_start_code

        temp = ""
        self.operand_stack.pop()
        while True:
            self.operand_stack.pop()  # social

            self.operand_stack.pop()  # link
            link = self.operand_stack.pop()

            # self.operand_stack.pop()  # name
            name = self.operand_stack.pop()


            each_social = (f'\n\t\t\t\t\t\t\t<div class="info-title">'
                           f'\n\t\t\t\t\t\t\t\t<a class="link-white" href=\"{link}\">{name}</a>'
                           f'\n\t\t\t\t\t\t\t</div></br>')

            code_temp += each_social

            temp = self.operand_stack.pop()
            if temp == 'begin_scope_operator':
                break
            self.operand_stack.append(temp)

        code_temp += socials_end_code

        self.code_stack.append(code_temp)

    def generate_certificate(self):
        # print(self.operand_stack)

        certificates_start_code = ('\n\n\t\t\t\t<div>\n\t\t\t\t\t<h2>Certifications</h2>'
                                   '\n\t\t\t\t\t<ul>')
        certificates_end_code = f'\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}'

        code_temp = certificates_start_code

        temp = self.operand_stack.pop()
        while True:
            # print(self.operand_stack)
            self.operand_stack.pop()  # link
            link = self.operand_stack.pop()

            self.operand_stack.pop()  # institution
            institution = self.operand_stack.pop()

            self.operand_stack.pop()  # name
            name = self.operand_stack.pop()

            # print(link)
            # print(name)

            each_social = f'\n\t\t\t\t\t\t<li><a href=\"{link}\">{name}-{institution}</a></li>'
            code_temp += each_social

            temp = self.operand_stack.pop()
            if len(self.operand_stack) == 0 or temp == 'begin_scope_operator':
                break
            self.operand_stack.append(temp)

        code_temp += certificates_end_code

        self.code_stack.append(code_temp)

    def generate_summary(self):
        summary = self.operand_stack.pop()
        summary_code = (f'\n\n\t\t\t\t<div class="info-item">\n\t\t\t\t\t'
                        f'<div class="additional-info-title">\n\t\t\t\t\t\t'
                        f'<img class="additioan-info-titles-icon" src="icons/info.svg" alt="about icon">'
                        f'<h2>About Me</h2>\n\t\t\t\t\t</div>'
                        f'\n\t\t\t\t\t<p class="non-styled-list text">{summary}</p>'
                        f'\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}')

        self.code_stack.append(summary_code)

    def generate_projects(self):
        # print(self.operand_stack)
        projects_start_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title">'
                               '\n\t\t\t\t\t<img class=\"additioan-info-titles-icon\" src=\"icons/diagram-project.svg\" '
                               'alt=\"Projects title icon\">'
                               '\n\t\t\t\t\t<h2>Projects</h2>\n\t\t\t\t\t</div>'
                               '\n\t\t\t\t\t<ul class="projects">\n\t\t\t\t\t\t')

        projects_end_code = f'\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}'

        code_temp = projects_start_code

        temp = ""
        self.operand_stack.pop()
        while True:
            self.operand_stack.pop()  # project

            self.operand_stack.pop()  # url
            link = self.operand_stack.pop()

            self.operand_stack.pop()  # description
            description = self.operand_stack.pop()

            self.operand_stack.pop()  # title
            title = self.operand_stack.pop()

            title_code = f'\n\t\t\t\t\t\t<div>\n\t\t\t\t\t\t<li><a class="link" href=\"{link}\">{title}</a></li>'
            description_code = f'\n\t\t\t\t\t\t<li><p class="text">{description}</p></li></div>'
            code_temp += title_code + description_code

            temp = self.operand_stack.pop()
            if temp == 'begin_scope_operator' or len(self.operand_stack) == 0:
                break
            self.operand_stack.append(temp)

        code_temp += projects_end_code

        self.code_stack.append(code_temp)

    def generate_work_experience(self):
        # print(self.operand_stack)
        work_experience_start_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title">'
                                      '\n\t\t\t\t\t<img class=\"additioan-info-titles-icon\" '
                                      'src=\"icons/diagram-project.svg\" '
                                      'alt=\"experience title icon\">'
                                      '\n\t\t\t\t\t<h2>Experience</h2>\n\t\t\t\t\t</div>'
                                      '\n\t\t\t\t\t<ul class="educations">\n\t\t\t\t\t\t')
        work_experience_end_code = f'\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}'

        code_temp = work_experience_start_code

        temp = ""
        self.operand_stack.pop()
        while True:
            self.operand_stack.pop()  # job

            self.operand_stack.pop()  # responsibilities

            self.operand_stack.pop()  # end_scope_operator
            responsibility = ""
            while True:
                self.operand_stack.pop()  # responsibility
                responsibility = f"{self.operand_stack.pop()}{responsibility}"
                temp = self.operand_stack.pop()
                if temp == 'begin_scope_operator':
                    break
                self.operand_stack.append(temp)

            self.operand_stack.pop()  # end_date
            end_date = self.operand_stack.pop()

            self.operand_stack.pop()  # start_date
            start_date = self.operand_stack.pop()

            self.operand_stack.pop()  # position
            position = self.operand_stack.pop()

            self.operand_stack.pop()  # company
            company = self.operand_stack.pop()

            position_code = f'\n\t\t\t\t\t\t<div>\n\t\t\t\t\t\t\t<li>{position}</li>'
            company_code = f'\n\t\t\t\t\t\t<p class="text">{company}</p>'
            from_code = f'\n\t\t\t\t\t\t<p class="text">From {start_date} to {end_date}</p>'
            text_code = (f'\n\t\t\t\t\t\t<p class="text">{responsibility}</p>'
                         f'\n\t\t\t\t\t\t</div>')

            code_temp += position_code + company_code + from_code + text_code

            temp = self.operand_stack.pop()
            if temp == 'begin_scope_operator':
                break
            self.operand_stack.append(temp)

        code_temp += work_experience_end_code

        self.code_stack.append(code_temp)

    def generate_educations(self):
        # print(self.operand_stack)
        educations_start_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title">'
                                 '\n\t\t\t\t\t<img class=\"additioan-info-titles-icon\" '
                                 'src=\"icons/user-graduate.svg\" '
                                 'alt=\"Projects title icon\">'
                                 '\n\t\t\t\t\t<h2>Educations</h2>\n\t\t\t\t\t</div>'
                                 '\n\t\t\t\t\t<ul class="educations">\n\t\t\t\t\t\t')

        educations_end_code = f'\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}'

        code_temp = educations_start_code

        temp = ""
        self.operand_stack.pop()
        while True:
            self.operand_stack.pop()  # education

            self.operand_stack.pop()  # end_date
            end_date = self.operand_stack.pop()

            self.operand_stack.pop()  # start_date
            start_date = self.operand_stack.pop()

            self.operand_stack.pop()  # institution
            degree = self.operand_stack.pop()

            self.operand_stack.pop()  # institution
            institution = self.operand_stack.pop()

            degree_code = f'\n\t\t\t\t\t\t<div>\n\t\t\t\t\t\t\t<li>{degree}</li>'
            institution_code = f'\n\t\t\t\t\t\t<p class="text">{institution}</p>'
            from_code = (f'\n\t\t\t\t\t\t<p class="text">From {start_date} to {end_date}</p>'
                         f'\n\t\t\t\t\t\t</div>')

            code_temp += degree_code + institution_code + from_code

            temp = self.operand_stack.pop()
            if temp == 'begin_scope_operator':
                break
            self.operand_stack.append(temp)

        code_temp += educations_end_code

        self.code_stack.append(code_temp)

    def generate_languages(self):
        temp = self.operand_stack.pop()
        languages = []
        if temp == 'end_scope_operator':
            while temp != 'begin_scope_operator':
                temp = self.operand_stack.pop()
                if temp == 'language':
                    continue
                languages.append(temp)
        else:
            pass

        languages.pop()

        # print(languages)
        element = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>Language_item</strong>\n\t\t\t\t\t\t</li>'
        code_items = ""
        for language in languages:
            code_items += element.replace("Language_item", language)

        languages_code = ('<div class=\"info-item\">'
                          '\n\t\t\t\t\t<div class="additional-info-title">'
                          '\n\t\t\t\t\t\t<img class="additioan-info-titles-icon" src="icons/language.svg" '
                          'alt="languages title icon">'
                          '\n\t\t\t\t\t\t<h2>Languages</h2>'
                          '\n\t\t\t\t\t</div>'
                          '\n\t\t\t\t\t<ul class="additional-info-list">'
                          '\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')

        languages_code = languages_code.replace("HERE", code_items)

        code_string = f"\n\n\t\t\t\t{languages_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)

    def generate_soft_skills(self):
        temp = self.operand_stack.pop()
        soft_skills = []
        if temp == 'end_scope_operator':
            while temp != 'begin_scope_operator':
                temp = self.operand_stack.pop()
                if temp == 'soft_skill':
                    continue
                soft_skills.append(temp)
        else:
            pass

        soft_skills.pop()

        # print(soft_skills)
        element = (f'\n\t\t\t\t\t\t<div class="additional-info-item">'
                   f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>soft_skills_item</strong>\n\t\t\t\t\t\t</li>'
                   f'\n\t\t\t\t\t\t</div>')
        code_items = ""
        for soft_skill in soft_skills:
            code_items += element.replace("soft_skills_item", soft_skill)

        soft_skill_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title">'
                           '\n\t\t\t\t\t<img class=\"additioan-info-titles-icon\" src=\"icons/skill-alt.svg\" '
                           'alt=\"languages title icon\">'
                           '\n\t\t\t\t\t<h2>Soft Skills</h2>\n\t\t\t\t\t</div>'
                           '\n\t\t\t\t\t<ul class="additional-info-list">\n\t\t\t\t\t\t'
                           'HERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')

        soft_skill_code = soft_skill_code.replace("HERE", code_items)

        code_string = f"\n\n\t\t\t\t{soft_skill_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)

    def generate_hard_skills(self):
        # print(self.operand_stack)

        temp = self.operand_stack.pop()
        hard_skills = []
        if temp == 'end_scope_operator':
            while temp != 'begin_scope_operator':
                temp = self.operand_stack.pop()
                if temp == 'hard_skill':
                    continue
                hard_skills.append(temp)
        else:
            pass

        hard_skills.pop()

        # print(hard_skills)

        element = (f'\n\t\t\t\t\t\t<div class="additional-info-item">\n\t\t\t\t\t\t\t'
                   f'<li>\n\t\t\t\t\t\t\t\t<strong>hard_skills_item</strong>\n\t\t\t\t\t\t</li>'
                   f'\n\t\t\t\t\t\t\t<div class="rate">rating-skill\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>')

        fill_star = '\n\t\t\t\t\t\t\t\t<img class="rate-star" src="icons/filled star.svg" alt="">'
        empty_star = '\n\t\t\t\t\t\t\t\t<img class="rate-star" src="icons/star (1).svg" alt="">'

        code_items = ""
        while len(hard_skills) > 0:
            hard_skill_name = hard_skills.pop()
            hard_skill_rate = hard_skills.pop()
            temp_code = element.replace("hard_skills_item", hard_skill_name)
            rating_code = fill_star * int(hard_skill_rate) + empty_star * (5-int(hard_skill_rate))
            temp_code = temp_code.replace("rating-skill",rating_code)
            code_items += temp_code

        hard_skill_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title">'
                           '\n\t\t\t\t\t<img class=\"additioan-info-titles-icon\" src=\"icons/user-skill-gear.svg\" '
                           'alt=\"languages title icon\">'
                           '\n\t\t\t\t\t<h2>Hard Skills</h2>\n\t\t\t\t\t</div>'
                           '\n\t\t\t\t\t<ul class="additional-info-list">\n\t\t\t\t\t\t'
                           'HERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')

        hard_skill_code = hard_skill_code.replace("HERE", code_items)

        code_string = f"\n\n\t\t\t\t{hard_skill_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)

