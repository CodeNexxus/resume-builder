from ast_code.ast import AST
from ast_code.make_ast_subtree import make_ast_subtree
from gen.ResumeListener import ResumeListener


class CustomResumeListener(ResumeListener):

    def __init__(self, rule_names):
        self.overridden_rules = ['resume', 'base_info', 'additional_info',
                                 'personal_info', 'name', 'surname',
                                 'job_title', 'phone', 'institution',
                                 'city', 'gmail', 'birth',
                                 'summary', 'socials', 'social',
                                 'hard_skills', 'soft_skills', 'soft_skill',
                                 'languages', 'language', 'certificates',
                                 'certificate', 'educations', 'link',
                                 'projects', 'project', 'project_title',
                                 'project_description', 'project_url', 'work_experience'
                                 'job', 'company', 'position',
                                 'start_date', 'end_date', 'responsibility_list',
                                 'responsibility', 'education', 'degree',
                                 'git_scraper', 'jobinja_scraper',
                                 'go_top', 'autocopy', 'job_title_effect',
                                 'interactive_skill_bars', 'collapsable_sections',
                                 'theme_switching', 'tooltip']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitResume(self, ctx):
        make_ast_subtree(self.ast, ctx, "resume", keep_node=True)

    def exitGit_scraper(self, ctx):
        make_ast_subtree(self.ast, ctx, "git_scraper", keep_node=True)

    def exitSocial(self, ctx):
        make_ast_subtree(self.ast, ctx, "social", keep_node=True)

    def exitSocials(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "socials", keep_node=True)


    def exitBase_info(self, ctx):
        make_ast_subtree(self.ast, ctx, "base_info", keep_node=True)

    def exitAdditional_info(self, ctx):
        make_ast_subtree(self.ast, ctx, "additional_info", keep_node=True)

    def exitPersonal_info(self, ctx):
        make_ast_subtree(self.ast, ctx, "personal_info", keep_node=True)

    def exitName(self, ctx):
        make_ast_subtree(self.ast, ctx, "name", keep_node=True)

    def exitSurname(self, ctx):
        make_ast_subtree(self.ast, ctx, "surname", keep_node=True)

    def exitJob_title(self, ctx):
        make_ast_subtree(self.ast, ctx, "job_title", keep_node=True)

    def exitBirth(self, ctx):
        make_ast_subtree(self.ast, ctx, "birth", keep_node=True)

    def exitPhone(self, ctx):
        make_ast_subtree(self.ast, ctx, "phone", keep_node=True)

    def exitCity(self, ctx):
        make_ast_subtree(self.ast, ctx, "city", keep_node=True)

    def exitGmail(self, ctx):
        make_ast_subtree(self.ast, ctx, "gmail", keep_node=True)

    def exitSummary(self, ctx):
        make_ast_subtree(self.ast, ctx, "summary", keep_node=True)

    def exitHard_skills(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "hard_skills", keep_node=True)

    def exitSoft_skills(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "soft_skills", keep_node=True)

    def exitSoft_skill(self, ctx):
        make_ast_subtree(self.ast, ctx, "soft_skill", keep_node=True)

    def exitLanguages(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "languages", keep_node=True)

    def exitEducations(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "educations", keep_node=True)


    def exitLanguage(self, ctx):
        make_ast_subtree(self.ast, ctx, "language", keep_node=True)

    def exitCertificates(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "certificates", keep_node=True)

    def exitCertificate(self, ctx):
        make_ast_subtree(self.ast, ctx, "certificate", keep_node=True)

    def exitInstitution(self, ctx):
        make_ast_subtree(self.ast, ctx, "institution", keep_node=True)

    def exitLink(self, ctx):
        make_ast_subtree(self.ast, ctx, "link", keep_node=True)

    def exitProjects(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "projects", keep_node=True)

    def exitProject(self, ctx):
        make_ast_subtree(self.ast, ctx, "project", keep_node=True)

    def exitProject_title(self, ctx):
        make_ast_subtree(self.ast, ctx, "title", keep_node=True)

    def exitProject_description(self, ctx):
        make_ast_subtree(self.ast, ctx, "description", keep_node=True)

    def exitProject_url(self, ctx):
        make_ast_subtree(self.ast, ctx, "url", keep_node=True)

    def exitWork_experience(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "work_experience", keep_node=True)

    def exitJob(self, ctx):
        make_ast_subtree(self.ast, ctx, "job", keep_node=True)

    def exitCompany(self, ctx):
        make_ast_subtree(self.ast, ctx, "company", keep_node=True)

    def exitPosition(self, ctx):
        make_ast_subtree(self.ast, ctx, "position", keep_node=True)

    def exitStart_date(self, ctx):
        make_ast_subtree(self.ast, ctx, "start_date", keep_node=True)

    def exitEnd_date(self, ctx):
        make_ast_subtree(self.ast, ctx, "end_date", keep_node=True)

    def exitResponsibility_list(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "responsibilities", keep_node=True)

    def exitResponsibility(self, ctx):
        make_ast_subtree(self.ast, ctx, "responsibility", keep_node=True)

    def exitEducation(self, ctx):
        make_ast_subtree(self.ast, ctx, "education", keep_node=True)

    def exitDegree(self, ctx):
        make_ast_subtree(self.ast, ctx, "degree", keep_node=True)

    def exitJobinja_scraper(self, ctx):
        make_ast_subtree(self.ast, ctx, "jobinja_scraper", keep_node=True)

    def exitGo_top(self, ctx):
        make_ast_subtree(self.ast, ctx, "go_top", keep_node=True)

    def exitAutocopy(self, ctx):
        make_ast_subtree(self.ast, ctx, "autocopy", keep_node=True)

    def exitJob_title_effect(self, ctx):
        make_ast_subtree(self.ast, ctx, "job_title_effect", keep_node=True)

    def exitInteractive_skill_bars(self, ctx):
        make_ast_subtree(self.ast, ctx, "interactive_skill_bars", keep_node=True)

    def exitCollapsable_sections(self, ctx):
        make_ast_subtree(self.ast, ctx, "collapsable_sections", keep_node=True)

    def exitTheme_switching(self, ctx):
        make_ast_subtree(self.ast, ctx, "theme_switching", keep_node=True)

    def exitSwitching(self, ctx):
        make_ast_subtree(self.ast, ctx, "switching", keep_node=True)

    def exitTooltip(self, ctx):
        make_ast_subtree(self.ast, ctx, "tooltip", keep_node=True)
