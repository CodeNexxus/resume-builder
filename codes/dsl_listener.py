from default_codes.ast import AST
from default_codes.make_ast_subtree import make_ast_subtree
from gen.ExampleDSLListener import ExampleDSLListener


class CustomExampleDSLListener(ExampleDSLListener):
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

