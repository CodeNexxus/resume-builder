from antlr4 import *
import argparse
from listener.ResumeBuilderListener import CustomResumeListener
from ast_code.ast_to_networkx_graph import show_ast
from gen.ResumeLexer import ResumeLexer
from gen.ResumeParser import ResumeParser
from ast_code.post_order_ast_traverser import PostOrderASTTraverser
from listener.ResumeCodeGenerator import ResumeDslCodeGenerator


def main(arguments):
    stream = FileStream(arguments.input, encoding='utf8')
    lexer = ResumeLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = ResumeParser(token_stream)
    parse_tree = parser.resume()
    ast_builder_listener = CustomResumeListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)
    ast = ast_builder_listener.ast
    show_ast(ast.root)
    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
    traversal = post_order_ast_traverser.traverse_ast(ast.root)
    code_generator = ResumeDslCodeGenerator()
    generated_code = code_generator.generate_code(traversal)

    generated_html = generated_code[0]
    generated_css = generated_code[1]

    with open(arguments.output, 'w') as output_file:
        output_file.write(generated_html)
    with open('styles.css', 'w') as output_file:
        output_file.write(generated_css)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default=r'input.rsm')
    argparser.add_argument('-o', '--output', help='Output path', default=r'resume.html')
    args = argparser.parse_args()
    main(args)
