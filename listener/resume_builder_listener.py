from gen.ResumeParser import ResumeParser
from gen.ResumeListener import ResumeListener


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
