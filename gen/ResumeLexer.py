# Generated from C:/Users/DarknesS/source/repos/dsl/grammar/Resume.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,5,4,32,8,4,10,4,12,4,35,9,4,1,5,1,5,5,5,39,8,5,10,5,12,5,42,
        9,5,1,5,1,5,1,6,4,6,47,8,6,11,6,12,6,48,1,6,1,6,0,0,7,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,1,0,4,3,0,65,90,95,95,97,122,4,0,48,57,65,90,
        95,95,97,122,1,0,34,34,3,0,9,10,13,13,32,32,54,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,1,15,1,0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,29,1,0,
        0,0,11,36,1,0,0,0,13,46,1,0,0,0,15,16,5,115,0,0,16,17,5,101,0,0,
        17,18,5,99,0,0,18,19,5,116,0,0,19,20,5,105,0,0,20,21,5,111,0,0,21,
        22,5,110,0,0,22,2,1,0,0,0,23,24,5,123,0,0,24,4,1,0,0,0,25,26,5,125,
        0,0,26,6,1,0,0,0,27,28,5,58,0,0,28,8,1,0,0,0,29,33,7,0,0,0,30,32,
        7,1,0,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,
        34,10,1,0,0,0,35,33,1,0,0,0,36,40,5,34,0,0,37,39,8,2,0,0,38,37,1,
        0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,
        40,1,0,0,0,43,44,5,34,0,0,44,12,1,0,0,0,45,47,7,3,0,0,46,45,1,0,
        0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,
        6,6,0,0,51,14,1,0,0,0,4,0,33,40,48,1,6,0,0
    ]

class ResumeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    STRING = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'section'", "'{'", "'}'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ID", "STRING", "WS" ]

    grammarFileName = "Resume.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


