from ast_code.ast import AST
from ast_code.make_ast_subtree import make_ast_subtree
from gen.ResumeListener import ResumeListener
from gen.ResumeParser import ResumeParser


class ResumeBuilderListener(ResumeListener):
    def __init__(self):
        self.sections = []
        self.current_section = {}

    def enterSection(self, ctx: ResumeParser.SectionContext):
        self.current_section = {'title': ctx.ID().getText(), 'entries': []}
        self.sections.append(self.current_section)

    def exitEntry(self, ctx: ResumeParser.EntryContext):
        self.current_section['entries'].append((ctx.ID().getText(), ctx.STRING().getText()))

    def exitText(self, ctx: ResumeParser.TextContext):
        self.current_section['entries'].append(('text', ctx.STRING().getText()))


class ResumeListener(ResumeListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['resume', 'personal_info', 'summary']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitResume(self, ctx):
        make_ast_subtree(self.ast, ctx, "resume", keep_node=True)

    def exitPersonal_info(self, ctx):
        make_ast_subtree(self.ast, ctx, "personal_info", keep_node=True)

    def exitSummary(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "summary", keep_node=True)