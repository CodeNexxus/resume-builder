grammar Resume;

start: resume EOF;

resume: personal_info summary? skills? certificates? socials? projects? work_experience? educations?;

personal_info: 'name:' name 'surname:' surname 'job_title:' job_title 'phone: ' phone 'city:' city 'gmail:' gmail 'birth:' birth;

name: TEXT;
surname: TEXT;
job_title: TEXT;
birth: TEXT;
phone: PHONE;
city: TEXT;
gmail: EMAIL;

summary: 'summary:' TEXT;

skills: hard_skills soft_skills? languages?;
hard_skills: 'hard_skills:' hard_skill_list;
hard_skill_list: hard_skill*;
hard_skill: TEXT ',' TEXT;

soft_skills: 'soft_skills:' soft_skill_list;
soft_skill_list: soft_skill*;
soft_skill: TEXT;

languages: 'languages:' language_list;
language_list: language*;
language: TEXT;

certificates: 'certificates:' certificate_list;
certificate_list: certificate*;
certificate: 'name:' TEXT 'institution:' TEXT 'link:' URL;

socials: 'socials:' NEWLINE social_list;
social_list: social (NEWLINE social)*;
social: TEXT ':' URL;

projects: 'projects:' NEWLINE project (NEWLINE NEWLINE project)*;
project: 'title:' TEXT NEWLINE 'description:' TEXT NEWLINE 'link:' URL NEWLINE;

work_experience: 'work_experience:' NEWLINE job (NEWLINE NEWLINE job)*;
job: 'company:' TEXT NEWLINE 'position:' TEXT NEWLINE 'start_date:' TEXT NEWLINE 'end_date:' TEXT NEWLINE 'responsibilities:' NEWLINE responsibility_list;
responsibility_list: responsibility (NEWLINE responsibility)*;
responsibility: TEXT;

educations: 'educations:' NEWLINE education (NEWLINE NEWLINE education)*;
education: 'institution:' TEXT NEWLINE 'degree:' TEXT NEWLINE 'start_date:' TEXT NEWLINE 'end_date:' TEXT NEWLINE;

TEXT: [a-zA-Z0-9_./\- ]+;
//ID: LETTER (LETTER | DIGIT)*;
//fragment DIGIT: [0-9];
//fragment LETTER: [a-zA-Z];

//DATE: [0-9]{4} '-' [0-9]{2} '-' [0-9]{2};
PHONE: ' '* '+98' [0-9]+;
EMAIL: ' '* [a-zA-Z0-9_.+-]+ '@' [a-zA-Z0-9-]+ '.' [a-zA-Z0-9-.]+;
URL: 'http' 's'? '://' [a-zA-Z0-9./?=&_-]+;
RATING: [1-5];
//INTEGER: '0' | [1-9]+ [0-9]*;

WS: [ \t]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;
