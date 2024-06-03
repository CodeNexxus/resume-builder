from antlr4 import *
from gen.ResumeLexer import ResumeLexer
from gen.ResumeParser import ResumeParser
from listener.resume_builder_listener import ResumeBuilderListener


def get_html(self):
    html = '''
    <html>
    <head>
        <title>Resume</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
    '''
    for section in self.sections:
        html += f'<h2>{section["title"]}</h2><ul>'
        for entry in section['entries']:
            if entry[0] == 'text':
                html += f'<li>{entry[1]}</li>'
            else:
                html += f'<li><strong>{entry[0]}:</strong> {entry[1]}</li>'
        html += '</ul>'
    html += '</body></html>'
    return html


def generate_html_from_resume_file(file_path):
    with open(file_path, 'r') as file:
        resume_dsl = file.read()

    input_stream = InputStream(resume_dsl)
    lexer = ResumeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ResumeParser(stream)
    tree = parser.resume()

    listener = ResumeBuilderListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    html = get_html(listener)
    return html
