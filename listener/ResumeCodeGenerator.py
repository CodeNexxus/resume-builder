class ResumeDslCodeGenerator:
    def __init__(self):
        self.non_operands = ['resume', 'base_info', 'additional_info',
                             'personal_info', 'summary',
                             'skills',
                             'certificates', 'certificate',
                             'socials','social_list',
                                       'projects',
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
            "<html>\n\n\t<head>\n\t\t<title>Resume</title>\n\t\t"
            "<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">\n\t</head>"
            "\n\n\t<body class=\"t1 background\">"
            "\n\t\t<section class=\"container\">"
            "\n\n\t\t\t<div class=\"header-name\">\n\t\t\t\t<h1>John Doe</h1>\n\t\t\t</div>"
            "\n\n\t\t\t<div class=\"information\">\n\t\t\t\tHERE\n\t\t\t</div>\n\t\t"
            "</section>\n\t</body>\n</html>"
        )
        return base_html.replace("HERE", result)

    def generate_code_based_on_non_operand(self, item):
        if item == "personal_info":
            self.generate_personal_info()

        elif item == "summary":
            self.generate_summrary()

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

        elif item == "skills":
            self.generate_skills()

        elif item == "certificates":
            self.generate_certificates()

        elif item == "certificate":
            self.generate_each_certificate()

        elif item == "socials":
            # print(self.operand_stack)
            # print("hello")
            self.generate_socials()

        elif item == "social_list":
            # print(self.operand_stack)
            self.generate_each_social()

        elif item == "projects":
            self.generate_projects()

        elif item == "work_experience":
            self.generate_work_experience()

        elif item == "educations":
            self.generate_educations()

    def generate_base_info(self):
        personal_code = self.code_stack.pop()
        # socials_code = self.code_stack.pop()

        code_string = (f"\n\t\t\t\t<div class=\"base-info\">"
                       f"{personal_code}\n"
                       f"\n\t\t\t\t</div>")

        self.code_stack.append(code_string)

    def generate_additional_info(self):
        languages = self.code_stack.pop()
        socials_code = self.code_stack.pop()
        soft_skills = self.code_stack.pop()
        hard_skills = self.code_stack.pop()
        summary = self.code_stack.pop()
        # print(summary)

        code_string = (f"\n\t\t\t\t<div class=\"additional-info\">"
                       f"{summary}\n{languages}\n{soft_skills}\n{hard_skills}"
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

        name_code = f"<li>\n\t\t\t\t\t\t\t<strong>name:</strong> \"{name}\"\n\t\t\t\t\t\t</li>"
        surname_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>ser name:</strong> \"{surname}\"\n\t\t\t\t\t\t</li>'
        job_title_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>job title:</strong> \"{job_title}\"\n\t\t\t\t\t\t</li>'
        birth_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>birth:</strong> \"{birth}\"\n\t\t\t\t\t\t</li>'
        phone_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>phone:</strong> \"{phone}\"\n\t\t\t\t\t\t</li>'
        city_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>city:</strong> \"{city}\"\n\t\t\t\t\t\t</li>'
        gmail_code = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>email:</strong> \"{gmail}\"\n\t\t\t\t\t\t</li>'

        temp = name_code + surname_code + job_title_code + birth_code + phone_code + city_code + gmail_code

        personal_image = ('\n\t\t\t\t<div class=\"profile-img\">'
                          '\n\t\t\t\t\t<img src=\"face.jpg\" />\n\t\t\t\t</div>')
        personal_base_code = ('<div>\n\t\t\t\t\t<h2>Personal Info</h2>'
                              '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')
        personal_base_code = personal_base_code.replace("HERE",temp)

        code_string = f"{personal_image}\n\n\t\t\t\t{personal_base_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)

    def generate_socials(self):
        print(self.operand_stack)

        socials_start_code = '<div><h2>Social</h2><ul>'
        socials_end_code = f'</ul></div>{self.hr_spliter}'

        # self.code_stack.append(socials_start_code)
        # self.code_stack.append(socials_end_code)


    def generate_each_social(self):

        name = self.operand_stack.pop()
        # url = self.operand_stack.pop()


        # socials_end_code = self.code_stack.pop()

        each_social = f'<li>{"name"}</li>'

        # self.code_stack.append(each_social)
        # self.code_stack.append(socials_end_code)


    def generate_certificates(self):
        certificates_start_code = ('\n\n\t\t\t\t<div>\n\t\t\t\t\t<h2>Certifications</h2>'
                                   '\n\t\t\t\t\t<ul>')
        certificates_end_code = f'\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}'

        self.code_stack.append(certificates_start_code)
        self.code_stack.append(certificates_end_code)


    def generate_each_certificate(self):
        name = self.operand_stack.pop()
        institution = self.operand_stack.pop()
        link = self.operand_stack.pop()

        certificate_end_code = self.code_stack.pop()

        each_social = f'<li>{name}-{institution}</li>'

        self.code_stack.append(each_social)
        self.code_stack.append(certificate_end_code)


    def generate_summrary(self):
        summary = self.operand_stack.pop()
        summary_code = (f'\n\n\t\t\t\t<div>\n\t\t\t\t\t<h2>Summary</h2>'
                        f'\n\t\t\t\t\t<p class="non-styled-list">{summary}</p>'
                        f'\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}')

        self.code_stack.append(summary_code)



    def generate_skills(self):
        pass
    def generate_projects(self):
        pass
    def generate_work_experience(self):
        pass
    def generate_educations(self):
        pass

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

        languages_code = ('<div>\n\t\t\t\t\t<h2>Languages</h2>'
                          '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')

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
        element = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>soft_skills_item</strong>\n\t\t\t\t\t\t</li>'
        code_items = ""
        for soft_skill in soft_skills:
            code_items += element.replace("soft_skills_item", soft_skill)

        soft_skill_code = ('<div>\n\t\t\t\t\t<h2>Soft Skills</h2>'
                           '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')

        soft_skill_code = soft_skill_code.replace("HERE", code_items)

        code_string = f"\n\n\t\t\t\t{soft_skill_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)

    def generate_hard_skills(self):
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
        element = f'\n\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t<strong>hard_skills_item</strong>\n\t\t\t\t\t\t</li>'
        code_items = ""
        while len(hard_skills) > 0:
            hard_skill_name = hard_skills.pop()
            hard_skill_rate = hard_skills.pop()
            code_items += element.replace("hard_skills_item", f"{hard_skill_name},{hard_skill_rate}")

        hard_skill_code = ('<div>\n\t\t\t\t\t<h2>Hard Skills</h2>'
                           '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')

        hard_skill_code = hard_skill_code.replace("HERE", code_items)

        code_string = f"\n\n\t\t\t\t{hard_skill_code}\n\n\t\t\t\t{self.hr_spliter}"

        self.code_stack.append(code_string)





    # def generate_program(self):
    #     placements_code = self.code_stack.pop()
    #     initiate_code = self.code_stack.pop()
    #     output_type = 'console'
    #     hints_enabled = False
    #     while self.code_stack:
    #         temp_code = self.code_stack.pop()
    #         if temp_code.startswith('##COMPILER_PARAM:::output_type:::'):
    #             output_type = temp_code.replace('##COMPILER_PARAM:::output_type:::', '')
    #         elif temp_code.startswith('##COMPILER_PARAM:::hint:::'):
    #             hints_enabled = temp_code.replace('##COMPILER_PARAM:::hint:::', '') == 'True'
    #         else:
    #             self.code_stack.append(temp_code)
    #             break

    #     if output_type == 'console':
    #         program_code = initiate_code + placements_code
    #         if hints_enabled:
    #             program_code += self.generate_hint_code()
    #         program_code += self.generate_print_code(hints_enabled)
    #         self.code_stack.append(program_code)

    # def generate_initiate_game(self):
    #     height = int(self.operand_stack.pop())
    #     width = int(self.operand_stack.pop())
    #     code_string = f"bombs = [[False for y in range({height})] for x in range({width})]\n"
    #     self.code_stack.append(code_string)

    # def generate_bomb(self):
    #     y = int(self.operand_stack.pop())
    #     x = int(self.operand_stack.pop())
    #     code_string = f"bombs[{x - 1}][{y - 1}] = True\n"
    #     self.code_stack.append(code_string)

    # def set_output_type(self):
    #     self.code_stack.append(f"##COMPILER_PARAM:::output_type:::{self.operand_stack.pop()}")

    # def generate_bomb_placements(self):
    #     temp_block_stack = []
    #     current_code = self.code_stack.pop()
    #     if current_code != '##COMPILER_PARAM:::scope:::end_scope_operator':
    #         self.code_stack.append(current_code)
    #         return
    #     while current_code != '##COMPILER_PARAM:::scope:::begin_scope_operator':
    #         current_code = self.code_stack.pop()
    #         temp_block_stack.append(current_code)
    #     temp_block_stack.pop()
    #     result = ''
    #     while len(temp_block_stack) != 0:
    #         result = result + temp_block_stack.pop()
    #     self.code_stack.append(result)

    # def generate_begin_scope_operator(self):
    #     self.code_stack.append("##COMPILER_PARAM:::scope:::begin_scope_operator")

    # def generate_end_scope_operator(self):
    #     self.code_stack.append("##COMPILER_PARAM:::scope:::end_scope_operator")

    # def generate_hint(self):
    #     self.code_stack.append(f"##COMPILER_PARAM:::hint:::{self.operand_stack.pop()}")

