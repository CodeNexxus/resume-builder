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
        4,1,36,462,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,1,1,1,
        5,1,82,8,1,10,1,12,1,85,9,1,1,1,3,1,88,8,1,1,1,5,1,91,8,1,10,1,12,
        1,94,9,1,1,1,3,1,97,8,1,1,1,5,1,100,8,1,10,1,12,1,103,9,1,1,1,3,
        1,106,8,1,1,1,5,1,109,8,1,10,1,12,1,112,9,1,1,1,3,1,115,8,1,1,1,
        5,1,118,8,1,10,1,12,1,121,9,1,1,1,3,1,124,8,1,1,1,5,1,127,8,1,10,
        1,12,1,130,9,1,1,1,3,1,133,8,1,1,1,5,1,136,8,1,10,1,12,1,139,9,1,
        1,1,3,1,142,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,
        12,5,12,187,8,12,10,12,12,12,190,9,12,1,12,3,12,193,8,12,1,12,5,
        12,196,8,12,10,12,12,12,199,9,12,1,12,3,12,202,8,12,1,13,1,13,1,
        13,5,13,207,8,13,10,13,12,13,210,9,13,1,14,1,14,1,14,1,14,1,14,1,
        15,1,15,1,16,1,16,1,17,1,17,1,17,5,17,224,8,17,10,17,12,17,227,9,
        17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,5,20,237,8,20,10,20,12,
        20,240,9,20,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,5,23,250,8,23,
        10,23,12,23,253,9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        5,24,264,8,24,10,24,12,24,267,9,24,1,25,1,25,1,26,1,26,1,27,1,27,
        1,27,1,27,1,28,5,28,278,8,28,10,28,12,28,281,9,28,1,29,1,29,1,29,
        1,29,1,29,1,30,1,30,1,30,1,30,1,30,5,30,293,8,30,10,30,12,30,296,
        9,30,1,31,1,31,1,31,5,31,301,8,31,10,31,12,31,304,9,31,1,31,1,31,
        1,31,5,31,309,8,31,10,31,12,31,312,9,31,1,31,1,31,1,31,5,31,317,
        8,31,10,31,12,31,320,9,31,1,32,1,32,5,32,324,8,32,10,32,12,32,327,
        9,32,1,32,1,32,1,32,1,32,5,32,333,8,32,10,32,12,32,336,9,32,1,33,
        1,33,4,33,340,8,33,11,33,12,33,341,1,33,5,33,345,8,33,10,33,12,33,
        348,9,33,1,33,1,33,4,33,352,8,33,11,33,12,33,353,1,33,5,33,357,8,
        33,10,33,12,33,360,9,33,1,33,1,33,4,33,364,8,33,11,33,12,33,365,
        1,33,5,33,369,8,33,10,33,12,33,372,9,33,1,33,1,33,4,33,376,8,33,
        11,33,12,33,377,1,33,5,33,381,8,33,10,33,12,33,384,9,33,1,33,1,33,
        1,33,1,33,1,34,1,34,1,34,5,34,393,8,34,10,34,12,34,396,9,34,1,35,
        4,35,399,8,35,11,35,12,35,400,1,36,1,36,1,36,1,36,1,36,1,36,5,36,
        409,8,36,10,36,12,36,412,9,36,1,37,1,37,4,37,416,8,37,11,37,12,37,
        417,1,37,5,37,421,8,37,10,37,12,37,424,9,37,1,37,1,37,4,37,428,8,
        37,11,37,12,37,429,1,37,5,37,433,8,37,10,37,12,37,436,9,37,1,37,
        1,37,4,37,440,8,37,11,37,12,37,441,1,37,5,37,445,8,37,10,37,12,37,
        448,9,37,1,37,1,37,4,37,452,8,37,11,37,12,37,453,1,37,5,37,457,8,
        37,10,37,12,37,460,9,37,1,37,0,0,38,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,0,0,472,0,76,1,0,0,0,2,79,1,0,0,0,4,143,1,0,0,0,6,
        164,1,0,0,0,8,166,1,0,0,0,10,168,1,0,0,0,12,170,1,0,0,0,14,172,1,
        0,0,0,16,174,1,0,0,0,18,176,1,0,0,0,20,178,1,0,0,0,22,182,1,0,0,
        0,24,184,1,0,0,0,26,203,1,0,0,0,28,211,1,0,0,0,30,216,1,0,0,0,32,
        218,1,0,0,0,34,220,1,0,0,0,36,228,1,0,0,0,38,231,1,0,0,0,40,233,
        1,0,0,0,42,241,1,0,0,0,44,244,1,0,0,0,46,246,1,0,0,0,48,254,1,0,
        0,0,50,268,1,0,0,0,52,270,1,0,0,0,54,272,1,0,0,0,56,279,1,0,0,0,
        58,282,1,0,0,0,60,287,1,0,0,0,62,297,1,0,0,0,64,321,1,0,0,0,66,337,
        1,0,0,0,68,389,1,0,0,0,70,398,1,0,0,0,72,402,1,0,0,0,74,413,1,0,
        0,0,76,77,3,2,1,0,77,78,5,0,0,1,78,1,1,0,0,0,79,83,3,4,2,0,80,82,
        5,36,0,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,
        84,87,1,0,0,0,85,83,1,0,0,0,86,88,3,20,10,0,87,86,1,0,0,0,87,88,
        1,0,0,0,88,92,1,0,0,0,89,91,5,36,0,0,90,89,1,0,0,0,91,94,1,0,0,0,
        92,90,1,0,0,0,92,93,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,95,97,3,
        24,12,0,96,95,1,0,0,0,96,97,1,0,0,0,97,101,1,0,0,0,98,100,5,36,0,
        0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,
        105,1,0,0,0,103,101,1,0,0,0,104,106,3,46,23,0,105,104,1,0,0,0,105,
        106,1,0,0,0,106,110,1,0,0,0,107,109,5,36,0,0,108,107,1,0,0,0,109,
        112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,113,115,3,54,27,0,114,113,1,0,0,0,114,115,1,0,0,0,115,
        119,1,0,0,0,116,118,5,36,0,0,117,116,1,0,0,0,118,121,1,0,0,0,119,
        117,1,0,0,0,119,120,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,122,
        124,3,60,30,0,123,122,1,0,0,0,123,124,1,0,0,0,124,128,1,0,0,0,125,
        127,5,36,0,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,
        129,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,131,133,3,64,32,0,132,
        131,1,0,0,0,132,133,1,0,0,0,133,137,1,0,0,0,134,136,5,36,0,0,135,
        134,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,
        141,1,0,0,0,139,137,1,0,0,0,140,142,3,72,36,0,141,140,1,0,0,0,141,
        142,1,0,0,0,142,3,1,0,0,0,143,144,5,1,0,0,144,145,3,6,3,0,145,146,
        5,36,0,0,146,147,5,2,0,0,147,148,3,8,4,0,148,149,5,36,0,0,149,150,
        5,3,0,0,150,151,3,10,5,0,151,152,5,36,0,0,152,153,5,4,0,0,153,154,
        3,14,7,0,154,155,5,36,0,0,155,156,5,5,0,0,156,157,3,16,8,0,157,158,
        5,36,0,0,158,159,5,6,0,0,159,160,3,18,9,0,160,161,5,36,0,0,161,162,
        5,7,0,0,162,163,3,12,6,0,163,5,1,0,0,0,164,165,5,32,0,0,165,7,1,
        0,0,0,166,167,5,32,0,0,167,9,1,0,0,0,168,169,5,32,0,0,169,11,1,0,
        0,0,170,171,5,32,0,0,171,13,1,0,0,0,172,173,5,31,0,0,173,15,1,0,
        0,0,174,175,5,32,0,0,175,17,1,0,0,0,176,177,5,30,0,0,177,19,1,0,
        0,0,178,179,5,8,0,0,179,180,3,22,11,0,180,181,5,36,0,0,181,21,1,
        0,0,0,182,183,5,32,0,0,183,23,1,0,0,0,184,188,3,26,13,0,185,187,
        5,36,0,0,186,185,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,191,193,3,34,17,0,192,191,
        1,0,0,0,192,193,1,0,0,0,193,197,1,0,0,0,194,196,5,36,0,0,195,194,
        1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,201,
        1,0,0,0,199,197,1,0,0,0,200,202,3,40,20,0,201,200,1,0,0,0,201,202,
        1,0,0,0,202,25,1,0,0,0,203,204,5,9,0,0,204,208,5,36,0,0,205,207,
        3,28,14,0,206,205,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,
        1,0,0,0,209,27,1,0,0,0,210,208,1,0,0,0,211,212,3,30,15,0,212,213,
        5,10,0,0,213,214,3,32,16,0,214,215,5,36,0,0,215,29,1,0,0,0,216,217,
        5,32,0,0,217,31,1,0,0,0,218,219,5,32,0,0,219,33,1,0,0,0,220,221,
        5,11,0,0,221,225,5,36,0,0,222,224,3,36,18,0,223,222,1,0,0,0,224,
        227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,35,1,0,0,0,227,225,
        1,0,0,0,228,229,3,38,19,0,229,230,5,36,0,0,230,37,1,0,0,0,231,232,
        5,32,0,0,232,39,1,0,0,0,233,234,5,12,0,0,234,238,5,36,0,0,235,237,
        3,42,21,0,236,235,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,
        1,0,0,0,239,41,1,0,0,0,240,238,1,0,0,0,241,242,3,44,22,0,242,243,
        5,36,0,0,243,43,1,0,0,0,244,245,5,32,0,0,245,45,1,0,0,0,246,247,
        5,13,0,0,247,251,5,36,0,0,248,250,3,48,24,0,249,248,1,0,0,0,250,
        253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,47,1,0,0,0,253,251,
        1,0,0,0,254,255,5,1,0,0,255,256,3,6,3,0,256,257,5,36,0,0,257,258,
        5,14,0,0,258,259,3,50,25,0,259,260,5,36,0,0,260,261,5,15,0,0,261,
        265,3,52,26,0,262,264,5,36,0,0,263,262,1,0,0,0,264,267,1,0,0,0,265,
        263,1,0,0,0,265,266,1,0,0,0,266,49,1,0,0,0,267,265,1,0,0,0,268,269,
        5,32,0,0,269,51,1,0,0,0,270,271,5,29,0,0,271,53,1,0,0,0,272,273,
        5,16,0,0,273,274,5,36,0,0,274,275,3,56,28,0,275,55,1,0,0,0,276,278,
        3,58,29,0,277,276,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,
        1,0,0,0,280,57,1,0,0,0,281,279,1,0,0,0,282,283,5,32,0,0,283,284,
        5,17,0,0,284,285,5,29,0,0,285,286,5,36,0,0,286,59,1,0,0,0,287,288,
        5,18,0,0,288,294,5,36,0,0,289,290,3,62,31,0,290,291,5,36,0,0,291,
        293,1,0,0,0,292,289,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,
        295,1,0,0,0,295,61,1,0,0,0,296,294,1,0,0,0,297,298,5,19,0,0,298,
        302,5,32,0,0,299,301,5,36,0,0,300,299,1,0,0,0,301,304,1,0,0,0,302,
        300,1,0,0,0,302,303,1,0,0,0,303,305,1,0,0,0,304,302,1,0,0,0,305,
        306,5,20,0,0,306,310,5,32,0,0,307,309,5,36,0,0,308,307,1,0,0,0,309,
        312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,313,1,0,0,0,312,
        310,1,0,0,0,313,314,5,15,0,0,314,318,5,29,0,0,315,317,5,36,0,0,316,
        315,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,
        63,1,0,0,0,320,318,1,0,0,0,321,325,5,21,0,0,322,324,5,36,0,0,323,
        322,1,0,0,0,324,327,1,0,0,0,325,323,1,0,0,0,325,326,1,0,0,0,326,
        328,1,0,0,0,327,325,1,0,0,0,328,334,3,66,33,0,329,330,5,36,0,0,330,
        331,5,36,0,0,331,333,3,66,33,0,332,329,1,0,0,0,333,336,1,0,0,0,334,
        332,1,0,0,0,334,335,1,0,0,0,335,65,1,0,0,0,336,334,1,0,0,0,337,339,
        5,22,0,0,338,340,5,32,0,0,339,338,1,0,0,0,340,341,1,0,0,0,341,339,
        1,0,0,0,341,342,1,0,0,0,342,346,1,0,0,0,343,345,5,36,0,0,344,343,
        1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,349,
        1,0,0,0,348,346,1,0,0,0,349,351,5,23,0,0,350,352,5,32,0,0,351,350,
        1,0,0,0,352,353,1,0,0,0,353,351,1,0,0,0,353,354,1,0,0,0,354,358,
        1,0,0,0,355,357,5,36,0,0,356,355,1,0,0,0,357,360,1,0,0,0,358,356,
        1,0,0,0,358,359,1,0,0,0,359,361,1,0,0,0,360,358,1,0,0,0,361,363,
        5,24,0,0,362,364,5,32,0,0,363,362,1,0,0,0,364,365,1,0,0,0,365,363,
        1,0,0,0,365,366,1,0,0,0,366,370,1,0,0,0,367,369,5,36,0,0,368,367,
        1,0,0,0,369,372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,373,
        1,0,0,0,372,370,1,0,0,0,373,375,5,25,0,0,374,376,5,32,0,0,375,374,
        1,0,0,0,376,377,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,0,378,382,
        1,0,0,0,379,381,5,36,0,0,380,379,1,0,0,0,381,384,1,0,0,0,382,380,
        1,0,0,0,382,383,1,0,0,0,383,385,1,0,0,0,384,382,1,0,0,0,385,386,
        5,26,0,0,386,387,5,36,0,0,387,388,3,68,34,0,388,67,1,0,0,0,389,394,
        3,70,35,0,390,391,5,36,0,0,391,393,3,70,35,0,392,390,1,0,0,0,393,
        396,1,0,0,0,394,392,1,0,0,0,394,395,1,0,0,0,395,69,1,0,0,0,396,394,
        1,0,0,0,397,399,5,32,0,0,398,397,1,0,0,0,399,400,1,0,0,0,400,398,
        1,0,0,0,400,401,1,0,0,0,401,71,1,0,0,0,402,403,5,27,0,0,403,404,
        5,36,0,0,404,410,3,74,37,0,405,406,5,36,0,0,406,407,5,36,0,0,407,
        409,3,74,37,0,408,405,1,0,0,0,409,412,1,0,0,0,410,408,1,0,0,0,410,
        411,1,0,0,0,411,73,1,0,0,0,412,410,1,0,0,0,413,415,5,14,0,0,414,
        416,5,32,0,0,415,414,1,0,0,0,416,417,1,0,0,0,417,415,1,0,0,0,417,
        418,1,0,0,0,418,422,1,0,0,0,419,421,5,36,0,0,420,419,1,0,0,0,421,
        424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,425,1,0,0,0,424,
        422,1,0,0,0,425,427,5,28,0,0,426,428,5,32,0,0,427,426,1,0,0,0,428,
        429,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,434,1,0,0,0,431,
        433,5,36,0,0,432,431,1,0,0,0,433,436,1,0,0,0,434,432,1,0,0,0,434,
        435,1,0,0,0,435,437,1,0,0,0,436,434,1,0,0,0,437,439,5,24,0,0,438,
        440,5,32,0,0,439,438,1,0,0,0,440,441,1,0,0,0,441,439,1,0,0,0,441,
        442,1,0,0,0,442,446,1,0,0,0,443,445,5,36,0,0,444,443,1,0,0,0,445,
        448,1,0,0,0,446,444,1,0,0,0,446,447,1,0,0,0,447,449,1,0,0,0,448,
        446,1,0,0,0,449,451,5,25,0,0,450,452,5,32,0,0,451,450,1,0,0,0,452,
        453,1,0,0,0,453,451,1,0,0,0,453,454,1,0,0,0,454,458,1,0,0,0,455,
        457,5,36,0,0,456,455,1,0,0,0,457,460,1,0,0,0,458,456,1,0,0,0,458,
        459,1,0,0,0,459,75,1,0,0,0,460,458,1,0,0,0,49,83,87,92,96,101,105,
        110,114,119,123,128,132,137,141,188,192,197,201,208,225,238,251,
        265,279,294,302,310,318,325,334,341,346,353,358,365,370,377,382,
        394,400,410,417,422,429,434,441,446,453,458
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
    RULE_personal_info = 2
    RULE_name = 3
    RULE_surname = 4
    RULE_job_title = 5
    RULE_birth = 6
    RULE_phone = 7
    RULE_city = 8
    RULE_gmail = 9
    RULE_summary = 10
    RULE_value = 11
    RULE_skills = 12
    RULE_hard_skills = 13
    RULE_hard_skill = 14
    RULE_hard_skill_name = 15
    RULE_rate = 16
    RULE_soft_skills = 17
    RULE_soft_skill = 18
    RULE_soft_skill_name = 19
    RULE_languages = 20
    RULE_language = 21
    RULE_language_name = 22
    RULE_certificates = 23
    RULE_certificate = 24
    RULE_institution = 25
    RULE_url = 26
    RULE_socials = 27
    RULE_social_list = 28
    RULE_social = 29
    RULE_projects = 30
    RULE_project = 31
    RULE_work_experience = 32
    RULE_job = 33
    RULE_responsibility_list = 34
    RULE_responsibility = 35
    RULE_educations = 36
    RULE_education = 37

    ruleNames =  [ "start", "resume", "personal_info", "name", "surname", 
                   "job_title", "birth", "phone", "city", "gmail", "summary", 
                   "value", "skills", "hard_skills", "hard_skill", "hard_skill_name", 
                   "rate", "soft_skills", "soft_skill", "soft_skill_name", 
                   "languages", "language", "language_name", "certificates", 
                   "certificate", "institution", "url", "socials", "social_list", 
                   "social", "projects", "project", "work_experience", "job", 
                   "responsibility_list", "responsibility", "educations", 
                   "education" ]

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
            self.state = 76
            self.resume()
            self.state = 77
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

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
            self.state = 79
            self.personal_info()
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self.match(ResumeParser.NEWLINE) 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 86
                self.summary()


            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self.match(ResumeParser.NEWLINE) 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 95
                self.skills()


            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.match(ResumeParser.NEWLINE) 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 104
                self.certificates()


            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 107
                    self.match(ResumeParser.NEWLINE) 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 113
                self.socials()


            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 116
                    self.match(ResumeParser.NEWLINE) 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 122
                self.projects()


            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 125
                    self.match(ResumeParser.NEWLINE) 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 131
                self.work_experience()


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 134
                self.match(ResumeParser.NEWLINE)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 140
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
        self.enterRule(localctx, 4, self.RULE_personal_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ResumeParser.T__0)
            self.state = 144
            self.name()
            self.state = 145
            self.match(ResumeParser.NEWLINE)
            self.state = 146
            self.match(ResumeParser.T__1)
            self.state = 147
            self.surname()
            self.state = 148
            self.match(ResumeParser.NEWLINE)
            self.state = 149
            self.match(ResumeParser.T__2)
            self.state = 150
            self.job_title()
            self.state = 151
            self.match(ResumeParser.NEWLINE)
            self.state = 152
            self.match(ResumeParser.T__3)
            self.state = 153
            self.phone()
            self.state = 154
            self.match(ResumeParser.NEWLINE)
            self.state = 155
            self.match(ResumeParser.T__4)
            self.state = 156
            self.city()
            self.state = 157
            self.match(ResumeParser.NEWLINE)
            self.state = 158
            self.match(ResumeParser.T__5)
            self.state = 159
            self.gmail()
            self.state = 160
            self.match(ResumeParser.NEWLINE)
            self.state = 161
            self.match(ResumeParser.T__6)
            self.state = 162
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
            self.state = 164
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
            self.state = 166
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
            self.state = 168
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
            self.state = 170
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
            self.state = 172
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
            self.state = 174
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
            self.state = 176
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
        self.enterRule(localctx, 20, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ResumeParser.T__7)
            self.state = 179
            self.value()
            self.state = 180
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
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
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
        self.enterRule(localctx, 24, self.RULE_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.hard_skills()
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    self.match(ResumeParser.NEWLINE) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 191
                self.soft_skills()


            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 194
                    self.match(ResumeParser.NEWLINE) 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 200
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
        self.enterRule(localctx, 26, self.RULE_hard_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ResumeParser.T__8)
            self.state = 204
            self.match(ResumeParser.NEWLINE)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 205
                self.hard_skill()
                self.state = 210
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
        self.enterRule(localctx, 28, self.RULE_hard_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.hard_skill_name()
            self.state = 212
            self.match(ResumeParser.T__9)
            self.state = 213
            self.rate()
            self.state = 214
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
        self.enterRule(localctx, 30, self.RULE_hard_skill_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
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
        self.enterRule(localctx, 32, self.RULE_rate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
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
        self.enterRule(localctx, 34, self.RULE_soft_skills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(ResumeParser.T__10)
            self.state = 221
            self.match(ResumeParser.NEWLINE)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 222
                self.soft_skill()
                self.state = 227
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
        self.enterRule(localctx, 36, self.RULE_soft_skill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.soft_skill_name()
            self.state = 229
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
        self.enterRule(localctx, 38, self.RULE_soft_skill_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
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
        self.enterRule(localctx, 40, self.RULE_languages)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ResumeParser.T__11)
            self.state = 234
            self.match(ResumeParser.NEWLINE)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 235
                self.language()
                self.state = 240
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
        self.enterRule(localctx, 42, self.RULE_language)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.language_name()
            self.state = 242
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
        self.enterRule(localctx, 44, self.RULE_language_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
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

        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

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
        self.enterRule(localctx, 46, self.RULE_certificates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ResumeParser.T__12)
            self.state = 247
            self.match(ResumeParser.NEWLINE)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 248
                self.certificate()
                self.state = 253
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


        def url(self):
            return self.getTypedRuleContext(ResumeParser.UrlContext,0)


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
        self.enterRule(localctx, 48, self.RULE_certificate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(ResumeParser.T__0)
            self.state = 255
            self.name()
            self.state = 256
            self.match(ResumeParser.NEWLINE)
            self.state = 257
            self.match(ResumeParser.T__13)
            self.state = 258
            self.institution()
            self.state = 259
            self.match(ResumeParser.NEWLINE)
            self.state = 260
            self.match(ResumeParser.T__14)
            self.state = 261
            self.url()
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 262
                    self.match(ResumeParser.NEWLINE) 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_institution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ResumeParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

        def getRuleIndex(self):
            return ResumeParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = ResumeParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ResumeParser.URL)
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
        self.enterRule(localctx, 54, self.RULE_socials)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ResumeParser.T__15)
            self.state = 273
            self.match(ResumeParser.NEWLINE)
            self.state = 274
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
        self.enterRule(localctx, 56, self.RULE_social_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 276
                self.social()
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


    class SocialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ResumeParser.TEXT, 0)

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

        def NEWLINE(self):
            return self.getToken(ResumeParser.NEWLINE, 0)

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
        self.enterRule(localctx, 58, self.RULE_social)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ResumeParser.TEXT)
            self.state = 283
            self.match(ResumeParser.T__16)
            self.state = 284
            self.match(ResumeParser.URL)
            self.state = 285
            self.match(ResumeParser.NEWLINE)
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
        self.enterRule(localctx, 60, self.RULE_projects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ResumeParser.T__17)
            self.state = 288
            self.match(ResumeParser.NEWLINE)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 289
                self.project()
                self.state = 290
                self.match(ResumeParser.NEWLINE)
                self.state = 296
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

        def URL(self):
            return self.getToken(ResumeParser.URL, 0)

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
        self.enterRule(localctx, 62, self.RULE_project)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ResumeParser.T__18)
            self.state = 298
            self.match(ResumeParser.TEXT)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 299
                self.match(ResumeParser.NEWLINE)
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 305
            self.match(ResumeParser.T__19)
            self.state = 306
            self.match(ResumeParser.TEXT)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 307
                self.match(ResumeParser.NEWLINE)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 313
            self.match(ResumeParser.T__14)
            self.state = 314
            self.match(ResumeParser.URL)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 315
                    self.match(ResumeParser.NEWLINE) 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_work_experience)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(ResumeParser.T__20)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 322
                self.match(ResumeParser.NEWLINE)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 328
            self.job()
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 329
                    self.match(ResumeParser.NEWLINE)
                    self.state = 330
                    self.match(ResumeParser.NEWLINE)
                    self.state = 331
                    self.job() 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.NEWLINE)
            else:
                return self.getToken(ResumeParser.NEWLINE, i)

        def responsibility_list(self):
            return self.getTypedRuleContext(ResumeParser.Responsibility_listContext,0)


        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ResumeParser.TEXT)
            else:
                return self.getToken(ResumeParser.TEXT, i)

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
        self.enterRule(localctx, 66, self.RULE_job)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(ResumeParser.T__21)
            self.state = 339 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 338
                self.match(ResumeParser.TEXT)
                self.state = 341 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 343
                self.match(ResumeParser.NEWLINE)
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349
            self.match(ResumeParser.T__22)
            self.state = 351 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 350
                self.match(ResumeParser.TEXT)
                self.state = 353 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 355
                self.match(ResumeParser.NEWLINE)
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 361
            self.match(ResumeParser.T__23)
            self.state = 363 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 362
                self.match(ResumeParser.TEXT)
                self.state = 365 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 367
                self.match(ResumeParser.NEWLINE)
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 373
            self.match(ResumeParser.T__24)
            self.state = 375 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 374
                self.match(ResumeParser.TEXT)
                self.state = 377 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 379
                self.match(ResumeParser.NEWLINE)
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 385
            self.match(ResumeParser.T__25)
            self.state = 386
            self.match(ResumeParser.NEWLINE)
            self.state = 387
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
        self.enterRule(localctx, 68, self.RULE_responsibility_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.responsibility()
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 390
                    self.match(ResumeParser.NEWLINE)
                    self.state = 391
                    self.responsibility() 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_responsibility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 397
                self.match(ResumeParser.TEXT)
                self.state = 400 
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
        self.enterRule(localctx, 72, self.RULE_educations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(ResumeParser.T__26)
            self.state = 403
            self.match(ResumeParser.NEWLINE)
            self.state = 404
            self.education()
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 405
                self.match(ResumeParser.NEWLINE)
                self.state = 406
                self.match(ResumeParser.NEWLINE)
                self.state = 407
                self.education()
                self.state = 412
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
        self.enterRule(localctx, 74, self.RULE_education)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(ResumeParser.T__13)
            self.state = 415 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 414
                self.match(ResumeParser.TEXT)
                self.state = 417 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 419
                self.match(ResumeParser.NEWLINE)
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 425
            self.match(ResumeParser.T__27)
            self.state = 427 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 426
                self.match(ResumeParser.TEXT)
                self.state = 429 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 431
                self.match(ResumeParser.NEWLINE)
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 437
            self.match(ResumeParser.T__23)
            self.state = 439 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 438
                self.match(ResumeParser.TEXT)
                self.state = 441 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 443
                self.match(ResumeParser.NEWLINE)
                self.state = 448
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 449
            self.match(ResumeParser.T__24)
            self.state = 451 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 450
                self.match(ResumeParser.TEXT)
                self.state = 453 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 455
                    self.match(ResumeParser.NEWLINE) 
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





