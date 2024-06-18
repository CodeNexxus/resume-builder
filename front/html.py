from antlr4 import *
from gen.ResumeLexer import ResumeLexer
from gen.ResumeParser import ResumeParser
from listener.ResumeBuilderListener import ResumeListener
from listener.ResumeCodeGenerator import ResumeDslCodeGenerator
from ast_code.post_order_ast_traverser import PostOrderASTTraverser
from ast_code.ast_to_networkx_graph import show_ast


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

    # listener = ResumeBuilderListener()
    walker = ParseTreeWalker()
    ast_builder_listener = ResumeListener(parser.ruleNames)
    walker.walk(t=tree, listener=ast_builder_listener)

    ast = ast_builder_listener.ast
    show_ast(ast.root)
    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
    traversal = post_order_ast_traverser.traverse_ast(ast.root)

    code_generator = ResumeDslCodeGenerator()
    generated_resume = code_generator.generate_code(traversal)

    # html = get_html(listener)
    return generated_resume
