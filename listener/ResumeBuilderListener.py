from ast_code.ast import AST
from ast_code.make_ast_subtree import make_ast_subtree
from gen.ResumeListener import ResumeListener


class CustomResumeListener(ResumeListener):

    def __init__(self, rule_names):
        self.overridden_rules = ['resume', 'base_info', 'additional_info',
                                 'personal_info', 'name',
                                 'surname', 'job_title', 'birth',
                                 'phone', 'city', 'gmail', 'summary',
                                 'socials', 'social_list',
                                 'hard_skills', 'soft_skills', 'soft_skill',
                                 'languages', 'language', 'certificate',
                                 'educations',
                                 ]
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitResume(self, ctx):
        make_ast_subtree(self.ast, ctx, "resume", keep_node=True)

    def exitSocial_list(self, ctx):
        make_ast_subtree(self.ast, ctx, "social_list", keep_node=True)

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
        make_ast_subtree(self.ast, ctx, "certificates", keep_node=True)

    def exitCertificate(self, ctx):
        make_ast_subtree(self.ast, ctx, "certificate", keep_node=True)