# Generated from C:/Users/DarknesS/source/repos/dsl/grammar/Resume.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ResumeParser import ResumeParser
else:
    from ResumeParser import ResumeParser

# This class defines a complete listener for a parse tree produced by ResumeParser.
class ResumeListener(ParseTreeListener):

    # Enter a parse tree produced by ResumeParser#resume.
    def enterResume(self, ctx:ResumeParser.ResumeContext):
        pass

    # Exit a parse tree produced by ResumeParser#resume.
    def exitResume(self, ctx:ResumeParser.ResumeContext):
        pass


    # Enter a parse tree produced by ResumeParser#section.
    def enterSection(self, ctx:ResumeParser.SectionContext):
        pass

    # Exit a parse tree produced by ResumeParser#section.
    def exitSection(self, ctx:ResumeParser.SectionContext):
        pass


    # Enter a parse tree produced by ResumeParser#entry.
    def enterEntry(self, ctx:ResumeParser.EntryContext):
        pass

    # Exit a parse tree produced by ResumeParser#entry.
    def exitEntry(self, ctx:ResumeParser.EntryContext):
        pass


    # Enter a parse tree produced by ResumeParser#text.
    def enterText(self, ctx:ResumeParser.TextContext):
        pass

    # Exit a parse tree produced by ResumeParser#text.
    def exitText(self, ctx:ResumeParser.TextContext):
        pass



del ResumeParser