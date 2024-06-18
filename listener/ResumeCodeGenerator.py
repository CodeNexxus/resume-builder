class ResumeDslCodeGenerator:
    def __init__(self):
        self.non_operands = ['resume','personal_info', 'summary',
                             'skills', 
                             'certificates', 'certificate',
                             'socials','social',
                             'projects',
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
            if not self.is_operand(item["label"]):
                self.generate_code_based_on_non_operand(item["label"])
            else:
                self.operand_stack.append(item["label"])

        result = ''
        for code_string in self.code_stack:
            if code_string is not None:
                result += code_string


        base_html = (
            "<html><head><title>Resume</title><link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\"></head>"
            "<body class=\"t1 background\"><section class=\"container\">"
            "<div class=\"header-name\"><h1>John Doe</h1></div>"
            "<div class=\"information\">HERE</div>"
            "</section></body></html>"
        )
        return base_html.replace("HERE", result)

    def generate_code_based_on_non_operand(self, item):
        if item == "personal_info":
            self.generate_personal_info()

        elif item == "summary":
            self.generate_summrary()

        elif item == "skills":
            self.generate_skills()

        elif item == "certificates":
            self.generate_certificates()

        elif item == "certificate":
            self.generate_each_certificate()

        elif item == "socials":
            self.generate_socials()

        elif item == "social":
            self.generate_each_social()

        elif item == "projects":
            self.generate_projects()

        elif item == "work_experience":
            self.generate_work_experience()

        elif item == "educations":
            self.generate_educations()

    def generate_personal_info(self):
        name = self.operand_stack.pop()
        surname = self.operand_stack.pop()

        job_title = self.operand_stack.pop()
        phone = self.operand_stack.pop()

        city = self.operand_stack.pop()
        gmail = self.operand_stack.pop()

        birth = self.operand_stack.pop()

        name_code = f'<li><strong>name:</strong> "{name}"</li>'
        surname_code = f'<li><strong>ser name:</strong> "{surname}"</li>'
        job_title_code = f'<li><strong>job title:</strong> "{job_title}"</li>'
        birth_code = f'<li><strong>birth:</strong> "{birth}"</li>'
        phone_code = f'<li><strong>phone:</strong> "{phone}"</li>'
        city_code = f'<li><strong>city:</strong> "{city}"</li>'
        gmail_code = f'<li><strong>email:</strong> "{gmail}"</li>'

        temp = name_code + surname_code + job_title_code + birth_code + phone_code + city_code + gmail_code

        

        personal_base_code = '<div><h2>Personal Info</h2><ul>HERE</ul></div>'
        personal_base_code = personal_base_code.replace("HERE",temp)

        code_string = f"{personal_base_code}{self.hr_spliter}"

        self.code_stack.append(code_string)
    
    def generate_socials(self):
        socials_start_code = '<div><h2>Social</h2><ul>'
        socials_end_code = f'</ul></div>{self.hr_spliter}'

        self.code_stack.append(socials_start_code)
        self.code_stack.append(socials_end_code)

      
    def generate_each_social(self):
        name = self.operand_stack.pop()
        url = self.operand_stack.pop()

        socials_end_code = self.code_stack.pop()

        each_social = f'<li>{name}</li>'

        self.code_stack.append(each_social)
        self.code_stack.append(socials_end_code)

    
    def generate_certificates(self):
        certificates_start_code = '<div><h2>Certifications</h2><ul>'
        certificates_end_code = f'</ul></div>{self.hr_spliter}'

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
        summary_code = f'<div><h2>Summary</h2><p class="non-styled-list">{summary}</p></div>'

        self.code_stack.append(summary_code)



    def generate_skills(self):
        pass
    def generate_projects(self):
        pass
    def generate_work_experience(self):
        pass
    def generate_educations(self):
        pass










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

