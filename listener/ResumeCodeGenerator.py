from .GitScraper import git_scraper
from .JobinjaScraper import get_required_skills
from .GenerateCss import GenerateCss


class ResumeDslCodeGenerator:
	def __init__(self):
		self.non_operands = ['resume', 'base_info', 'additional_info', 'git_scraper',
							 'personal_info', 'summary',
							 'skills',
							 'certificates', 'certificate',
							 'socials', 'social_list', 'projects',
							 'languages', 'soft_skills', 'hard_skills',
							 'work_experience', 'educations', 'jobinja_scraper',
							 'go_top', 'autocopy', 'job_title_effect',
							 'collapsable_sections', 'theme_switching', 'tooltip']
		self.operand_stack = []
		self.code_stack = []
		self.hr_spliter = '<hr class="rounded" />'
		self.jobinja_added = False

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
		while True:
			code_string = self.code_stack.pop()
			if code_string == 'FLAG-FOR_JS':
				break
			if code_string is not None:
				result += code_string

		# result_js = ''
		# for code_string in self.js_code_stack:
		#     if code_string is not None:
		#         result_js += code_string

		base_html = (
			"<html>\n\n\t<head>"
			"\n\t\t<meta charset=\"utf-8\">\n\t\t<title>Resume</title>\n\t\t"
			"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n\t\t"
			"<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">\n\t</head>"
			"\n\n\t<body id=\"themeHolder\" class=\"t1 background\">"
			"\n\t\t<section class=\"container\">"
			"\n\n\t\t\t<div class=\"information\">\n\t\t\t\tHERE\n\t\t\t</div>\n\t\t"
			"<!-- snack bar -->\n\t\t\t"
			"<div id=\"email-snackbar\">email saved in clipboared</div>\n\t\t\t"
			"<div id=\"phone-snackbar\">phone saved in clipboared</div>\n\t\t"
			"<!-- end snack bar -->\n\t\t"
			"<!-- go top btn -->\n\t\t"
			"<a href=\"#\" class=\"go-top\">\n\t\t"
			"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"20\" height=\"20\" fill=\"#fff\" "
			"class=\"bi bi-triangle-fill\" viewBox=\"0 0 16 16\">"
			"<path fill-rule=\"evenodd\" d=\"M7.022 1.566a1.13 1.13 0 0 1 1.96 0l6.857 11.667c.457.778"
			"-.092 1.767-.98 1.767H1.144c-.889 0-1.437-.99-.98-1.767z\"/>"
			"</svg>"
			"</a>\n\t\t"
			"<!-- end go top -->\n\t\t"
			"<!-- change theme -->\n\t\t"
			"CHANGE_THEME_PLACE\n\t\t"
			"<!-- end change theme -->\n\t\t"
			"</section>\n\t\t<script src=\"https://cdn.jsdelivr.net/npm/typed.js@2.0.12\">"
			"\n\t\t</script>"
			"\n\t\t<script>scripts_Here"
			"\n\t\t</script>"
			"\n\t</body>\n</html>"
		)
		base_html = base_html.replace("HERE", result)
		base_html = base_html.replace("scripts_Here", self.code_stack.pop())

		temp_theme = ("<div class=\"button-container\"><h3 style=\"margin: 10px 0;\">Themes:</h3>"
					  "<button class=\"change-theme-btn\" onclick=\"changeClass('t1')\">Warm Vanilla</button>"
					  "<button class=\"change-theme-btn\" onclick=\"changeClass('t2')\">Soft Blush</button>"
					  "<button class=\"change-theme-btn\" onclick=\"changeClass('t3')\">Peach Cream</button></div>")

		if self.flag_theme:
			base_html = base_html.replace("CHANGE_THEME_PLACE",temp_theme)
		else:
			base_html = base_html.replace("CHANGE_THEME_PLACE", "")


		css_class = GenerateCss()
		css_file = css_class.generate_code()

		codes = [base_html, css_file]
		return codes

	def generate_code_based_on_non_operand(self, item):
		if item == "resume":
			self.generate_resume()

		elif item == "personal_info":
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

		elif item == "jobinja_scraper":
			self.generate_jobinja_scraper()

		elif item == "go_top":
			self.generate_go_top()

		elif item == "autocopy":
			self.generate_autocopy()

		elif item == "job_title_effect":
			self.generate_job_title_effect()

		elif item == "collapsable_sections":
			self.generate_collapsable_sections()

		elif item == "theme_switching":
			self.generate_theme_switching()

		elif item == "tooltip":
			self.generate_tooltip()

	def generate_resume(self):
		additional_info = self.code_stack.pop()
		base_info = self.code_stack.pop()
		go_top_enabled = False
		autocopy_enabled = False
		job_title_effect_enabled = False
		collapsable_sections_enabled = False
		theme_switching_enabled = False
		tooltip_enabled = False

		while self.code_stack:
			temp_code = self.code_stack.pop()
			if temp_code.startswith('##COMPILER_PARAM:::go_top:::'):
				go_top_enabled = temp_code.replace('##COMPILER_PARAM:::go_top:::', '') == 'True'
			elif temp_code.startswith('##COMPILER_PARAM:::autocopy:::'):
				autocopy_enabled = temp_code.replace('##COMPILER_PARAM:::autocopy:::', '') == 'True'
			elif temp_code.startswith('##COMPILER_PARAM:::job_title_effect:::'):
				job_title_effect_enabled = temp_code.replace('##COMPILER_PARAM:::job_title_effect:::', '') == 'True'
			elif temp_code.startswith('##COMPILER_PARAM:::collapsable_sections:::'):
				collapsable_sections_enabled = temp_code.replace('##COMPILER_PARAM:::collapsable_sections:::',
																 '') == 'True'
			elif temp_code.startswith('##COMPILER_PARAM:::theme_switching:::'):
				theme_switching_enabled = temp_code.replace('##COMPILER_PARAM:::theme_switching:::', '') == 'True'
			elif temp_code.startswith('##COMPILER_PARAM:::tooltip:::'):
				tooltip_enabled = temp_code.replace('##COMPILER_PARAM:::tooltip:::', '') == 'True'
			else:
				self.code_stack.append(temp_code)
				break

		html_code = base_info + additional_info
		program_code = ""
		if go_top_enabled:
			program_code += self.generate_go_top_code()
		if autocopy_enabled:
			program_code += self.generate_autocopy_code()
		if job_title_effect_enabled:
			program_code += self.generate_job_title_effect_code().replace("job_title_for_js", self.job_title_replace)
			html_code = html_code.replace("JS_FLAG_FOR_JOB_TITLE", "")
		else:
			html_code = html_code.replace("JS_FLAG_FOR_JOB_TITLE", self.job_title_replace)
		if collapsable_sections_enabled:
			program_code += self.generate_collapsable_sections_code()
		if theme_switching_enabled:
			program_code += self.generate_theme_switching_code()
			self.flag_theme = True
		else:
			self.flag_theme = False
		if tooltip_enabled:
			program_code += self.generate_tooltip_code()

		flag_for_js = "FLAG-FOR_JS"
		self.code_stack.append(program_code)
		self.code_stack.append(flag_for_js)
		self.code_stack.append(html_code)

	def generate_go_top_code(self):
		return (
			'\n\t\t\t// go top btn'
			'\n\t\t\tconst toTop = document.querySelector(".go-top");'
			'\n\t\t\twindow.addEventListener("scroll", () => {'
			'\n\t\t\tif (window.pageYOffset > 150){'
			'\n\t\t\ttoTop.classList.add("active");'
			'\n\t\t\t} else {toTop.classList.remove("active");}'
			'\n\t\t\t});'
		)

	def generate_autocopy_code(self):
		js_snack_bar_code = ('\n\t\t\tconst email = document.getElementById(\"email\")\n\t\t\t'
							 'email.addEventListener(\'click\', (event) => {\n\t\t\t'
							 'event.preventDefault();\n\t\t\t'
							 'navigator.clipboard.writeText(email.innerHTML);\n\t\t\t'
							 'var x = document.getElementById("email-snackbar");\n\t\t\t'
							 'x.className = "show";\n\t\t\t'
							 'setTimeout(function () {\n\t\t\t'
							 'x.className = x.className.replace("show", "");\n\t\t\t'
							 '}, 3000);\n\t\t\t'
							 '});\n\t\t\t')

		js_snack_bar_code += ('\n\t\t\tconst phone = document.getElementById(\"phone\")\n\t\t\t'
							  'phone.addEventListener(\'click\', (event) => {\n\t\t\t'
							  'event.preventDefault();\n\t\t\t'
							  'navigator.clipboard.writeText(phone.innerHTML);\n\t\t\t'
							  'var x = document.getElementById("phone-snackbar");\n\t\t\t'
							  'x.className = "show";\n\t\t\t'
							  'setTimeout(function () {\n\t\t\t'
							  'x.className = x.className.replace("show", "");\n\t\t\t'
							  '}, 3000);\n\t\t\t'
							  '});\n\t\t\t')

		return js_snack_bar_code

	def generate_job_title_effect_code(self):
		js_code = '\n\t\t\tnew Typed(\'#typed-text\', {\n\t\t\t'
		js_code += (f'strings: [\'job_title_for_js\'],\n\t\t\t'
					f'typeSpeed: 40,\n\t\t\t'
					f'loop: true,\n\t\t\t'
					f'showCursor: false \n\t\t\t')
		js_code += "});\n\t\t\t"
		return js_code

	def generate_collapsable_sections_code(self):
		return ('\n\t\t\t// collapsable sections'
               '\n\t\t\tconst collapsables = document.querySelectorAll(".collapsable");'
               '\n\t\t\tcollapsables.forEach((collapsable) => {'
               '\n\t\t\tcollapsable.addEventListener("click", () => {'
               '\n\t\t\tcollapsable.classList.toggle("active");'
               '\n\t\t\tconst content = collapsable.nextElementSibling;'
               '\n\t\t\tif (content.style.display == "" || content.style.display === "flex") {'
               '\n\t\t\tcontent.style.display = "none";'
               '\n\t\t\t} else {'
               '\n\t\t\tcontent.style.display = "flex";'
               '\n\t\t\t}'
               '\n\t\t\t});'
               '\n\t\t\t});'
		)

	def generate_theme_switching_code(self):
		pass
		return (
			'\n\t\t\tfunction changeClass(newClass) {'
			'\n\t\t\t\tconst div = document.getElementById("themeHolder");'
			'\n\t\t\t\tdiv.className = newClass + " background";'
			'\n\t\t\t}'
		)

	def generate_tooltip_code(self):
		pass

	def generate_go_top(self):
		self.code_stack.append(f"##COMPILER_PARAM:::go_top:::{self.operand_stack.pop()}")

	def generate_autocopy(self):
		self.code_stack.append(f"##COMPILER_PARAM:::autocopy:::{self.operand_stack.pop()}")

	def generate_job_title_effect(self):
		self.code_stack.append(f"##COMPILER_PARAM:::job_title_effect:::{self.operand_stack.pop()}")

	def generate_collapsable_sections(self):
		self.code_stack.append(f"##COMPILER_PARAM:::collapsable_sections:::{self.operand_stack.pop()}")

	def generate_theme_switching(self):
		self.code_stack.append(f"##COMPILER_PARAM:::theme_switching:::{self.operand_stack.pop()}")

	def generate_tooltip(self):
		self.code_stack.append(f"##COMPILER_PARAM:::tooltip:::{self.operand_stack.pop()}")

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
		self.job_title_replace = self.operand_stack.pop()

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
						  '\n\t\t\t\t\t<img src=\"face.jpeg\" />\n\t\t\t\t</div>')
		personal_base_code = (f'<div>\n\t\t\t\t\t<h2 id="typed-text" class="base-item"'
							  f' style="height: 30px">JS_FLAG_FOR_JOB_TITLE</h2>'
							  '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')
		personal_base_code = personal_base_code.replace("HERE", temp)

		code_string = f"{personal_image}\n\n\t\t\t\t{personal_base_code}\n\n\t\t\t\t{self.hr_spliter}"

		self.code_stack.append(code_string)

		phone_code = (f'\n\t\t\t\t\t\t<div class="info-title">\n\t\t\t\t\t\t\t'
					  f'<img class="base-info-icon" src="icons/icons8-phone.svg" alt="phone icon">'
					  f'\n\t\t\t\t\t\t\t<p id="phone" class="link-white" >{phone}</p>\n\t\t\t\t\t\t</div>')

		gmail_code = (f'\n\t\t\t\t\t\t<div class="info-title">\n\t\t\t\t\t\t\t'
					  f'<img class="base-info-icon" src="icons/icons8-gmail.svg" alt="gmail icon">'
					  f'\n\t\t\t\t\t\t\t<p id="email" "class="link-white" >{gmail}</p>\n\t\t\t\t\t\t</div>')
		temp = phone_code + gmail_code

		contacts_code = (f'<div>\n\t\t\t\t\t<h2 class="base-item">Contacts</h2>'
						 '\n\t\t\t\t\t<ul>\n\t\t\t\t\t\tHERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')
		contacts_code = contacts_code.replace("HERE", temp)

		code_string = f"{contacts_code}\n\n\t\t\t\t{self.hr_spliter}"

		self.code_stack.append(code_string)

	def generate_git_scraper(self):
		# print(self.operand_stack)
		self.operand_stack.pop()
		username = self.operand_stack.pop().replace(" ", "")
		languages = git_scraper(username)
		# languages = {}
		cl_start_code = '\n\t\t\t\t\t<div>\n\t\t\t\t\t\t<h2 class="base-item">Top Five GitHub</h2>\n\t\t\t\t\t\t<ul>'
		cl_end_code = f'\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t{self.hr_spliter}'

		code_temp = cl_start_code
		for lan in languages:
			number = (float(languages[lan]) % 3) + 1

			element = (f'\n\t\t\t\t\t\t<div class="additional-info-item">\n\t\t\t\t\t\t\t'
					   f'<li>\n\t\t\t\t\t\t\t\t<strong>hard_skills_item</strong>\n\t\t\t\t\t\t</li>'
					   f'\n\t\t\t\t\t\t\t<div class="rate">rating-skill\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>')

			fill_star = '\n\t\t\t\t\t\t\t\t<img class="rate-star" src="icons/wstarfilled.svg" alt="">'
			empty_star = '\n\t\t\t\t\t\t\t\t<img class="rate-star" src="icons/wstar.svg" alt="">'

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
			link = self.operand_stack.pop().strip().strip('"')

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
						f'<div class="additional-info-title collapsable">\n\t\t\t\t\t\t'
						f'<img class="additioan-info-titles-icon" src="icons/info.svg" alt="about icon">'
						f'<h2>About Me</h2>\n\t\t\t\t\t</div>'
						f'\n\t\t\t\t\t<p class="non-styled-list text">{summary}</p>'
						f'\n\t\t\t\t</div>\n\n\t\t\t\t{self.hr_spliter}')

		self.code_stack.append(summary_code)

	def generate_projects(self):
		# print(self.operand_stack)
		projects_start_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title collapsable">'
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
			link = self.operand_stack.pop().strip().strip('"')

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
		work_experience_start_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title collapsable">'
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
		educations_start_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title collapsable">'
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
						  '\n\t\t\t\t\t<div class="additional-info-title collapsable">'
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

		soft_skill_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title collapsable">'
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

		for x in range(len(hard_skills)):
			hard_skills[x] = hard_skills[x].replace(" ","")

		temp = self.operand_stack.pop()
		while temp != 'optional_features':
			if temp in hard_skills:
				temp = self.operand_stack.pop()
				continue
			hard_skills.append('3')
			hard_skills.append(temp)
			temp = self.operand_stack.pop()

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
			rating_code = fill_star * int(hard_skill_rate) + empty_star * (5 - int(hard_skill_rate))
			temp_code = temp_code.replace("rating-skill", rating_code)
			code_items += temp_code

		hard_skill_code = ('<div class="info-item">\n\t\t\t\t\t<div class="additional-info-title collapsable">'
						   '\n\t\t\t\t\t<img class=\"additioan-info-titles-icon\" src=\"icons/user-skill-gear.svg\" '
						   'alt=\"languages title icon\">'
						   '\n\t\t\t\t\t<h2>Hard Skills</h2>\n\t\t\t\t\t</div>'
						   '\n\t\t\t\t\t<ul class="additional-info-list">\n\t\t\t\t\t\t'
						   'HERE\n\t\t\t\t\t</ul>\n\t\t\t\t</div>')

		hard_skill_code = hard_skill_code.replace("HERE", code_items)

		code_string = f"\n\n\t\t\t\t{hard_skill_code}\n\n\t\t\t\t{self.hr_spliter}"

		self.code_stack.append(code_string)

	def generate_jobinja_scraper(self):
		# print(self.operand_stack)
		_ = self.operand_stack.pop()
		job_url = self.operand_stack.pop().strip().strip('"')
		required_skills = get_required_skills(job_url)

		for i in range(len(required_skills)):
			self.operand_stack.append(required_skills[i])
