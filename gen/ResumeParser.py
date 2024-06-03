# Generated from C:/Users/DarknesS/source/repos/dsl/grammar/Resume.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,32,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,30,0,9,1,0,0,0,2,13,1,
        0,0,0,4,25,1,0,0,0,6,29,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,
        0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,5,1,0,0,14,15,
        5,5,0,0,15,20,5,2,0,0,16,19,3,4,2,0,17,19,3,6,3,0,18,16,1,0,0,0,
        18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,23,1,
        0,0,0,22,20,1,0,0,0,23,24,5,3,0,0,24,3,1,0,0,0,25,26,5,5,0,0,26,
        27,5,4,0,0,27,28,5,6,0,0,28,5,1,0,0,0,29,30,5,6,0,0,30,7,1,0,0,0,
        3,11,18,20
    ]

class ResumeParser ( Parser ):

    grammarFileName = "Resume.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'section'", "'{'", "'}'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STRING", "WS" ]

    RULE_resume = 0
    RULE_section = 1
    RULE_entry = 2
    RULE_text = 3

    ruleNames =  [ "resume", "section", "entry", "text" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    STRING=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ResumeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.SectionContext)
            else:
                return self.getTypedRuleContext(ResumeParser.SectionContext,i)


        def getRuleIndex(self):
            return ResumeParser.RULE_resume

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResume" ):
                listener.enterResume(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResume" ):
                listener.exitResume(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResume" ):
                return visitor.visitResume(self)
            else:
                return visitor.visitChildren(self)




    def resume(self):

        localctx = ResumeParser.ResumeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_resume)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.section()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ResumeParser.ID, 0)

        def entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.EntryContext)
            else:
                return self.getTypedRuleContext(ResumeParser.EntryContext,i)


        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.TextContext)
            else:
                return self.getTypedRuleContext(ResumeParser.TextContext,i)


        def getRuleIndex(self):
            return ResumeParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = ResumeParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(ResumeParser.T__0)
            self.state = 14
            self.match(ResumeParser.ID)
            self.state = 15
            self.match(ResumeParser.T__1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 18
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 16
                    self.entry()
                    pass
                elif token in [6]:
                    self.state = 17
                    self.text()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self.match(ResumeParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ResumeParser.ID, 0)

        def STRING(self):
            return self.getToken(ResumeParser.STRING, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry" ):
                listener.enterEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry" ):
                listener.exitEntry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry" ):
                return visitor.visitEntry(self)
            else:
                return visitor.visitChildren(self)




    def entry(self):

        localctx = ResumeParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ResumeParser.ID)
            self.state = 26
            self.match(ResumeParser.T__3)
            self.state = 27
            self.match(ResumeParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ResumeParser.STRING, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = ResumeParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ResumeParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





