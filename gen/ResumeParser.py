# Generated from D:/Uni/semester_6/Compiler/project/resume-builder/grammar/Resume.g4 by ANTLR 4.13.1
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
        4,1,35,297,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,1,1,1,3,1,74,8,1,1,1,3,1,77,8,1,1,1,3,1,80,8,
        1,1,1,3,1,83,8,1,1,1,3,1,86,8,1,1,1,3,1,89,8,1,1,1,3,1,92,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,
        1,11,1,11,3,11,128,8,11,1,11,3,11,131,8,11,1,12,1,12,1,12,1,13,1,
        13,1,13,5,13,139,8,13,10,13,12,13,142,9,13,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,155,8,16,10,16,12,16,158,9,
        16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,171,
        8,19,10,19,12,19,174,9,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        5,21,184,8,21,10,21,12,21,187,9,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,5,24,206,
        8,24,10,24,12,24,209,9,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        1,26,1,26,5,26,221,8,26,10,26,12,26,224,9,26,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,5,28,
        242,8,28,10,28,12,28,245,9,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,5,30,
        266,8,30,10,30,12,30,269,9,30,1,31,1,31,1,32,1,32,1,32,1,32,1,32,
        1,32,5,32,279,8,32,10,32,12,32,282,9,32,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,0,0,34,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,0,0,280,0,68,1,0,0,0,2,71,1,0,0,0,4,93,1,0,0,0,
        6,108,1,0,0,0,8,110,1,0,0,0,10,112,1,0,0,0,12,114,1,0,0,0,14,116,
        1,0,0,0,16,118,1,0,0,0,18,120,1,0,0,0,20,122,1,0,0,0,22,125,1,0,
        0,0,24,132,1,0,0,0,26,135,1,0,0,0,28,143,1,0,0,0,30,147,1,0,0,0,
        32,151,1,0,0,0,34,159,1,0,0,0,36,163,1,0,0,0,38,167,1,0,0,0,40,175,
        1,0,0,0,42,177,1,0,0,0,44,188,1,0,0,0,46,198,1,0,0,0,48,202,1,0,
        0,0,50,210,1,0,0,0,52,214,1,0,0,0,54,225,1,0,0,0,56,235,1,0,0,0,
        58,246,1,0,0,0,60,262,1,0,0,0,62,270,1,0,0,0,64,272,1,0,0,0,66,283,
        1,0,0,0,68,69,3,2,1,0,69,70,5,0,0,1,70,1,1,0,0,0,71,73,3,4,2,0,72,
        74,3,20,10,0,73,72,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,77,3,22,
        11,0,76,75,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,80,3,42,21,0,79,
        78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,83,3,46,23,0,82,81,1,0,
        0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,86,3,52,26,0,85,84,1,0,0,0,85,
        86,1,0,0,0,86,88,1,0,0,0,87,89,3,56,28,0,88,87,1,0,0,0,88,89,1,0,
        0,0,89,91,1,0,0,0,90,92,3,64,32,0,91,90,1,0,0,0,91,92,1,0,0,0,92,
        3,1,0,0,0,93,94,5,1,0,0,94,95,3,6,3,0,95,96,5,2,0,0,96,97,3,8,4,
        0,97,98,5,3,0,0,98,99,3,10,5,0,99,100,5,4,0,0,100,101,3,14,7,0,101,
        102,5,5,0,0,102,103,3,16,8,0,103,104,5,6,0,0,104,105,3,18,9,0,105,
        106,5,7,0,0,106,107,3,12,6,0,107,5,1,0,0,0,108,109,5,29,0,0,109,
        7,1,0,0,0,110,111,5,29,0,0,111,9,1,0,0,0,112,113,5,29,0,0,113,11,
        1,0,0,0,114,115,5,29,0,0,115,13,1,0,0,0,116,117,5,30,0,0,117,15,
        1,0,0,0,118,119,5,29,0,0,119,17,1,0,0,0,120,121,5,31,0,0,121,19,
        1,0,0,0,122,123,5,8,0,0,123,124,5,29,0,0,124,21,1,0,0,0,125,127,
        3,24,12,0,126,128,3,30,15,0,127,126,1,0,0,0,127,128,1,0,0,0,128,
        130,1,0,0,0,129,131,3,36,18,0,130,129,1,0,0,0,130,131,1,0,0,0,131,
        23,1,0,0,0,132,133,5,9,0,0,133,134,3,26,13,0,134,25,1,0,0,0,135,
        140,3,28,14,0,136,137,5,35,0,0,137,139,3,28,14,0,138,136,1,0,0,0,
        139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,27,1,0,0,0,142,
        140,1,0,0,0,143,144,5,29,0,0,144,145,5,10,0,0,145,146,5,29,0,0,146,
        29,1,0,0,0,147,148,5,11,0,0,148,149,5,35,0,0,149,150,3,32,16,0,150,
        31,1,0,0,0,151,156,3,34,17,0,152,153,5,35,0,0,153,155,3,34,17,0,
        154,152,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,
        157,33,1,0,0,0,158,156,1,0,0,0,159,160,5,29,0,0,160,161,5,10,0,0,
        161,162,5,33,0,0,162,35,1,0,0,0,163,164,5,12,0,0,164,165,5,35,0,
        0,165,166,3,38,19,0,166,37,1,0,0,0,167,172,3,40,20,0,168,169,5,35,
        0,0,169,171,3,40,20,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,1,
        0,0,0,172,173,1,0,0,0,173,39,1,0,0,0,174,172,1,0,0,0,175,176,5,29,
        0,0,176,41,1,0,0,0,177,178,5,13,0,0,178,179,5,35,0,0,179,185,3,44,
        22,0,180,181,5,35,0,0,181,182,5,35,0,0,182,184,3,44,22,0,183,180,
        1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,43,1,
        0,0,0,187,185,1,0,0,0,188,189,5,1,0,0,189,190,5,29,0,0,190,191,5,
        35,0,0,191,192,5,14,0,0,192,193,5,29,0,0,193,194,5,35,0,0,194,195,
        5,15,0,0,195,196,5,32,0,0,196,197,5,35,0,0,197,45,1,0,0,0,198,199,
        5,16,0,0,199,200,5,35,0,0,200,201,3,48,24,0,201,47,1,0,0,0,202,207,
        3,50,25,0,203,204,5,35,0,0,204,206,3,50,25,0,205,203,1,0,0,0,206,
        209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,49,1,0,0,0,209,207,
        1,0,0,0,210,211,5,29,0,0,211,212,5,17,0,0,212,213,5,32,0,0,213,51,
        1,0,0,0,214,215,5,18,0,0,215,216,5,35,0,0,216,222,3,54,27,0,217,
        218,5,35,0,0,218,219,5,35,0,0,219,221,3,54,27,0,220,217,1,0,0,0,
        221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,53,1,0,0,0,224,
        222,1,0,0,0,225,226,5,19,0,0,226,227,5,29,0,0,227,228,5,35,0,0,228,
        229,5,20,0,0,229,230,5,29,0,0,230,231,5,35,0,0,231,232,5,15,0,0,
        232,233,5,32,0,0,233,234,5,35,0,0,234,55,1,0,0,0,235,236,5,21,0,
        0,236,237,5,35,0,0,237,243,3,58,29,0,238,239,5,35,0,0,239,240,5,
        35,0,0,240,242,3,58,29,0,241,238,1,0,0,0,242,245,1,0,0,0,243,241,
        1,0,0,0,243,244,1,0,0,0,244,57,1,0,0,0,245,243,1,0,0,0,246,247,5,
        22,0,0,247,248,5,29,0,0,248,249,5,35,0,0,249,250,5,23,0,0,250,251,
        5,29,0,0,251,252,5,35,0,0,252,253,5,24,0,0,253,254,5,29,0,0,254,
        255,5,35,0,0,255,256,5,25,0,0,256,257,5,29,0,0,257,258,5,35,0,0,
        258,259,5,26,0,0,259,260,5,35,0,0,260,261,3,60,30,0,261,59,1,0,0,
        0,262,267,3,62,31,0,263,264,5,35,0,0,264,266,3,62,31,0,265,263,1,
        0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,61,1,0,
        0,0,269,267,1,0,0,0,270,271,5,29,0,0,271,63,1,0,0,0,272,273,5,27,
        0,0,273,274,5,35,0,0,274,280,3,66,33,0,275,276,5,35,0,0,276,277,
        5,35,0,0,277,279,3,66,33,0,278,275,1,0,0,0,279,282,1,0,0,0,280,278,
        1,0,0,0,280,281,1,0,0,0,281,65,1,0,0,0,282,280,1,0,0,0,283,284,5,
        14,0,0,284,285,5,29,0,0,285,286,5,35,0,0,286,287,5,28,0,0,287,288,
        5,29,0,0,288,289,5,35,0,0,289,290,5,24,0,0,290,291,5,29,0,0,291,
        292,5,35,0,0,292,293,5,25,0,0,293,294,5,29,0,0,294,295,5,35,0,0,
        295,67,1,0,0,0,18,73,76,79,82,85,88,91,127,130,140,156,172,185,207,
        222,243,267,280
    ]

class ResumeParser ( Parser ):

    grammarFileName = "Resume.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'name:'", "'surname:'", "'job_title:'", 
                     "'phone: '", "'city:'", "'gmail:'", "'birth:'", "'summary:'", 
                     "'hard_skills:'", "','", "'soft_skills:'", "'languages:'", 
                     "'certificates:'", "'institution:'", "'link:'", "'socials:'", 
                     "':'", "'projects:'", "'title:'", "'description:'", 
                     "'work_experience:'", "'company:'", "'position:'", 
                     "'start_date:'", "'end_date:'", "'responsibilities:'", 
                     "'educations:'", "'degree:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TEXT", "PHONE", "EMAIL", "URL", "RATING", 
                      "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_resume = 1
    RULE_personal_info = 2
    RULE_name = 3
    RULE_surname = 4
    RULE_job_title = 5
    RULE_birth = 6
    RULE_phone = 7
    RULE_city = 8
    RULE_gmail = 9
    RULE_summary = 10
    RULE_skills = 11
    RULE_hard_skills = 12
    RULE_hard_skill_list = 13
    RULE_hard_skill = 14
    RULE_soft_skills = 15
    RULE_soft_skill_list = 16
    RULE_soft_skill = 17
    RULE_languages = 18
    RULE_language_list = 19
    RULE_language = 20
    RULE_certificates = 21
    RULE_certificate = 22
    RULE_socials = 23
    RULE_social_list = 24
    RULE_social = 25
    RULE_projects = 26
    RULE_project = 27
    RULE_work_experience = 28
    RULE_job = 29
    RULE_responsibility_list = 30
    RULE_responsibility = 31
    RULE_educations = 32
    RULE_education = 33

    ruleNames =  [ "start", "resume", "personal_info", "name", "surname", 
                   "job_title", "birth", "phone", "city", "gmail", "summary", 
                   "skills", "hard_skills", "hard_skill_list", "hard_skill", 
                   "soft_skills", "soft_skill_list", "soft_skill", "languages", 
                   "language_list", "language", "certificates", "certificate", 
                   "socials", "social_list", "social", "projects", "project", 
                   "work_experience", "job", "responsibility_list", "responsibility", 
                   "educations", "education" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    TEXT=29
    PHONE=30
    EMAIL=31
    URL=32
    RATING=33
    WS=34
    NEWLINE=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def resume(self):
            return self.getTypedRuleContext(ResumeParser.ResumeContext,0)


        def EOF(self):
            return self.getToken(ResumeParser.EOF, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ResumeParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.resume()
            self.state = 69
            self.match(ResumeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResumeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def personal_info(self):
            return self.getTypedRuleContext(ResumeParser.Personal_infoContext,0)


        def summary(self):
            return self.getTypedRuleContext(ResumeParser.SummaryContext,0)


        def skills(self):
            return self.getTypedRuleContext(ResumeParser.SkillsContext,0)


        def certificates(self):
            return self.getTypedRuleContext(ResumeParser.CertificatesContext,0)


        def socials(self):
            return self.getTypedRuleContext(ResumeParser.SocialsContext,0)


        def projects(self):
            return self.getTypedRuleContext(ResumeParser.ProjectsContext,0)


        def work_experience(self):
            return self.getTypedRuleContext(ResumeParser.Work_experienceContext,0)


        def educations(self):
            return self.getTypedRuleContext(ResumeParser.EducationsContext,0)


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
        self.enterRule(localctx, 2, self.RULE_resume)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.personal_info()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 72
                self.summary()


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 75
                self.skills()


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 78
                self.certificates()


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 81
                self.socials()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 84
                self.projects()


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 87
                self.work_experience()


            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 90
                self.educations()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Personal_infoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ResumeParser.NameContext,0)


        def surname(self):
            return self.getTypedRuleContext(ResumeParser.SurnameContext,0)


        def job_title(self):
            return self.getTypedRuleContext(ResumeParser.Job_titleContext,0)


        def phone(self):
            return self.getTypedRuleContext(ResumeParser.PhoneContext,0)


        def city(self):
            return self.getTypedRuleContext(ResumeParser.CityContext,0)


        def gmail(self):
            return self.getTypedRuleContext(ResumeParser.GmailContext,0)


        def birth(self):
            return self.getTypedRuleContext(ResumeParser.BirthContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_personal_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPersonal_info" ):
                listener.enterPersonal_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPersonal_info" ):
                listener.exitPersonal_info(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPersonal_info" ):
                return visitor.visitPersonal_info(self)
            else:
                return visitor.visitChildren(self)




    def personal_info(self):

        localctx = ResumeParser.Personal_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_personal_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ResumeParser.T__0)
            self.state = 94
            self.name()
            self.state = 95
            self.match(ResumeParser.T__1)
            self.state = 96
            self.surname()
            self.state = 97
            self.match(ResumeParser.T__2)
            self.state = 98
            self.job_title()
            self.state = 99
            self.match(ResumeParser.T__3)
            self.state = 100
            self.phone()
            self.state = 101
            self.match(ResumeParser.T__4)
            self.state = 102
            self.city()
            self.state = 103
            self.match(ResumeParser.T__5)
            self.state = 104
            self.gmail()
            self.state = 105
            self.match(ResumeParser.T__6)
            self.state = 106
            self.birth()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = ResumeParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SurnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_surname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSurname" ):
                listener.enterSurname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSurname" ):
                listener.exitSurname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSurname" ):
                return visitor.visitSurname(self)
            else:
                return visitor.visitChildren(self)




    def surname(self):

        localctx = ResumeParser.SurnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_surname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Job_titleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_job_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJob_title" ):
                listener.enterJob_title(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJob_title" ):
                listener.exitJob_title(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJob_title" ):
                return visitor.visitJob_title(self)
            else:
                return visitor.visitChildren(self)




    def job_title(self):

        localctx = ResumeParser.Job_titleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_job_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BirthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_birth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBirth" ):
                listener.enterBirth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBirth" ):
                listener.exitBirth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBirth" ):
                return visitor.visitBirth(self)
            else:
                return visitor.visitChildren(self)




    def birth(self):

        localctx = ResumeParser.BirthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_birth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhoneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PHONE(self):
            return self.getToken(ResumeParser.PHONE, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_phone

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhone" ):
                listener.enterPhone(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhone" ):
                listener.exitPhone(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhone" ):
                return visitor.visitPhone(self)
            else:
                return visitor.visitChildren(self)




    def phone(self):

        localctx = ResumeParser.PhoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_phone)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ResumeParser.PHONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_city

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCity" ):
                listener.enterCity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCity" ):
                listener.exitCity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCity" ):
                return visitor.visitCity(self)
            else:
                return visitor.visitChildren(self)




    def city(self):

        localctx = ResumeParser.CityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_city)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GmailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMAIL(self):
            return self.getToken(ResumeParser.EMAIL, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_gmail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGmail" ):
                listener.enterGmail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGmail" ):
                listener.exitGmail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGmail" ):
                return visitor.visitGmail(self)
            else:
                return visitor.visitChildren(self)




    def gmail(self):

        localctx = ResumeParser.GmailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_gmail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ResumeParser.EMAIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_summary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummary" ):
                listener.enterSummary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummary" ):
                listener.exitSummary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummary" ):
                return visitor.visitSummary(self)
            else:
                return visitor.visitChildren(self)




    def summary(self):

        localctx = ResumeParser.SummaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ResumeParser.T__7)
            self.state = 123
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkillsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hard_skills(self):
            return self.getTypedRuleContext(ResumeParser.Hard_skillsContext,0)


        def soft_skills(self):
            return self.getTypedRuleContext(ResumeParser.Soft_skillsContext,0)


        def languages(self):
            return self.getTypedRuleContext(ResumeParser.LanguagesContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_skills

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkills" ):
                listener.enterSkills(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkills" ):
                listener.exitSkills(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkills" ):
                return visitor.visitSkills(self)
            else:
                return visitor.visitChildren(self)




    def skills(self):

        localctx = ResumeParser.SkillsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.hard_skills()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 126
                self.soft_skills()


            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 129
                self.languages()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hard_skillsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hard_skill_list(self):
            return self.getTypedRuleContext(ResumeParser.Hard_skill_listContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_hard_skills

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHard_skills" ):
                listener.enterHard_skills(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHard_skills" ):
                listener.exitHard_skills(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHard_skills" ):
                return visitor.visitHard_skills(self)
            else:
                return visitor.visitChildren(self)




    def hard_skills(self):

        localctx = ResumeParser.Hard_skillsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_hard_skills)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ResumeParser.T__8)
            self.state = 133
            self.hard_skill_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hard_skill_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hard_skill(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.Hard_skillContext)
            else:
                return self.getTypedRuleContext(ResumeParser.Hard_skillContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ResumeParser.RULE_hard_skill_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHard_skill_list" ):
                listener.enterHard_skill_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHard_skill_list" ):
                listener.exitHard_skill_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHard_skill_list" ):
                return visitor.visitHard_skill_list(self)
            else:
                return visitor.visitChildren(self)




    def hard_skill_list(self):

        localctx = ResumeParser.Hard_skill_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_hard_skill_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.hard_skill()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 136
                self.match(ResumeParser.NEWLINE)
                self.state = 137
                self.hard_skill()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hard_skillContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.TEXT)
            else:
                return self.getToken(ResumeParser.TEXT, i)

        def getRuleIndex(self):
            return ResumeParser.RULE_hard_skill

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHard_skill" ):
                listener.enterHard_skill(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHard_skill" ):
                listener.exitHard_skill(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHard_skill" ):
                return visitor.visitHard_skill(self)
            else:
                return visitor.visitChildren(self)




    def hard_skill(self):

        localctx = ResumeParser.Hard_skillContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_hard_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ResumeParser.TEXT)
            self.state = 144
            self.match(ResumeParser.T__9)
            self.state = 145
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Soft_skillsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

        def soft_skill_list(self):
            return self.getTypedRuleContext(ResumeParser.Soft_skill_listContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_soft_skills

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoft_skills" ):
                listener.enterSoft_skills(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoft_skills" ):
                listener.exitSoft_skills(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoft_skills" ):
                return visitor.visitSoft_skills(self)
            else:
                return visitor.visitChildren(self)




    def soft_skills(self):

        localctx = ResumeParser.Soft_skillsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_soft_skills)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ResumeParser.T__10)
            self.state = 148
            self.match(ResumeParser.NEWLINE)
            self.state = 149
            self.soft_skill_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Soft_skill_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def soft_skill(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.Soft_skillContext)
            else:
                return self.getTypedRuleContext(ResumeParser.Soft_skillContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ResumeParser.RULE_soft_skill_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoft_skill_list" ):
                listener.enterSoft_skill_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoft_skill_list" ):
                listener.exitSoft_skill_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoft_skill_list" ):
                return visitor.visitSoft_skill_list(self)
            else:
                return visitor.visitChildren(self)




    def soft_skill_list(self):

        localctx = ResumeParser.Soft_skill_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_soft_skill_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.soft_skill()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 152
                self.match(ResumeParser.NEWLINE)
                self.state = 153
                self.soft_skill()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Soft_skillContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def RATING(self):
            return self.getToken(ResumeParser.RATING, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_soft_skill

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoft_skill" ):
                listener.enterSoft_skill(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoft_skill" ):
                listener.exitSoft_skill(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoft_skill" ):
                return visitor.visitSoft_skill(self)
            else:
                return visitor.visitChildren(self)




    def soft_skill(self):

        localctx = ResumeParser.Soft_skillContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_soft_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ResumeParser.TEXT)
            self.state = 160
            self.match(ResumeParser.T__9)
            self.state = 161
            self.match(ResumeParser.RATING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LanguagesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

        def language_list(self):
            return self.getTypedRuleContext(ResumeParser.Language_listContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_languages

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguages" ):
                listener.enterLanguages(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguages" ):
                listener.exitLanguages(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguages" ):
                return visitor.visitLanguages(self)
            else:
                return visitor.visitChildren(self)




    def languages(self):

        localctx = ResumeParser.LanguagesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_languages)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ResumeParser.T__11)
            self.state = 164
            self.match(ResumeParser.NEWLINE)
            self.state = 165
            self.language_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Language_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def language(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.LanguageContext)
            else:
                return self.getTypedRuleContext(ResumeParser.LanguageContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ResumeParser.RULE_language_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguage_list" ):
                listener.enterLanguage_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguage_list" ):
                listener.exitLanguage_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguage_list" ):
                return visitor.visitLanguage_list(self)
            else:
                return visitor.visitChildren(self)




    def language_list(self):

        localctx = ResumeParser.Language_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_language_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.language()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 168
                self.match(ResumeParser.NEWLINE)
                self.state = 169
                self.language()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LanguageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_language

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguage" ):
                listener.enterLanguage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguage" ):
                listener.exitLanguage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguage" ):
                return visitor.visitLanguage(self)
            else:
                return visitor.visitChildren(self)




    def language(self):

        localctx = ResumeParser.LanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_language)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CertificatesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def certificate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.CertificateContext)
            else:
                return self.getTypedRuleContext(ResumeParser.CertificateContext,i)


        def getRuleIndex(self):
            return ResumeParser.RULE_certificates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCertificates" ):
                listener.enterCertificates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCertificates" ):
                listener.exitCertificates(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCertificates" ):
                return visitor.visitCertificates(self)
            else:
                return visitor.visitChildren(self)




    def certificates(self):

        localctx = ResumeParser.CertificatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_certificates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ResumeParser.T__12)
            self.state = 178
            self.match(ResumeParser.NEWLINE)
            self.state = 179
            self.certificate()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 180
                self.match(ResumeParser.NEWLINE)
                self.state = 181
                self.match(ResumeParser.NEWLINE)
                self.state = 182
                self.certificate()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CertificateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.TEXT)
            else:
                return self.getToken(ResumeParser.TEXT, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_certificate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCertificate" ):
                listener.enterCertificate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCertificate" ):
                listener.exitCertificate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCertificate" ):
                return visitor.visitCertificate(self)
            else:
                return visitor.visitChildren(self)




    def certificate(self):

        localctx = ResumeParser.CertificateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_certificate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ResumeParser.T__0)
            self.state = 189
            self.match(ResumeParser.TEXT)
            self.state = 190
            self.match(ResumeParser.NEWLINE)
            self.state = 191
            self.match(ResumeParser.T__13)
            self.state = 192
            self.match(ResumeParser.TEXT)
            self.state = 193
            self.match(ResumeParser.NEWLINE)
            self.state = 194
            self.match(ResumeParser.T__14)
            self.state = 195
            self.match(ResumeParser.URL)
            self.state = 196
            self.match(ResumeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SocialsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

        def social_list(self):
            return self.getTypedRuleContext(ResumeParser.Social_listContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_socials

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSocials" ):
                listener.enterSocials(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSocials" ):
                listener.exitSocials(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSocials" ):
                return visitor.visitSocials(self)
            else:
                return visitor.visitChildren(self)




    def socials(self):

        localctx = ResumeParser.SocialsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_socials)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(ResumeParser.T__15)
            self.state = 199
            self.match(ResumeParser.NEWLINE)
            self.state = 200
            self.social_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Social_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def social(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.SocialContext)
            else:
                return self.getTypedRuleContext(ResumeParser.SocialContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ResumeParser.RULE_social_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSocial_list" ):
                listener.enterSocial_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSocial_list" ):
                listener.exitSocial_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSocial_list" ):
                return visitor.visitSocial_list(self)
            else:
                return visitor.visitChildren(self)




    def social_list(self):

        localctx = ResumeParser.Social_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_social_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.social()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 203
                self.match(ResumeParser.NEWLINE)
                self.state = 204
                self.social()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SocialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_social

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSocial" ):
                listener.enterSocial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSocial" ):
                listener.exitSocial(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSocial" ):
                return visitor.visitSocial(self)
            else:
                return visitor.visitChildren(self)




    def social(self):

        localctx = ResumeParser.SocialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_social)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ResumeParser.TEXT)
            self.state = 211
            self.match(ResumeParser.T__16)
            self.state = 212
            self.match(ResumeParser.URL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProjectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def project(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.ProjectContext)
            else:
                return self.getTypedRuleContext(ResumeParser.ProjectContext,i)


        def getRuleIndex(self):
            return ResumeParser.RULE_projects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProjects" ):
                listener.enterProjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProjects" ):
                listener.exitProjects(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProjects" ):
                return visitor.visitProjects(self)
            else:
                return visitor.visitChildren(self)




    def projects(self):

        localctx = ResumeParser.ProjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_projects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ResumeParser.T__17)
            self.state = 215
            self.match(ResumeParser.NEWLINE)
            self.state = 216
            self.project()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 217
                self.match(ResumeParser.NEWLINE)
                self.state = 218
                self.match(ResumeParser.NEWLINE)
                self.state = 219
                self.project()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.TEXT)
            else:
                return self.getToken(ResumeParser.TEXT, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_project

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject" ):
                listener.enterProject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject" ):
                listener.exitProject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProject" ):
                return visitor.visitProject(self)
            else:
                return visitor.visitChildren(self)




    def project(self):

        localctx = ResumeParser.ProjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_project)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(ResumeParser.T__18)
            self.state = 226
            self.match(ResumeParser.TEXT)
            self.state = 227
            self.match(ResumeParser.NEWLINE)
            self.state = 228
            self.match(ResumeParser.T__19)
            self.state = 229
            self.match(ResumeParser.TEXT)
            self.state = 230
            self.match(ResumeParser.NEWLINE)
            self.state = 231
            self.match(ResumeParser.T__14)
            self.state = 232
            self.match(ResumeParser.URL)
            self.state = 233
            self.match(ResumeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Work_experienceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def job(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.JobContext)
            else:
                return self.getTypedRuleContext(ResumeParser.JobContext,i)


        def getRuleIndex(self):
            return ResumeParser.RULE_work_experience

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWork_experience" ):
                listener.enterWork_experience(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWork_experience" ):
                listener.exitWork_experience(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWork_experience" ):
                return visitor.visitWork_experience(self)
            else:
                return visitor.visitChildren(self)




    def work_experience(self):

        localctx = ResumeParser.Work_experienceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_work_experience)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(ResumeParser.T__20)
            self.state = 236
            self.match(ResumeParser.NEWLINE)
            self.state = 237
            self.job()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 238
                self.match(ResumeParser.NEWLINE)
                self.state = 239
                self.match(ResumeParser.NEWLINE)
                self.state = 240
                self.job()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JobContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.TEXT)
            else:
                return self.getToken(ResumeParser.TEXT, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def responsibility_list(self):
            return self.getTypedRuleContext(ResumeParser.Responsibility_listContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_job

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJob" ):
                listener.enterJob(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJob" ):
                listener.exitJob(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJob" ):
                return visitor.visitJob(self)
            else:
                return visitor.visitChildren(self)




    def job(self):

        localctx = ResumeParser.JobContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_job)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ResumeParser.T__21)
            self.state = 247
            self.match(ResumeParser.TEXT)
            self.state = 248
            self.match(ResumeParser.NEWLINE)
            self.state = 249
            self.match(ResumeParser.T__22)
            self.state = 250
            self.match(ResumeParser.TEXT)
            self.state = 251
            self.match(ResumeParser.NEWLINE)
            self.state = 252
            self.match(ResumeParser.T__23)
            self.state = 253
            self.match(ResumeParser.TEXT)
            self.state = 254
            self.match(ResumeParser.NEWLINE)
            self.state = 255
            self.match(ResumeParser.T__24)
            self.state = 256
            self.match(ResumeParser.TEXT)
            self.state = 257
            self.match(ResumeParser.NEWLINE)
            self.state = 258
            self.match(ResumeParser.T__25)
            self.state = 259
            self.match(ResumeParser.NEWLINE)
            self.state = 260
            self.responsibility_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Responsibility_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def responsibility(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.ResponsibilityContext)
            else:
                return self.getTypedRuleContext(ResumeParser.ResponsibilityContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ResumeParser.RULE_responsibility_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResponsibility_list" ):
                listener.enterResponsibility_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResponsibility_list" ):
                listener.exitResponsibility_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResponsibility_list" ):
                return visitor.visitResponsibility_list(self)
            else:
                return visitor.visitChildren(self)




    def responsibility_list(self):

        localctx = ResumeParser.Responsibility_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_responsibility_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.responsibility()
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263
                    self.match(ResumeParser.NEWLINE)
                    self.state = 264
                    self.responsibility() 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResponsibilityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_responsibility

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResponsibility" ):
                listener.enterResponsibility(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResponsibility" ):
                listener.exitResponsibility(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResponsibility" ):
                return visitor.visitResponsibility(self)
            else:
                return visitor.visitChildren(self)




    def responsibility(self):

        localctx = ResumeParser.ResponsibilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_responsibility)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EducationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def education(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.EducationContext)
            else:
                return self.getTypedRuleContext(ResumeParser.EducationContext,i)


        def getRuleIndex(self):
            return ResumeParser.RULE_educations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEducations" ):
                listener.enterEducations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEducations" ):
                listener.exitEducations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEducations" ):
                return visitor.visitEducations(self)
            else:
                return visitor.visitChildren(self)




    def educations(self):

        localctx = ResumeParser.EducationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_educations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ResumeParser.T__26)
            self.state = 273
            self.match(ResumeParser.NEWLINE)
            self.state = 274
            self.education()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 275
                self.match(ResumeParser.NEWLINE)
                self.state = 276
                self.match(ResumeParser.NEWLINE)
                self.state = 277
                self.education()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EducationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.TEXT)
            else:
                return self.getToken(ResumeParser.TEXT, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ResumeParser.RULE_education

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEducation" ):
                listener.enterEducation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEducation" ):
                listener.exitEducation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEducation" ):
                return visitor.visitEducation(self)
            else:
                return visitor.visitChildren(self)




    def education(self):

        localctx = ResumeParser.EducationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_education)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ResumeParser.T__13)
            self.state = 284
            self.match(ResumeParser.TEXT)
            self.state = 285
            self.match(ResumeParser.NEWLINE)
            self.state = 286
            self.match(ResumeParser.T__27)
            self.state = 287
            self.match(ResumeParser.TEXT)
            self.state = 288
            self.match(ResumeParser.NEWLINE)
            self.state = 289
            self.match(ResumeParser.T__23)
            self.state = 290
            self.match(ResumeParser.TEXT)
            self.state = 291
            self.match(ResumeParser.NEWLINE)
            self.state = 292
            self.match(ResumeParser.T__24)
            self.state = 293
            self.match(ResumeParser.TEXT)
            self.state = 294
            self.match(ResumeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





