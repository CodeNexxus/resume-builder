# Generated from D:/Uni/semester_6/Compiler/proj/resume-builder/grammar/Resume.g4 by ANTLR 4.13.1
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
        4,1,38,510,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,1,0,1,0,1,0,1,1,1,1,5,1,106,8,
        1,10,1,12,1,109,9,1,1,1,1,1,1,2,1,2,5,2,115,8,2,10,2,12,2,118,9,
        2,1,2,3,2,121,8,2,1,2,5,2,124,8,2,10,2,12,2,127,9,2,1,2,3,2,130,
        8,2,1,2,5,2,133,8,2,10,2,12,2,136,9,2,1,2,3,2,139,8,2,1,3,3,3,142,
        8,3,1,3,5,3,145,8,3,10,3,12,3,148,9,3,1,3,3,3,151,8,3,1,3,5,3,154,
        8,3,10,3,12,3,157,9,3,1,3,3,3,160,8,3,1,3,5,3,163,8,3,10,3,12,3,
        166,9,3,1,3,3,3,169,8,3,1,3,5,3,172,8,3,10,3,12,3,175,9,3,1,3,3,
        3,178,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,
        8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,5,13,
        222,8,13,10,13,12,13,225,9,13,1,14,1,14,1,15,1,15,5,15,231,8,15,
        10,15,12,15,234,9,15,1,15,1,15,5,15,238,8,15,10,15,12,15,241,9,15,
        1,15,3,15,244,8,15,1,15,5,15,247,8,15,10,15,12,15,250,9,15,1,15,
        3,15,253,8,15,1,16,1,16,1,16,1,17,1,17,1,17,5,17,261,8,17,10,17,
        12,17,264,9,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,
        1,21,1,21,5,21,278,8,21,10,21,12,21,281,9,21,1,22,1,22,1,22,1,23,
        1,23,1,24,1,24,1,24,5,24,291,8,24,10,24,12,24,294,9,24,1,25,1,25,
        1,25,1,26,1,26,1,27,1,27,5,27,303,8,27,10,27,12,27,306,9,27,1,27,
        5,27,309,8,27,10,27,12,27,312,9,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,5,28,323,8,28,10,28,12,28,326,9,28,1,29,1,29,1,30,
        1,30,1,31,1,31,5,31,334,8,31,10,31,12,31,337,9,31,1,31,1,31,1,31,
        4,31,342,8,31,11,31,12,31,343,1,32,1,32,1,32,1,32,1,33,1,33,1,34,
        1,34,1,34,1,34,1,34,5,34,357,8,34,10,34,12,34,360,9,34,1,35,1,35,
        1,35,5,35,365,8,35,10,35,12,35,368,9,35,1,35,1,35,1,35,5,35,373,
        8,35,10,35,12,35,376,9,35,1,35,1,35,1,35,5,35,381,8,35,10,35,12,
        35,384,9,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,5,39,394,8,39,
        10,39,12,39,397,9,39,1,39,1,39,1,39,1,39,5,39,403,8,39,10,39,12,
        39,406,9,39,1,40,1,40,1,40,5,40,411,8,40,10,40,12,40,414,9,40,1,
        40,1,40,1,40,5,40,419,8,40,10,40,12,40,422,9,40,1,40,1,40,1,40,5,
        40,427,8,40,10,40,12,40,430,9,40,1,40,1,40,1,40,5,40,435,8,40,10,
        40,12,40,438,9,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,5,41,447,8,
        41,10,41,12,41,450,9,41,1,42,4,42,453,8,42,11,42,12,42,454,1,43,
        1,43,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,45,5,45,467,8,45,10,45,
        12,45,470,9,45,1,46,1,46,1,46,5,46,475,8,46,10,46,12,46,478,9,46,
        1,46,1,46,1,46,5,46,483,8,46,10,46,12,46,486,9,46,1,46,1,46,1,46,
        5,46,491,8,46,10,46,12,46,494,9,46,1,46,1,46,1,46,5,46,499,8,46,
        10,46,12,46,502,9,46,1,47,1,47,1,48,1,48,1,49,1,49,1,49,0,0,50,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,
        92,94,96,98,0,0,506,0,100,1,0,0,0,2,103,1,0,0,0,4,112,1,0,0,0,6,
        141,1,0,0,0,8,179,1,0,0,0,10,182,1,0,0,0,12,203,1,0,0,0,14,205,1,
        0,0,0,16,207,1,0,0,0,18,209,1,0,0,0,20,211,1,0,0,0,22,213,1,0,0,
        0,24,215,1,0,0,0,26,217,1,0,0,0,28,226,1,0,0,0,30,228,1,0,0,0,32,
        254,1,0,0,0,34,257,1,0,0,0,36,265,1,0,0,0,38,270,1,0,0,0,40,272,
        1,0,0,0,42,274,1,0,0,0,44,282,1,0,0,0,46,285,1,0,0,0,48,287,1,0,
        0,0,50,295,1,0,0,0,52,298,1,0,0,0,54,300,1,0,0,0,56,313,1,0,0,0,
        58,327,1,0,0,0,60,329,1,0,0,0,62,331,1,0,0,0,64,345,1,0,0,0,66,349,
        1,0,0,0,68,351,1,0,0,0,70,361,1,0,0,0,72,385,1,0,0,0,74,387,1,0,
        0,0,76,389,1,0,0,0,78,391,1,0,0,0,80,407,1,0,0,0,82,443,1,0,0,0,
        84,452,1,0,0,0,86,456,1,0,0,0,88,458,1,0,0,0,90,460,1,0,0,0,92,471,
        1,0,0,0,94,503,1,0,0,0,96,505,1,0,0,0,98,507,1,0,0,0,100,101,3,2,
        1,0,101,102,5,0,0,1,102,1,1,0,0,0,103,107,3,4,2,0,104,106,5,38,0,
        0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,
        0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,3,6,3,0,111,3,1,0,0,0,
        112,116,3,10,5,0,113,115,5,38,0,0,114,113,1,0,0,0,115,118,1,0,0,
        0,116,114,1,0,0,0,116,117,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,
        0,119,121,3,62,31,0,120,119,1,0,0,0,120,121,1,0,0,0,121,125,1,0,
        0,0,122,124,5,38,0,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,
        0,0,125,126,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,128,130,3,54,
        27,0,129,128,1,0,0,0,129,130,1,0,0,0,130,134,1,0,0,0,131,133,5,38,
        0,0,132,131,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,
        0,0,135,138,1,0,0,0,136,134,1,0,0,0,137,139,3,8,4,0,138,137,1,0,
        0,0,138,139,1,0,0,0,139,5,1,0,0,0,140,142,3,26,13,0,141,140,1,0,
        0,0,141,142,1,0,0,0,142,146,1,0,0,0,143,145,5,38,0,0,144,143,1,0,
        0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,150,1,0,
        0,0,148,146,1,0,0,0,149,151,3,30,15,0,150,149,1,0,0,0,150,151,1,
        0,0,0,151,155,1,0,0,0,152,154,5,38,0,0,153,152,1,0,0,0,154,157,1,
        0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,159,1,0,0,0,157,155,1,
        0,0,0,158,160,3,68,34,0,159,158,1,0,0,0,159,160,1,0,0,0,160,164,
        1,0,0,0,161,163,5,38,0,0,162,161,1,0,0,0,163,166,1,0,0,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,167,169,
        3,78,39,0,168,167,1,0,0,0,168,169,1,0,0,0,169,173,1,0,0,0,170,172,
        5,38,0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,
        1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,176,178,3,90,45,0,177,176,
        1,0,0,0,177,178,1,0,0,0,178,7,1,0,0,0,179,180,5,1,0,0,180,181,3,
        12,6,0,181,9,1,0,0,0,182,183,5,2,0,0,183,184,3,12,6,0,184,185,5,
        38,0,0,185,186,5,3,0,0,186,187,3,14,7,0,187,188,5,38,0,0,188,189,
        5,4,0,0,189,190,3,16,8,0,190,191,5,38,0,0,191,192,5,5,0,0,192,193,
        3,20,10,0,193,194,5,38,0,0,194,195,5,6,0,0,195,196,3,22,11,0,196,
        197,5,38,0,0,197,198,5,7,0,0,198,199,3,24,12,0,199,200,5,38,0,0,
        200,201,5,8,0,0,201,202,3,18,9,0,202,11,1,0,0,0,203,204,5,34,0,0,
        204,13,1,0,0,0,205,206,5,34,0,0,206,15,1,0,0,0,207,208,5,34,0,0,
        208,17,1,0,0,0,209,210,5,34,0,0,210,19,1,0,0,0,211,212,5,33,0,0,
        212,21,1,0,0,0,213,214,5,34,0,0,214,23,1,0,0,0,215,216,5,32,0,0,
        216,25,1,0,0,0,217,223,5,9,0,0,218,219,3,28,14,0,219,220,5,38,0,
        0,220,222,1,0,0,0,221,218,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,
        0,223,224,1,0,0,0,224,27,1,0,0,0,225,223,1,0,0,0,226,227,5,34,0,
        0,227,29,1,0,0,0,228,232,3,32,16,0,229,231,5,38,0,0,230,229,1,0,
        0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,235,1,0,
        0,0,234,232,1,0,0,0,235,239,3,34,17,0,236,238,5,38,0,0,237,236,1,
        0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,243,1,
        0,0,0,241,239,1,0,0,0,242,244,3,42,21,0,243,242,1,0,0,0,243,244,
        1,0,0,0,244,248,1,0,0,0,245,247,5,38,0,0,246,245,1,0,0,0,247,250,
        1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,252,1,0,0,0,250,248,
        1,0,0,0,251,253,3,48,24,0,252,251,1,0,0,0,252,253,1,0,0,0,253,31,
        1,0,0,0,254,255,5,10,0,0,255,256,3,58,29,0,256,33,1,0,0,0,257,258,
        5,11,0,0,258,262,5,38,0,0,259,261,3,36,18,0,260,259,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,35,1,0,0,0,264,262,
        1,0,0,0,265,266,3,38,19,0,266,267,5,12,0,0,267,268,3,40,20,0,268,
        269,5,38,0,0,269,37,1,0,0,0,270,271,5,34,0,0,271,39,1,0,0,0,272,
        273,5,34,0,0,273,41,1,0,0,0,274,275,5,13,0,0,275,279,5,38,0,0,276,
        278,3,44,22,0,277,276,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,
        280,1,0,0,0,280,43,1,0,0,0,281,279,1,0,0,0,282,283,3,46,23,0,283,
        284,5,38,0,0,284,45,1,0,0,0,285,286,5,34,0,0,286,47,1,0,0,0,287,
        288,5,14,0,0,288,292,5,38,0,0,289,291,3,50,25,0,290,289,1,0,0,0,
        291,294,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,49,1,0,0,0,294,
        292,1,0,0,0,295,296,3,52,26,0,296,297,5,38,0,0,297,51,1,0,0,0,298,
        299,5,34,0,0,299,53,1,0,0,0,300,304,5,15,0,0,301,303,5,38,0,0,302,
        301,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,
        310,1,0,0,0,306,304,1,0,0,0,307,309,3,56,28,0,308,307,1,0,0,0,309,
        312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,55,1,0,0,0,312,310,
        1,0,0,0,313,314,5,2,0,0,314,315,3,12,6,0,315,316,5,38,0,0,316,317,
        5,16,0,0,317,318,3,60,30,0,318,319,5,38,0,0,319,320,5,17,0,0,320,
        324,3,58,29,0,321,323,5,38,0,0,322,321,1,0,0,0,323,326,1,0,0,0,324,
        322,1,0,0,0,324,325,1,0,0,0,325,57,1,0,0,0,326,324,1,0,0,0,327,328,
        5,31,0,0,328,59,1,0,0,0,329,330,5,34,0,0,330,61,1,0,0,0,331,335,
        5,18,0,0,332,334,5,38,0,0,333,332,1,0,0,0,334,337,1,0,0,0,335,333,
        1,0,0,0,335,336,1,0,0,0,336,341,1,0,0,0,337,335,1,0,0,0,338,339,
        3,64,32,0,339,340,5,38,0,0,340,342,1,0,0,0,341,338,1,0,0,0,342,343,
        1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,63,1,0,0,0,345,346,3,
        66,33,0,346,347,5,19,0,0,347,348,3,58,29,0,348,65,1,0,0,0,349,350,
        5,34,0,0,350,67,1,0,0,0,351,352,5,20,0,0,352,358,5,38,0,0,353,354,
        3,70,35,0,354,355,5,38,0,0,355,357,1,0,0,0,356,353,1,0,0,0,357,360,
        1,0,0,0,358,356,1,0,0,0,358,359,1,0,0,0,359,69,1,0,0,0,360,358,1,
        0,0,0,361,362,5,21,0,0,362,366,3,72,36,0,363,365,5,38,0,0,364,363,
        1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,369,
        1,0,0,0,368,366,1,0,0,0,369,370,5,22,0,0,370,374,3,74,37,0,371,373,
        5,38,0,0,372,371,1,0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,375,
        1,0,0,0,375,377,1,0,0,0,376,374,1,0,0,0,377,378,5,17,0,0,378,382,
        3,76,38,0,379,381,5,38,0,0,380,379,1,0,0,0,381,384,1,0,0,0,382,380,
        1,0,0,0,382,383,1,0,0,0,383,71,1,0,0,0,384,382,1,0,0,0,385,386,5,
        34,0,0,386,73,1,0,0,0,387,388,5,34,0,0,388,75,1,0,0,0,389,390,5,
        31,0,0,390,77,1,0,0,0,391,395,5,23,0,0,392,394,5,38,0,0,393,392,
        1,0,0,0,394,397,1,0,0,0,395,393,1,0,0,0,395,396,1,0,0,0,396,398,
        1,0,0,0,397,395,1,0,0,0,398,404,3,80,40,0,399,400,5,38,0,0,400,401,
        5,38,0,0,401,403,3,80,40,0,402,399,1,0,0,0,403,406,1,0,0,0,404,402,
        1,0,0,0,404,405,1,0,0,0,405,79,1,0,0,0,406,404,1,0,0,0,407,408,5,
        24,0,0,408,412,3,86,43,0,409,411,5,38,0,0,410,409,1,0,0,0,411,414,
        1,0,0,0,412,410,1,0,0,0,412,413,1,0,0,0,413,415,1,0,0,0,414,412,
        1,0,0,0,415,416,5,25,0,0,416,420,3,88,44,0,417,419,5,38,0,0,418,
        417,1,0,0,0,419,422,1,0,0,0,420,418,1,0,0,0,420,421,1,0,0,0,421,
        423,1,0,0,0,422,420,1,0,0,0,423,424,5,26,0,0,424,428,3,96,48,0,425,
        427,5,38,0,0,426,425,1,0,0,0,427,430,1,0,0,0,428,426,1,0,0,0,428,
        429,1,0,0,0,429,431,1,0,0,0,430,428,1,0,0,0,431,432,5,27,0,0,432,
        436,3,98,49,0,433,435,5,38,0,0,434,433,1,0,0,0,435,438,1,0,0,0,436,
        434,1,0,0,0,436,437,1,0,0,0,437,439,1,0,0,0,438,436,1,0,0,0,439,
        440,5,28,0,0,440,441,5,38,0,0,441,442,3,82,41,0,442,81,1,0,0,0,443,
        448,3,84,42,0,444,445,5,38,0,0,445,447,3,84,42,0,446,444,1,0,0,0,
        447,450,1,0,0,0,448,446,1,0,0,0,448,449,1,0,0,0,449,83,1,0,0,0,450,
        448,1,0,0,0,451,453,5,34,0,0,452,451,1,0,0,0,453,454,1,0,0,0,454,
        452,1,0,0,0,454,455,1,0,0,0,455,85,1,0,0,0,456,457,5,34,0,0,457,
        87,1,0,0,0,458,459,5,34,0,0,459,89,1,0,0,0,460,461,5,29,0,0,461,
        462,5,38,0,0,462,468,3,92,46,0,463,464,5,38,0,0,464,465,5,38,0,0,
        465,467,3,92,46,0,466,463,1,0,0,0,467,470,1,0,0,0,468,466,1,0,0,
        0,468,469,1,0,0,0,469,91,1,0,0,0,470,468,1,0,0,0,471,472,5,16,0,
        0,472,476,3,60,30,0,473,475,5,38,0,0,474,473,1,0,0,0,475,478,1,0,
        0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,479,1,0,0,0,478,476,1,0,
        0,0,479,480,5,30,0,0,480,484,3,94,47,0,481,483,5,38,0,0,482,481,
        1,0,0,0,483,486,1,0,0,0,484,482,1,0,0,0,484,485,1,0,0,0,485,487,
        1,0,0,0,486,484,1,0,0,0,487,488,5,26,0,0,488,492,3,96,48,0,489,491,
        5,38,0,0,490,489,1,0,0,0,491,494,1,0,0,0,492,490,1,0,0,0,492,493,
        1,0,0,0,493,495,1,0,0,0,494,492,1,0,0,0,495,496,5,27,0,0,496,500,
        3,98,49,0,497,499,5,38,0,0,498,497,1,0,0,0,499,502,1,0,0,0,500,498,
        1,0,0,0,500,501,1,0,0,0,501,93,1,0,0,0,502,500,1,0,0,0,503,504,5,
        34,0,0,504,95,1,0,0,0,505,506,5,34,0,0,506,97,1,0,0,0,507,508,5,
        34,0,0,508,99,1,0,0,0,47,107,116,120,125,129,134,138,141,146,150,
        155,159,164,168,173,177,223,232,239,243,248,252,262,279,292,304,
        310,324,335,343,358,366,374,382,395,404,412,420,428,436,448,454,
        468,476,484,492,500
    ]

class ResumeParser ( Parser ):

    grammarFileName = "Resume.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'git-username:'", "'name:'", "'surname:'", 
                     "'job_title:'", "'phone:'", "'city:'", "'gmail:'", 
                     "'birth:'", "'summary:'", "'jobinja:'", "'hard_skills:'", 
                     "','", "'soft_skills:'", "'languages:'", "'certificates:'", 
                     "'institution:'", "'link:'", "'socials:'", "':'", "'projects:'", 
                     "'title:'", "'description:'", "'work_experience:'", 
                     "'company:'", "'position:'", "'start_date:'", "'end_date:'", 
                     "'responsibilities:'", "'educations:'", "'degree:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "URL", "EMAIL", 
                      "PHONE", "TEXT", "INTEGER", "RATING", "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_resume = 1
    RULE_base_info = 2
    RULE_additional_info = 3
    RULE_git_scraper = 4
    RULE_personal_info = 5
    RULE_name = 6
    RULE_surname = 7
    RULE_job_title = 8
    RULE_birth = 9
    RULE_phone = 10
    RULE_city = 11
    RULE_gmail = 12
    RULE_summary = 13
    RULE_value = 14
    RULE_skills = 15
    RULE_jobinja_scraper = 16
    RULE_hard_skills = 17
    RULE_hard_skill = 18
    RULE_hard_skill_name = 19
    RULE_rate = 20
    RULE_soft_skills = 21
    RULE_soft_skill = 22
    RULE_soft_skill_name = 23
    RULE_languages = 24
    RULE_language = 25
    RULE_language_name = 26
    RULE_certificates = 27
    RULE_certificate = 28
    RULE_link = 29
    RULE_institution = 30
    RULE_socials = 31
    RULE_social = 32
    RULE_social_name = 33
    RULE_projects = 34
    RULE_project = 35
    RULE_project_title = 36
    RULE_project_description = 37
    RULE_project_url = 38
    RULE_work_experience = 39
    RULE_job = 40
    RULE_responsibility_list = 41
    RULE_responsibility = 42
    RULE_company = 43
    RULE_position = 44
    RULE_educations = 45
    RULE_education = 46
    RULE_degree = 47
    RULE_start_date = 48
    RULE_end_date = 49

    ruleNames =  [ "start", "resume", "base_info", "additional_info", "git_scraper", 
                   "personal_info", "name", "surname", "job_title", "birth", 
                   "phone", "city", "gmail", "summary", "value", "skills", 
                   "jobinja_scraper", "hard_skills", "hard_skill", "hard_skill_name", 
                   "rate", "soft_skills", "soft_skill", "soft_skill_name", 
                   "languages", "language", "language_name", "certificates", 
                   "certificate", "link", "institution", "socials", "social", 
                   "social_name", "projects", "project", "project_title", 
                   "project_description", "project_url", "work_experience", 
                   "job", "responsibility_list", "responsibility", "company", 
                   "position", "educations", "education", "degree", "start_date", 
                   "end_date" ]

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
    T__28=29
    T__29=30
    URL=31
    EMAIL=32
    PHONE=33
    TEXT=34
    INTEGER=35
    RATING=36
    WS=37
    NEWLINE=38

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
            self.state = 100
            self.resume()
            self.state = 101
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

        def base_info(self):
            return self.getTypedRuleContext(ResumeParser.Base_infoContext,0)


        def additional_info(self):
            return self.getTypedRuleContext(ResumeParser.Additional_infoContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.base_info()
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.match(ResumeParser.NEWLINE) 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 110
            self.additional_info()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_infoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def personal_info(self):
            return self.getTypedRuleContext(ResumeParser.Personal_infoContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def socials(self):
            return self.getTypedRuleContext(ResumeParser.SocialsContext,0)


        def certificates(self):
            return self.getTypedRuleContext(ResumeParser.CertificatesContext,0)


        def git_scraper(self):
            return self.getTypedRuleContext(ResumeParser.Git_scraperContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_base_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_info" ):
                listener.enterBase_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_info" ):
                listener.exitBase_info(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase_info" ):
                return visitor.visitBase_info(self)
            else:
                return visitor.visitChildren(self)




    def base_info(self):

        localctx = ResumeParser.Base_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_base_info)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.personal_info()
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 113
                    self.match(ResumeParser.NEWLINE) 
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 119
                self.socials()


            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    self.match(ResumeParser.NEWLINE) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 128
                self.certificates()


            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    self.match(ResumeParser.NEWLINE) 
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 137
                self.git_scraper()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additional_infoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def summary(self):
            return self.getTypedRuleContext(ResumeParser.SummaryContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def skills(self):
            return self.getTypedRuleContext(ResumeParser.SkillsContext,0)


        def projects(self):
            return self.getTypedRuleContext(ResumeParser.ProjectsContext,0)


        def work_experience(self):
            return self.getTypedRuleContext(ResumeParser.Work_experienceContext,0)


        def educations(self):
            return self.getTypedRuleContext(ResumeParser.EducationsContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_additional_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditional_info" ):
                listener.enterAdditional_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditional_info" ):
                listener.exitAdditional_info(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditional_info" ):
                return visitor.visitAdditional_info(self)
            else:
                return visitor.visitChildren(self)




    def additional_info(self):

        localctx = ResumeParser.Additional_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_additional_info)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 140
                self.summary()


            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.match(ResumeParser.NEWLINE) 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 149
                self.skills()


            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 152
                    self.match(ResumeParser.NEWLINE) 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 158
                self.projects()


            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    self.match(ResumeParser.NEWLINE) 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 167
                self.work_experience()


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 170
                self.match(ResumeParser.NEWLINE)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 176
                self.educations()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Git_scraperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ResumeParser.NameContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_git_scraper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGit_scraper" ):
                listener.enterGit_scraper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGit_scraper" ):
                listener.exitGit_scraper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGit_scraper" ):
                return visitor.visitGit_scraper(self)
            else:
                return visitor.visitChildren(self)




    def git_scraper(self):

        localctx = ResumeParser.Git_scraperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_git_scraper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ResumeParser.T__0)
            self.state = 180
            self.name()
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

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
        self.enterRule(localctx, 10, self.RULE_personal_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ResumeParser.T__1)
            self.state = 183
            self.name()
            self.state = 184
            self.match(ResumeParser.NEWLINE)
            self.state = 185
            self.match(ResumeParser.T__2)
            self.state = 186
            self.surname()
            self.state = 187
            self.match(ResumeParser.NEWLINE)
            self.state = 188
            self.match(ResumeParser.T__3)
            self.state = 189
            self.job_title()
            self.state = 190
            self.match(ResumeParser.NEWLINE)
            self.state = 191
            self.match(ResumeParser.T__4)
            self.state = 192
            self.phone()
            self.state = 193
            self.match(ResumeParser.NEWLINE)
            self.state = 194
            self.match(ResumeParser.T__5)
            self.state = 195
            self.city()
            self.state = 196
            self.match(ResumeParser.NEWLINE)
            self.state = 197
            self.match(ResumeParser.T__6)
            self.state = 198
            self.gmail()
            self.state = 199
            self.match(ResumeParser.NEWLINE)
            self.state = 200
            self.match(ResumeParser.T__7)
            self.state = 201
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
        self.enterRule(localctx, 12, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
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
        self.enterRule(localctx, 14, self.RULE_surname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
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
        self.enterRule(localctx, 16, self.RULE_job_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
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
        self.enterRule(localctx, 18, self.RULE_birth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
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
        self.enterRule(localctx, 20, self.RULE_phone)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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
        self.enterRule(localctx, 22, self.RULE_city)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
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
        self.enterRule(localctx, 24, self.RULE_gmail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.ValueContext)
            else:
                return self.getTypedRuleContext(ResumeParser.ValueContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

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
        self.enterRule(localctx, 26, self.RULE_summary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ResumeParser.T__8)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 218
                self.value()
                self.state = 219
                self.match(ResumeParser.NEWLINE)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ResumeParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
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

        def jobinja_scraper(self):
            return self.getTypedRuleContext(ResumeParser.Jobinja_scraperContext,0)


        def hard_skills(self):
            return self.getTypedRuleContext(ResumeParser.Hard_skillsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

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
        self.enterRule(localctx, 30, self.RULE_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.jobinja_scraper()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 229
                self.match(ResumeParser.NEWLINE)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.hard_skills()
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 236
                    self.match(ResumeParser.NEWLINE) 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 242
                self.soft_skills()


            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 245
                    self.match(ResumeParser.NEWLINE) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 251
                self.languages()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jobinja_scraperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link(self):
            return self.getTypedRuleContext(ResumeParser.LinkContext,0)


        def getRuleIndex(self):
            return ResumeParser.RULE_jobinja_scraper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJobinja_scraper" ):
                listener.enterJobinja_scraper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJobinja_scraper" ):
                listener.exitJobinja_scraper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJobinja_scraper" ):
                return visitor.visitJobinja_scraper(self)
            else:
                return visitor.visitChildren(self)




    def jobinja_scraper(self):

        localctx = ResumeParser.Jobinja_scraperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_jobinja_scraper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(ResumeParser.T__9)
            self.state = 255
            self.link()
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

        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

        def hard_skill(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.Hard_skillContext)
            else:
                return self.getTypedRuleContext(ResumeParser.Hard_skillContext,i)


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
        self.enterRule(localctx, 34, self.RULE_hard_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ResumeParser.T__10)
            self.state = 258
            self.match(ResumeParser.NEWLINE)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 259
                self.hard_skill()
                self.state = 264
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

        def hard_skill_name(self):
            return self.getTypedRuleContext(ResumeParser.Hard_skill_nameContext,0)


        def rate(self):
            return self.getTypedRuleContext(ResumeParser.RateContext,0)


        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

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
        self.enterRule(localctx, 36, self.RULE_hard_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.hard_skill_name()
            self.state = 266
            self.match(ResumeParser.T__11)
            self.state = 267
            self.rate()
            self.state = 268
            self.match(ResumeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hard_skill_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_hard_skill_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHard_skill_name" ):
                listener.enterHard_skill_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHard_skill_name" ):
                listener.exitHard_skill_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHard_skill_name" ):
                return visitor.visitHard_skill_name(self)
            else:
                return visitor.visitChildren(self)




    def hard_skill_name(self):

        localctx = ResumeParser.Hard_skill_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_hard_skill_name)
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


    class RateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_rate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRate" ):
                listener.enterRate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRate" ):
                listener.exitRate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRate" ):
                return visitor.visitRate(self)
            else:
                return visitor.visitChildren(self)




    def rate(self):

        localctx = ResumeParser.RateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_rate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
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

        def soft_skill(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.Soft_skillContext)
            else:
                return self.getTypedRuleContext(ResumeParser.Soft_skillContext,i)


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
        self.enterRule(localctx, 42, self.RULE_soft_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(ResumeParser.T__12)
            self.state = 275
            self.match(ResumeParser.NEWLINE)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 276
                self.soft_skill()
                self.state = 281
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

        def soft_skill_name(self):
            return self.getTypedRuleContext(ResumeParser.Soft_skill_nameContext,0)


        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

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
        self.enterRule(localctx, 44, self.RULE_soft_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.soft_skill_name()
            self.state = 283
            self.match(ResumeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Soft_skill_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_soft_skill_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoft_skill_name" ):
                listener.enterSoft_skill_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoft_skill_name" ):
                listener.exitSoft_skill_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoft_skill_name" ):
                return visitor.visitSoft_skill_name(self)
            else:
                return visitor.visitChildren(self)




    def soft_skill_name(self):

        localctx = ResumeParser.Soft_skill_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_soft_skill_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ResumeParser.TEXT)
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

        def language(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.LanguageContext)
            else:
                return self.getTypedRuleContext(ResumeParser.LanguageContext,i)


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
        self.enterRule(localctx, 48, self.RULE_languages)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ResumeParser.T__13)
            self.state = 288
            self.match(ResumeParser.NEWLINE)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 289
                self.language()
                self.state = 294
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

        def language_name(self):
            return self.getTypedRuleContext(ResumeParser.Language_nameContext,0)


        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

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
        self.enterRule(localctx, 50, self.RULE_language)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.language_name()
            self.state = 296
            self.match(ResumeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Language_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_language_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguage_name" ):
                listener.enterLanguage_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguage_name" ):
                listener.exitLanguage_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguage_name" ):
                return visitor.visitLanguage_name(self)
            else:
                return visitor.visitChildren(self)




    def language_name(self):

        localctx = ResumeParser.Language_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_language_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
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
        self.enterRule(localctx, 54, self.RULE_certificates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ResumeParser.T__14)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 301
                    self.match(ResumeParser.NEWLINE) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 307
                self.certificate()
                self.state = 312
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

        def name(self):
            return self.getTypedRuleContext(ResumeParser.NameContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def institution(self):
            return self.getTypedRuleContext(ResumeParser.InstitutionContext,0)


        def link(self):
            return self.getTypedRuleContext(ResumeParser.LinkContext,0)


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
        self.enterRule(localctx, 56, self.RULE_certificate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(ResumeParser.T__1)
            self.state = 314
            self.name()
            self.state = 315
            self.match(ResumeParser.NEWLINE)
            self.state = 316
            self.match(ResumeParser.T__15)
            self.state = 317
            self.institution()
            self.state = 318
            self.match(ResumeParser.NEWLINE)
            self.state = 319
            self.match(ResumeParser.T__16)
            self.state = 320
            self.link()
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 321
                    self.match(ResumeParser.NEWLINE) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink" ):
                return visitor.visitLink(self)
            else:
                return visitor.visitChildren(self)




    def link(self):

        localctx = ResumeParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ResumeParser.URL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstitutionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_institution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstitution" ):
                listener.enterInstitution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstitution" ):
                listener.exitInstitution(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstitution" ):
                return visitor.visitInstitution(self)
            else:
                return visitor.visitChildren(self)




    def institution(self):

        localctx = ResumeParser.InstitutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_institution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ResumeParser.TEXT)
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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def social(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.SocialContext)
            else:
                return self.getTypedRuleContext(ResumeParser.SocialContext,i)


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
        self.enterRule(localctx, 62, self.RULE_socials)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ResumeParser.T__17)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 332
                self.match(ResumeParser.NEWLINE)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 341 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 338
                self.social()
                self.state = 339
                self.match(ResumeParser.NEWLINE)
                self.state = 343 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

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

        def social_name(self):
            return self.getTypedRuleContext(ResumeParser.Social_nameContext,0)


        def link(self):
            return self.getTypedRuleContext(ResumeParser.LinkContext,0)


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
        self.enterRule(localctx, 64, self.RULE_social)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.social_name()
            self.state = 346
            self.match(ResumeParser.T__18)
            self.state = 347
            self.link()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Social_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_social_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSocial_name" ):
                listener.enterSocial_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSocial_name" ):
                listener.exitSocial_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSocial_name" ):
                return visitor.visitSocial_name(self)
            else:
                return visitor.visitChildren(self)




    def social_name(self):

        localctx = ResumeParser.Social_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_social_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(ResumeParser.TEXT)
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
        self.enterRule(localctx, 68, self.RULE_projects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(ResumeParser.T__19)
            self.state = 352
            self.match(ResumeParser.NEWLINE)
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 353
                self.project()
                self.state = 354
                self.match(ResumeParser.NEWLINE)
                self.state = 360
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

        def project_title(self):
            return self.getTypedRuleContext(ResumeParser.Project_titleContext,0)


        def project_description(self):
            return self.getTypedRuleContext(ResumeParser.Project_descriptionContext,0)


        def project_url(self):
            return self.getTypedRuleContext(ResumeParser.Project_urlContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

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
        self.enterRule(localctx, 70, self.RULE_project)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(ResumeParser.T__20)
            self.state = 362
            self.project_title()
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 363
                self.match(ResumeParser.NEWLINE)
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 369
            self.match(ResumeParser.T__21)
            self.state = 370
            self.project_description()
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 371
                self.match(ResumeParser.NEWLINE)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 377
            self.match(ResumeParser.T__16)
            self.state = 378
            self.project_url()
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 379
                    self.match(ResumeParser.NEWLINE) 
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Project_titleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_project_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject_title" ):
                listener.enterProject_title(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject_title" ):
                listener.exitProject_title(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProject_title" ):
                return visitor.visitProject_title(self)
            else:
                return visitor.visitChildren(self)




    def project_title(self):

        localctx = ResumeParser.Project_titleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_project_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Project_descriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_project_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject_description" ):
                listener.enterProject_description(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject_description" ):
                listener.exitProject_description(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProject_description" ):
                return visitor.visitProject_description(self)
            else:
                return visitor.visitChildren(self)




    def project_description(self):

        localctx = ResumeParser.Project_descriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_project_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Project_urlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_project_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject_url" ):
                listener.enterProject_url(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject_url" ):
                listener.exitProject_url(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProject_url" ):
                return visitor.visitProject_url(self)
            else:
                return visitor.visitChildren(self)




    def project_url(self):

        localctx = ResumeParser.Project_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_project_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(ResumeParser.URL)
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

        def job(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResumeParser.JobContext)
            else:
                return self.getTypedRuleContext(ResumeParser.JobContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

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
        self.enterRule(localctx, 78, self.RULE_work_experience)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(ResumeParser.T__22)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 392
                self.match(ResumeParser.NEWLINE)
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 398
            self.job()
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 399
                    self.match(ResumeParser.NEWLINE)
                    self.state = 400
                    self.match(ResumeParser.NEWLINE)
                    self.state = 401
                    self.job() 
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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

        def company(self):
            return self.getTypedRuleContext(ResumeParser.CompanyContext,0)


        def position(self):
            return self.getTypedRuleContext(ResumeParser.PositionContext,0)


        def start_date(self):
            return self.getTypedRuleContext(ResumeParser.Start_dateContext,0)


        def end_date(self):
            return self.getTypedRuleContext(ResumeParser.End_dateContext,0)


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
        self.enterRule(localctx, 80, self.RULE_job)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(ResumeParser.T__23)
            self.state = 408
            self.company()
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 409
                self.match(ResumeParser.NEWLINE)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 415
            self.match(ResumeParser.T__24)
            self.state = 416
            self.position()
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 417
                self.match(ResumeParser.NEWLINE)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 423
            self.match(ResumeParser.T__25)
            self.state = 424
            self.start_date()
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 425
                self.match(ResumeParser.NEWLINE)
                self.state = 430
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 431
            self.match(ResumeParser.T__26)
            self.state = 432
            self.end_date()
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 433
                self.match(ResumeParser.NEWLINE)
                self.state = 438
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 439
            self.match(ResumeParser.T__27)
            self.state = 440
            self.match(ResumeParser.NEWLINE)
            self.state = 441
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
        self.enterRule(localctx, 82, self.RULE_responsibility_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.responsibility()
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 444
                    self.match(ResumeParser.NEWLINE)
                    self.state = 445
                    self.responsibility() 
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.TEXT)
            else:
                return self.getToken(ResumeParser.TEXT, i)

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
        self.enterRule(localctx, 84, self.RULE_responsibility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 451
                self.match(ResumeParser.TEXT)
                self.state = 454 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompanyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_company

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompany" ):
                listener.enterCompany(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompany" ):
                listener.exitCompany(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompany" ):
                return visitor.visitCompany(self)
            else:
                return visitor.visitChildren(self)




    def company(self):

        localctx = ResumeParser.CompanyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_company)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPosition" ):
                return visitor.visitPosition(self)
            else:
                return visitor.visitChildren(self)




    def position(self):

        localctx = ResumeParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_position)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
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
        self.enterRule(localctx, 90, self.RULE_educations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(ResumeParser.T__28)
            self.state = 461
            self.match(ResumeParser.NEWLINE)
            self.state = 462
            self.education()
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 463
                self.match(ResumeParser.NEWLINE)
                self.state = 464
                self.match(ResumeParser.NEWLINE)
                self.state = 465
                self.education()
                self.state = 470
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

        def institution(self):
            return self.getTypedRuleContext(ResumeParser.InstitutionContext,0)


        def degree(self):
            return self.getTypedRuleContext(ResumeParser.DegreeContext,0)


        def start_date(self):
            return self.getTypedRuleContext(ResumeParser.Start_dateContext,0)


        def end_date(self):
            return self.getTypedRuleContext(ResumeParser.End_dateContext,0)


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
        self.enterRule(localctx, 92, self.RULE_education)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ResumeParser.T__15)
            self.state = 472
            self.institution()
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 473
                self.match(ResumeParser.NEWLINE)
                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 479
            self.match(ResumeParser.T__29)
            self.state = 480
            self.degree()
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 481
                self.match(ResumeParser.NEWLINE)
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 487
            self.match(ResumeParser.T__25)
            self.state = 488
            self.start_date()
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 489
                self.match(ResumeParser.NEWLINE)
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 495
            self.match(ResumeParser.T__26)
            self.state = 496
            self.end_date()
            self.state = 500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 497
                    self.match(ResumeParser.NEWLINE) 
                self.state = 502
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DegreeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_degree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDegree" ):
                listener.enterDegree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDegree" ):
                listener.exitDegree(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDegree" ):
                return visitor.visitDegree(self)
            else:
                return visitor.visitChildren(self)




    def degree(self):

        localctx = ResumeParser.DegreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_degree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_dateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_start_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_date" ):
                listener.enterStart_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_date" ):
                listener.exitStart_date(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_date" ):
                return visitor.visitStart_date(self)
            else:
                return visitor.visitChildren(self)




    def start_date(self):

        localctx = ResumeParser.Start_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_start_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_dateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_end_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_date" ):
                listener.enterEnd_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_date" ):
                listener.exitEnd_date(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_date" ):
                return visitor.visitEnd_date(self)
            else:
                return visitor.visitChildren(self)




    def end_date(self):

        localctx = ResumeParser.End_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_end_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





