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
        4,1,36,479,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,1,0,1,0,1,1,1,1,5,1,102,8,1,10,1,12,1,105,9,1,
        1,1,1,1,1,2,1,2,5,2,111,8,2,10,2,12,2,114,9,2,1,2,3,2,117,8,2,1,
        2,5,2,120,8,2,10,2,12,2,123,9,2,1,2,3,2,126,8,2,1,3,3,3,129,8,3,
        1,3,5,3,132,8,3,10,3,12,3,135,9,3,1,3,3,3,138,8,3,1,3,5,3,141,8,
        3,10,3,12,3,144,9,3,1,3,3,3,147,8,3,1,3,5,3,150,8,3,10,3,12,3,153,
        9,3,1,3,3,3,156,8,3,1,3,5,3,159,8,3,10,3,12,3,162,9,3,1,3,3,3,165,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,5,14,
        210,8,14,10,14,12,14,213,9,14,1,14,3,14,216,8,14,1,14,5,14,219,8,
        14,10,14,12,14,222,9,14,1,14,3,14,225,8,14,1,15,1,15,1,15,5,15,230,
        8,15,10,15,12,15,233,9,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,18,
        1,18,1,19,1,19,1,19,5,19,247,8,19,10,19,12,19,250,9,19,1,20,1,20,
        1,20,1,21,1,21,1,22,1,22,1,22,5,22,260,8,22,10,22,12,22,263,9,22,
        1,23,1,23,1,23,1,24,1,24,1,25,1,25,5,25,272,8,25,10,25,12,25,275,
        9,25,1,25,5,25,278,8,25,10,25,12,25,281,9,25,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,5,26,292,8,26,10,26,12,26,295,9,26,1,27,
        1,27,1,28,1,28,1,29,1,29,5,29,303,8,29,10,29,12,29,306,9,29,1,29,
        1,29,1,29,4,29,311,8,29,11,29,12,29,312,1,30,1,30,1,30,1,30,1,31,
        1,31,1,32,1,32,1,32,1,32,1,32,5,32,326,8,32,10,32,12,32,329,9,32,
        1,33,1,33,1,33,5,33,334,8,33,10,33,12,33,337,9,33,1,33,1,33,1,33,
        5,33,342,8,33,10,33,12,33,345,9,33,1,33,1,33,1,33,5,33,350,8,33,
        10,33,12,33,353,9,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,5,37,
        363,8,37,10,37,12,37,366,9,37,1,37,1,37,1,37,1,37,5,37,372,8,37,
        10,37,12,37,375,9,37,1,38,1,38,1,38,5,38,380,8,38,10,38,12,38,383,
        9,38,1,38,1,38,1,38,5,38,388,8,38,10,38,12,38,391,9,38,1,38,1,38,
        1,38,5,38,396,8,38,10,38,12,38,399,9,38,1,38,1,38,1,38,5,38,404,
        8,38,10,38,12,38,407,9,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,5,39,
        416,8,39,10,39,12,39,419,9,39,1,40,4,40,422,8,40,11,40,12,40,423,
        1,41,1,41,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,5,43,436,8,43,
        10,43,12,43,439,9,43,1,44,1,44,1,44,5,44,444,8,44,10,44,12,44,447,
        9,44,1,44,1,44,1,44,5,44,452,8,44,10,44,12,44,455,9,44,1,44,1,44,
        1,44,5,44,460,8,44,10,44,12,44,463,9,44,1,44,1,44,1,44,5,44,468,
        8,44,10,44,12,44,471,9,44,1,45,1,45,1,46,1,46,1,47,1,47,1,47,0,0,
        48,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,92,94,0,0,473,0,96,1,0,0,0,2,99,1,0,0,0,4,108,1,0,0,0,6,128,
        1,0,0,0,8,166,1,0,0,0,10,187,1,0,0,0,12,189,1,0,0,0,14,191,1,0,0,
        0,16,193,1,0,0,0,18,195,1,0,0,0,20,197,1,0,0,0,22,199,1,0,0,0,24,
        201,1,0,0,0,26,205,1,0,0,0,28,207,1,0,0,0,30,226,1,0,0,0,32,234,
        1,0,0,0,34,239,1,0,0,0,36,241,1,0,0,0,38,243,1,0,0,0,40,251,1,0,
        0,0,42,254,1,0,0,0,44,256,1,0,0,0,46,264,1,0,0,0,48,267,1,0,0,0,
        50,269,1,0,0,0,52,282,1,0,0,0,54,296,1,0,0,0,56,298,1,0,0,0,58,300,
        1,0,0,0,60,314,1,0,0,0,62,318,1,0,0,0,64,320,1,0,0,0,66,330,1,0,
        0,0,68,354,1,0,0,0,70,356,1,0,0,0,72,358,1,0,0,0,74,360,1,0,0,0,
        76,376,1,0,0,0,78,412,1,0,0,0,80,421,1,0,0,0,82,425,1,0,0,0,84,427,
        1,0,0,0,86,429,1,0,0,0,88,440,1,0,0,0,90,472,1,0,0,0,92,474,1,0,
        0,0,94,476,1,0,0,0,96,97,3,2,1,0,97,98,5,0,0,1,98,1,1,0,0,0,99,103,
        3,4,2,0,100,102,5,36,0,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,
        1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,
        3,6,3,0,107,3,1,0,0,0,108,112,3,8,4,0,109,111,5,36,0,0,110,109,1,
        0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,116,1,
        0,0,0,114,112,1,0,0,0,115,117,3,58,29,0,116,115,1,0,0,0,116,117,
        1,0,0,0,117,121,1,0,0,0,118,120,5,36,0,0,119,118,1,0,0,0,120,123,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,124,126,3,50,25,0,125,124,1,0,0,0,125,126,1,0,0,0,126,5,
        1,0,0,0,127,129,3,24,12,0,128,127,1,0,0,0,128,129,1,0,0,0,129,133,
        1,0,0,0,130,132,5,36,0,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,
        1,0,0,0,133,134,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,136,138,
        3,28,14,0,137,136,1,0,0,0,137,138,1,0,0,0,138,142,1,0,0,0,139,141,
        5,36,0,0,140,139,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,
        1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,145,147,3,64,32,0,146,145,
        1,0,0,0,146,147,1,0,0,0,147,151,1,0,0,0,148,150,5,36,0,0,149,148,
        1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,155,
        1,0,0,0,153,151,1,0,0,0,154,156,3,74,37,0,155,154,1,0,0,0,155,156,
        1,0,0,0,156,160,1,0,0,0,157,159,5,36,0,0,158,157,1,0,0,0,159,162,
        1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,164,1,0,0,0,162,160,
        1,0,0,0,163,165,3,86,43,0,164,163,1,0,0,0,164,165,1,0,0,0,165,7,
        1,0,0,0,166,167,5,1,0,0,167,168,3,10,5,0,168,169,5,36,0,0,169,170,
        5,2,0,0,170,171,3,12,6,0,171,172,5,36,0,0,172,173,5,3,0,0,173,174,
        3,14,7,0,174,175,5,36,0,0,175,176,5,4,0,0,176,177,3,18,9,0,177,178,
        5,36,0,0,178,179,5,5,0,0,179,180,3,20,10,0,180,181,5,36,0,0,181,
        182,5,6,0,0,182,183,3,22,11,0,183,184,5,36,0,0,184,185,5,7,0,0,185,
        186,3,16,8,0,186,9,1,0,0,0,187,188,5,32,0,0,188,11,1,0,0,0,189,190,
        5,32,0,0,190,13,1,0,0,0,191,192,5,32,0,0,192,15,1,0,0,0,193,194,
        5,32,0,0,194,17,1,0,0,0,195,196,5,31,0,0,196,19,1,0,0,0,197,198,
        5,32,0,0,198,21,1,0,0,0,199,200,5,30,0,0,200,23,1,0,0,0,201,202,
        5,8,0,0,202,203,3,26,13,0,203,204,5,36,0,0,204,25,1,0,0,0,205,206,
        5,32,0,0,206,27,1,0,0,0,207,211,3,30,15,0,208,210,5,36,0,0,209,208,
        1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,214,216,3,38,19,0,215,214,1,0,0,0,215,216,
        1,0,0,0,216,220,1,0,0,0,217,219,5,36,0,0,218,217,1,0,0,0,219,222,
        1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,224,1,0,0,0,222,220,
        1,0,0,0,223,225,3,44,22,0,224,223,1,0,0,0,224,225,1,0,0,0,225,29,
        1,0,0,0,226,227,5,9,0,0,227,231,5,36,0,0,228,230,3,32,16,0,229,228,
        1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,31,1,
        0,0,0,233,231,1,0,0,0,234,235,3,34,17,0,235,236,5,10,0,0,236,237,
        3,36,18,0,237,238,5,36,0,0,238,33,1,0,0,0,239,240,5,32,0,0,240,35,
        1,0,0,0,241,242,5,32,0,0,242,37,1,0,0,0,243,244,5,11,0,0,244,248,
        5,36,0,0,245,247,3,40,20,0,246,245,1,0,0,0,247,250,1,0,0,0,248,246,
        1,0,0,0,248,249,1,0,0,0,249,39,1,0,0,0,250,248,1,0,0,0,251,252,3,
        42,21,0,252,253,5,36,0,0,253,41,1,0,0,0,254,255,5,32,0,0,255,43,
        1,0,0,0,256,257,5,12,0,0,257,261,5,36,0,0,258,260,3,46,23,0,259,
        258,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,
        45,1,0,0,0,263,261,1,0,0,0,264,265,3,48,24,0,265,266,5,36,0,0,266,
        47,1,0,0,0,267,268,5,32,0,0,268,49,1,0,0,0,269,273,5,13,0,0,270,
        272,5,36,0,0,271,270,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,
        274,1,0,0,0,274,279,1,0,0,0,275,273,1,0,0,0,276,278,3,52,26,0,277,
        276,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,
        51,1,0,0,0,281,279,1,0,0,0,282,283,5,1,0,0,283,284,3,10,5,0,284,
        285,5,36,0,0,285,286,5,14,0,0,286,287,3,56,28,0,287,288,5,36,0,0,
        288,289,5,15,0,0,289,293,3,54,27,0,290,292,5,36,0,0,291,290,1,0,
        0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,53,1,0,0,
        0,295,293,1,0,0,0,296,297,5,29,0,0,297,55,1,0,0,0,298,299,5,32,0,
        0,299,57,1,0,0,0,300,304,5,16,0,0,301,303,5,36,0,0,302,301,1,0,0,
        0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,310,1,0,0,
        0,306,304,1,0,0,0,307,308,3,60,30,0,308,309,5,36,0,0,309,311,1,0,
        0,0,310,307,1,0,0,0,311,312,1,0,0,0,312,310,1,0,0,0,312,313,1,0,
        0,0,313,59,1,0,0,0,314,315,3,62,31,0,315,316,5,17,0,0,316,317,3,
        54,27,0,317,61,1,0,0,0,318,319,5,32,0,0,319,63,1,0,0,0,320,321,5,
        18,0,0,321,327,5,36,0,0,322,323,3,66,33,0,323,324,5,36,0,0,324,326,
        1,0,0,0,325,322,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,
        1,0,0,0,328,65,1,0,0,0,329,327,1,0,0,0,330,331,5,19,0,0,331,335,
        3,68,34,0,332,334,5,36,0,0,333,332,1,0,0,0,334,337,1,0,0,0,335,333,
        1,0,0,0,335,336,1,0,0,0,336,338,1,0,0,0,337,335,1,0,0,0,338,339,
        5,20,0,0,339,343,3,70,35,0,340,342,5,36,0,0,341,340,1,0,0,0,342,
        345,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,346,1,0,0,0,345,
        343,1,0,0,0,346,347,5,15,0,0,347,351,3,72,36,0,348,350,5,36,0,0,
        349,348,1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,
        352,67,1,0,0,0,353,351,1,0,0,0,354,355,5,32,0,0,355,69,1,0,0,0,356,
        357,5,32,0,0,357,71,1,0,0,0,358,359,5,29,0,0,359,73,1,0,0,0,360,
        364,5,21,0,0,361,363,5,36,0,0,362,361,1,0,0,0,363,366,1,0,0,0,364,
        362,1,0,0,0,364,365,1,0,0,0,365,367,1,0,0,0,366,364,1,0,0,0,367,
        373,3,76,38,0,368,369,5,36,0,0,369,370,5,36,0,0,370,372,3,76,38,
        0,371,368,1,0,0,0,372,375,1,0,0,0,373,371,1,0,0,0,373,374,1,0,0,
        0,374,75,1,0,0,0,375,373,1,0,0,0,376,377,5,22,0,0,377,381,3,82,41,
        0,378,380,5,36,0,0,379,378,1,0,0,0,380,383,1,0,0,0,381,379,1,0,0,
        0,381,382,1,0,0,0,382,384,1,0,0,0,383,381,1,0,0,0,384,385,5,23,0,
        0,385,389,3,84,42,0,386,388,5,36,0,0,387,386,1,0,0,0,388,391,1,0,
        0,0,389,387,1,0,0,0,389,390,1,0,0,0,390,392,1,0,0,0,391,389,1,0,
        0,0,392,393,5,24,0,0,393,397,3,92,46,0,394,396,5,36,0,0,395,394,
        1,0,0,0,396,399,1,0,0,0,397,395,1,0,0,0,397,398,1,0,0,0,398,400,
        1,0,0,0,399,397,1,0,0,0,400,401,5,25,0,0,401,405,3,94,47,0,402,404,
        5,36,0,0,403,402,1,0,0,0,404,407,1,0,0,0,405,403,1,0,0,0,405,406,
        1,0,0,0,406,408,1,0,0,0,407,405,1,0,0,0,408,409,5,26,0,0,409,410,
        5,36,0,0,410,411,3,78,39,0,411,77,1,0,0,0,412,417,3,80,40,0,413,
        414,5,36,0,0,414,416,3,80,40,0,415,413,1,0,0,0,416,419,1,0,0,0,417,
        415,1,0,0,0,417,418,1,0,0,0,418,79,1,0,0,0,419,417,1,0,0,0,420,422,
        5,32,0,0,421,420,1,0,0,0,422,423,1,0,0,0,423,421,1,0,0,0,423,424,
        1,0,0,0,424,81,1,0,0,0,425,426,5,32,0,0,426,83,1,0,0,0,427,428,5,
        32,0,0,428,85,1,0,0,0,429,430,5,27,0,0,430,431,5,36,0,0,431,437,
        3,88,44,0,432,433,5,36,0,0,433,434,5,36,0,0,434,436,3,88,44,0,435,
        432,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,
        87,1,0,0,0,439,437,1,0,0,0,440,441,5,14,0,0,441,445,3,56,28,0,442,
        444,5,36,0,0,443,442,1,0,0,0,444,447,1,0,0,0,445,443,1,0,0,0,445,
        446,1,0,0,0,446,448,1,0,0,0,447,445,1,0,0,0,448,449,5,28,0,0,449,
        453,3,90,45,0,450,452,5,36,0,0,451,450,1,0,0,0,452,455,1,0,0,0,453,
        451,1,0,0,0,453,454,1,0,0,0,454,456,1,0,0,0,455,453,1,0,0,0,456,
        457,5,24,0,0,457,461,3,92,46,0,458,460,5,36,0,0,459,458,1,0,0,0,
        460,463,1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,462,464,1,0,0,0,
        463,461,1,0,0,0,464,465,5,25,0,0,465,469,3,94,47,0,466,468,5,36,
        0,0,467,466,1,0,0,0,468,471,1,0,0,0,469,467,1,0,0,0,469,470,1,0,
        0,0,470,89,1,0,0,0,471,469,1,0,0,0,472,473,5,32,0,0,473,91,1,0,0,
        0,474,475,5,32,0,0,475,93,1,0,0,0,476,477,5,32,0,0,477,95,1,0,0,
        0,43,103,112,116,121,125,128,133,137,142,146,151,155,160,164,211,
        215,220,224,231,248,261,273,279,293,304,312,327,335,343,351,364,
        373,381,389,397,405,417,423,437,445,453,461,469
    ]

class ResumeParser ( Parser ):

    grammarFileName = "Resume.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'name:'", "'surname:'", "'job_title:'", 
                     "'phone:'", "'city:'", "'gmail:'", "'birth:'", "'summary:'", 
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
                      "<INVALID>", "URL", "EMAIL", "PHONE", "TEXT", "INTEGER", 
                      "RATING", "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_resume = 1
    RULE_base_info = 2
    RULE_additional_info = 3
    RULE_personal_info = 4
    RULE_name = 5
    RULE_surname = 6
    RULE_job_title = 7
    RULE_birth = 8
    RULE_phone = 9
    RULE_city = 10
    RULE_gmail = 11
    RULE_summary = 12
    RULE_value = 13
    RULE_skills = 14
    RULE_hard_skills = 15
    RULE_hard_skill = 16
    RULE_hard_skill_name = 17
    RULE_rate = 18
    RULE_soft_skills = 19
    RULE_soft_skill = 20
    RULE_soft_skill_name = 21
    RULE_languages = 22
    RULE_language = 23
    RULE_language_name = 24
    RULE_certificates = 25
    RULE_certificate = 26
    RULE_link = 27
    RULE_institution = 28
    RULE_socials = 29
    RULE_social = 30
    RULE_social_name = 31
    RULE_projects = 32
    RULE_project = 33
    RULE_project_title = 34
    RULE_project_description = 35
    RULE_project_url = 36
    RULE_work_experience = 37
    RULE_job = 38
    RULE_responsibility_list = 39
    RULE_responsibility = 40
    RULE_company = 41
    RULE_position = 42
    RULE_educations = 43
    RULE_education = 44
    RULE_degree = 45
    RULE_start_date = 46
    RULE_end_date = 47

    ruleNames =  [ "start", "resume", "base_info", "additional_info", "personal_info", 
                   "name", "surname", "job_title", "birth", "phone", "city", 
                   "gmail", "summary", "value", "skills", "hard_skills", 
                   "hard_skill", "hard_skill_name", "rate", "soft_skills", 
                   "soft_skill", "soft_skill_name", "languages", "language", 
                   "language_name", "certificates", "certificate", "link", 
                   "institution", "socials", "social", "social_name", "projects", 
                   "project", "project_title", "project_description", "project_url", 
                   "work_experience", "job", "responsibility_list", "responsibility", 
                   "company", "position", "educations", "education", "degree", 
                   "start_date", "end_date" ]

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
    URL=29
    EMAIL=30
    PHONE=31
    TEXT=32
    INTEGER=33
    RATING=34
    WS=35
    NEWLINE=36

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
            self.state = 96
            self.resume()
            self.state = 97
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
            self.state = 99
            self.base_info()
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 100
                    self.match(ResumeParser.NEWLINE) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 106
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
            self.state = 108
            self.personal_info()
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 109
                    self.match(ResumeParser.NEWLINE) 
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 115
                self.socials()


            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 118
                    self.match(ResumeParser.NEWLINE) 
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 124
                self.certificates()


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
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 127
                self.summary()


            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 130
                    self.match(ResumeParser.NEWLINE) 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 136
                self.skills()


            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 139
                    self.match(ResumeParser.NEWLINE) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 145
                self.projects()


            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 148
                    self.match(ResumeParser.NEWLINE) 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 154
                self.work_experience()


            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 157
                self.match(ResumeParser.NEWLINE)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 163
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
        self.enterRule(localctx, 8, self.RULE_personal_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(ResumeParser.T__0)
            self.state = 167
            self.name()
            self.state = 168
            self.match(ResumeParser.NEWLINE)
            self.state = 169
            self.match(ResumeParser.T__1)
            self.state = 170
            self.surname()
            self.state = 171
            self.match(ResumeParser.NEWLINE)
            self.state = 172
            self.match(ResumeParser.T__2)
            self.state = 173
            self.job_title()
            self.state = 174
            self.match(ResumeParser.NEWLINE)
            self.state = 175
            self.match(ResumeParser.T__3)
            self.state = 176
            self.phone()
            self.state = 177
            self.match(ResumeParser.NEWLINE)
            self.state = 178
            self.match(ResumeParser.T__4)
            self.state = 179
            self.city()
            self.state = 180
            self.match(ResumeParser.NEWLINE)
            self.state = 181
            self.match(ResumeParser.T__5)
            self.state = 182
            self.gmail()
            self.state = 183
            self.match(ResumeParser.NEWLINE)
            self.state = 184
            self.match(ResumeParser.T__6)
            self.state = 185
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
        self.enterRule(localctx, 10, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
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
        self.enterRule(localctx, 12, self.RULE_surname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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
        self.enterRule(localctx, 14, self.RULE_job_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
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
        self.enterRule(localctx, 16, self.RULE_birth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
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
        self.enterRule(localctx, 18, self.RULE_phone)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 20, self.RULE_city)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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
        self.enterRule(localctx, 22, self.RULE_gmail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
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

        def value(self):
            return self.getTypedRuleContext(ResumeParser.ValueContext,0)


        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

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
        self.enterRule(localctx, 24, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(ResumeParser.T__7)
            self.state = 202
            self.value()
            self.state = 203
            self.match(ResumeParser.NEWLINE)
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
        self.enterRule(localctx, 26, self.RULE_value)
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


    class SkillsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 28, self.RULE_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.hard_skills()
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 208
                    self.match(ResumeParser.NEWLINE) 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 214
                self.soft_skills()


            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 217
                    self.match(ResumeParser.NEWLINE) 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 223
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
        self.enterRule(localctx, 30, self.RULE_hard_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ResumeParser.T__8)
            self.state = 227
            self.match(ResumeParser.NEWLINE)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 228
                self.hard_skill()
                self.state = 233
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
        self.enterRule(localctx, 32, self.RULE_hard_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.hard_skill_name()
            self.state = 235
            self.match(ResumeParser.T__9)
            self.state = 236
            self.rate()
            self.state = 237
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
        self.enterRule(localctx, 34, self.RULE_hard_skill_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
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
        self.enterRule(localctx, 36, self.RULE_rate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
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
        self.enterRule(localctx, 38, self.RULE_soft_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ResumeParser.T__10)
            self.state = 244
            self.match(ResumeParser.NEWLINE)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 245
                self.soft_skill()
                self.state = 250
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
        self.enterRule(localctx, 40, self.RULE_soft_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.soft_skill_name()
            self.state = 252
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
        self.enterRule(localctx, 42, self.RULE_soft_skill_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self.enterRule(localctx, 44, self.RULE_languages)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ResumeParser.T__11)
            self.state = 257
            self.match(ResumeParser.NEWLINE)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 258
                self.language()
                self.state = 263
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
        self.enterRule(localctx, 46, self.RULE_language)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.language_name()
            self.state = 265
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
        self.enterRule(localctx, 48, self.RULE_language_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
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
        self.enterRule(localctx, 50, self.RULE_certificates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ResumeParser.T__12)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 270
                    self.match(ResumeParser.NEWLINE) 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 276
                self.certificate()
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
        self.enterRule(localctx, 52, self.RULE_certificate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ResumeParser.T__0)
            self.state = 283
            self.name()
            self.state = 284
            self.match(ResumeParser.NEWLINE)
            self.state = 285
            self.match(ResumeParser.T__13)
            self.state = 286
            self.institution()
            self.state = 287
            self.match(ResumeParser.NEWLINE)
            self.state = 288
            self.match(ResumeParser.T__14)
            self.state = 289
            self.link()
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 290
                    self.match(ResumeParser.NEWLINE) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
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
        self.enterRule(localctx, 56, self.RULE_institution)
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
        self.enterRule(localctx, 58, self.RULE_socials)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ResumeParser.T__15)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 301
                self.match(ResumeParser.NEWLINE)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 307
                self.social()
                self.state = 308
                self.match(ResumeParser.NEWLINE)
                self.state = 312 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
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
        self.enterRule(localctx, 60, self.RULE_social)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.social_name()
            self.state = 315
            self.match(ResumeParser.T__16)
            self.state = 316
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
        self.enterRule(localctx, 62, self.RULE_social_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
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
        self.enterRule(localctx, 64, self.RULE_projects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ResumeParser.T__17)
            self.state = 321
            self.match(ResumeParser.NEWLINE)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 322
                self.project()
                self.state = 323
                self.match(ResumeParser.NEWLINE)
                self.state = 329
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
        self.enterRule(localctx, 66, self.RULE_project)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(ResumeParser.T__18)
            self.state = 331
            self.project_title()
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 332
                self.match(ResumeParser.NEWLINE)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 338
            self.match(ResumeParser.T__19)
            self.state = 339
            self.project_description()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 340
                self.match(ResumeParser.NEWLINE)
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            self.match(ResumeParser.T__14)
            self.state = 347
            self.project_url()
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 348
                    self.match(ResumeParser.NEWLINE) 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_project_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
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
        self.enterRule(localctx, 70, self.RULE_project_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
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
        self.enterRule(localctx, 72, self.RULE_project_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
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
        self.enterRule(localctx, 74, self.RULE_work_experience)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(ResumeParser.T__20)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 361
                self.match(ResumeParser.NEWLINE)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 367
            self.job()
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 368
                    self.match(ResumeParser.NEWLINE)
                    self.state = 369
                    self.match(ResumeParser.NEWLINE)
                    self.state = 370
                    self.job() 
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 76, self.RULE_job)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(ResumeParser.T__21)
            self.state = 377
            self.company()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 378
                self.match(ResumeParser.NEWLINE)
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 384
            self.match(ResumeParser.T__22)
            self.state = 385
            self.position()
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 386
                self.match(ResumeParser.NEWLINE)
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 392
            self.match(ResumeParser.T__23)
            self.state = 393
            self.start_date()
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 394
                self.match(ResumeParser.NEWLINE)
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 400
            self.match(ResumeParser.T__24)
            self.state = 401
            self.end_date()
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 402
                self.match(ResumeParser.NEWLINE)
                self.state = 407
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 408
            self.match(ResumeParser.T__25)
            self.state = 409
            self.match(ResumeParser.NEWLINE)
            self.state = 410
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
        self.enterRule(localctx, 78, self.RULE_responsibility_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.responsibility()
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 413
                    self.match(ResumeParser.NEWLINE)
                    self.state = 414
                    self.responsibility() 
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_responsibility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 420
                self.match(ResumeParser.TEXT)
                self.state = 423 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
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
        self.enterRule(localctx, 82, self.RULE_company)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
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
        self.enterRule(localctx, 84, self.RULE_position)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
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
        self.enterRule(localctx, 86, self.RULE_educations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(ResumeParser.T__26)
            self.state = 430
            self.match(ResumeParser.NEWLINE)
            self.state = 431
            self.education()
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 432
                self.match(ResumeParser.NEWLINE)
                self.state = 433
                self.match(ResumeParser.NEWLINE)
                self.state = 434
                self.education()
                self.state = 439
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
        self.enterRule(localctx, 88, self.RULE_education)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(ResumeParser.T__13)
            self.state = 441
            self.institution()
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 442
                self.match(ResumeParser.NEWLINE)
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 448
            self.match(ResumeParser.T__27)
            self.state = 449
            self.degree()
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 450
                self.match(ResumeParser.NEWLINE)
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 456
            self.match(ResumeParser.T__23)
            self.state = 457
            self.start_date()
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 458
                self.match(ResumeParser.NEWLINE)
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 464
            self.match(ResumeParser.T__24)
            self.state = 465
            self.end_date()
            self.state = 469
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 466
                    self.match(ResumeParser.NEWLINE) 
                self.state = 471
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_degree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
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
        self.enterRule(localctx, 92, self.RULE_start_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
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
        self.enterRule(localctx, 94, self.RULE_end_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





