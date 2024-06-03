# Generated from C:/Users/DarknesS/source/repos/dsl/grammar/Resume.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ResumeParser import ResumeParser
else:
    from ResumeParser import ResumeParser

# This class defines a complete generic visitor for a parse tree produced by ResumeParser.

class ResumeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ResumeParser#resume.
    def visitResume(self, ctx:ResumeParser.ResumeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#section.
    def visitSection(self, ctx:ResumeParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#entry.
    def visitEntry(self, ctx:ResumeParser.EntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#text.
    def visitText(self, ctx:ResumeParser.TextContext):
        return self.visitChildren(ctx)



del ResumeParser