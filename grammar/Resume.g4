grammar Resume;

start: resume EOF;

resume: base_info NEWLINE* additional_info;

base_info: personal_info NEWLINE* socials? NEWLINE* certificates?;

additional_info: summary? NEWLINE* skills? NEWLINE* projects? NEWLINE* work_experience? NEWLINE* educations?;

personal_info: 'name:' name NEWLINE 'surname:' surname NEWLINE 'job_title:' job_title NEWLINE 'phone:' phone NEWLINE 'city:' city NEWLINE 'gmail:' gmail NEWLINE 'birth:' birth;

name: TEXT;
surname: TEXT;
job_title: TEXT;
birth: TEXT;
phone: PHONE;
city: TEXT;
gmail: EMAIL;

summary: 'summary:' value NEWLINE;

value: TEXT;

skills: hard_skills NEWLINE* soft_skills? NEWLINE* languages?;
hard_skills: 'hard_skills:' NEWLINE (hard_skill)*;
hard_skill: hard_skill_name ',' rate NEWLINE;
hard_skill_name: TEXT;
rate: TEXT;

soft_skills: 'soft_skills:' NEWLINE (soft_skill)*;
soft_skill : soft_skill_name NEWLINE;
soft_skill_name: TEXT;

languages: 'languages:' NEWLINE (language)*;
language: language_name NEWLINE;
language_name : TEXT;

certificates: 'certificates:' NEWLINE* (certificate)*;
certificate: 'name:' name NEWLINE 'institution:' institution NEWLINE 'link:' link NEWLINE*;
link: URL;
institution: TEXT;


socials: 'socials:' NEWLINE* social_list;
social_list: (name ':' link NEWLINE)*;


projects: 'projects:' NEWLINE (project NEWLINE)*;
project: 'title:' project_title NEWLINE* 'description:' project_description NEWLINE* 'link:' project_url NEWLINE*;

project_title: TEXT;
project_description: TEXT;
project_url: URL;

work_experience: 'work_experience:' NEWLINE* job (NEWLINE NEWLINE job)*;
job: 'company:' text_name NEWLINE* 'position:' text_name NEWLINE* 'start_date:' date NEWLINE* 'end_date:' date NEWLINE*  'responsibilities:' NEWLINE responsibility_list;
responsibility_list: responsibility (NEWLINE responsibility)*;
responsibility: TEXT+;

text_name: TEXT+;

educations: 'educations:' NEWLINE education (NEWLINE NEWLINE education)*;
education: 'institution:' institution NEWLINE* 'degree:' degree NEWLINE* 'start_date:' date NEWLINE* 'end_date:' date NEWLINE*;


degree: TEXT+;
date: TEXT+;

URL: ' '* 'http' 's'? '://' [a-zA-Z0-9./?=&_-]+;
EMAIL: ' '* [a-zA-Z0-9_.+-]+ '@' [a-zA-Z0-9-]+ '.' [a-zA-Z0-9-.]+;
PHONE: ' '* '+98' [0-9]+;
TEXT : [a-zA-Z0-9_./\- ]+ ;
INTEGER: '0' | [1-9]+ [0-9]*;
//ID: LETTER (LETTER | DIGIT)*;
//fragment DIGIT: [0-9];
//fragment LETTER: [a-zA-Z];

//DATE: [0-9]{4} '-' [0-9]{2} '-' [0-9]{2};


//URL: 'http' 's'? '://' [a-zA-Z0-9./?=&_-]+;
RATING: [1-5];

WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r');
