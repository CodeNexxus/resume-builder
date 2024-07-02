grammar Resume;

start: resume EOF;

resume: optional_features NEWLINE* base_info NEWLINE* additional_info;

optional_features:
    go_top? NEWLINE*
    autocopy? NEWLINE*
    job_title_effect? NEWLINE*
    interactive_skill_bars? NEWLINE*
    collapsable_sections? NEWLINE*
    dynamic_theme? NEWLINE*
    switching? NEWLINE*
    tooltip? NEWLINE*
    pdf_output?;

go_top: 'go_top:' boolean;
autocopy: 'autocopy:' boolean;
job_title_effect: 'job_title_effect:' boolean;
interactive_skill_bars: 'interactive_skill_bars:' boolean;
collapsable_sections: 'collapsable_sections:' boolean;
dynamic_theme: 'dynamic_theme:' boolean;
switching: 'switching:' boolean;
tooltip: 'tooltip:' boolean;
pdf_output: 'pdf_output:' boolean;

boolean: BOOLEAN;

base_info: personal_info NEWLINE* socials? NEWLINE* certificates? NEWLINE* git_scraper?;

additional_info: summary? NEWLINE* skills? NEWLINE* projects? NEWLINE* work_experience? NEWLINE* educations?;

git_scraper: 'git-username:' name;

personal_info: 'name:' name NEWLINE 'surname:' surname NEWLINE 'job_title:' job_title NEWLINE 'phone:' phone NEWLINE 'city:' city NEWLINE 'gmail:' gmail NEWLINE 'birth:' birth;

name: TEXT;
surname: TEXT;
job_title: TEXT;
birth: TEXT;
phone: PHONE;
city: TEXT;
gmail: EMAIL;

summary: 'summary:' (value NEWLINE)*;

value: TEXT;

skills: jobinja_scraper NEWLINE* hard_skills NEWLINE* soft_skills? NEWLINE* languages?;
jobinja_scraper: 'jobinja:' link;

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

socials: 'socials:' NEWLINE* (social NEWLINE)+;
social: social_name ':' link;
social_name: TEXT;

projects: 'projects:' NEWLINE (project NEWLINE)*;
project: 'title:' project_title NEWLINE* 'description:' project_description NEWLINE* 'link:' project_url NEWLINE*;

project_title: TEXT;
project_description: TEXT;
project_url: URL;

work_experience: 'work_experience:' NEWLINE* job (NEWLINE NEWLINE job)*;
job: 'company:' company NEWLINE* 'position:' position NEWLINE* 'start_date:' start_date NEWLINE* 'end_date:' end_date NEWLINE*  'responsibilities:' NEWLINE responsibility_list;
responsibility_list: responsibility (NEWLINE responsibility)*;
responsibility: TEXT+;

company: TEXT;
position: TEXT;

educations: 'educations:' NEWLINE education (NEWLINE NEWLINE education)*;
education: 'institution:' institution NEWLINE* 'degree:' degree NEWLINE* 'start_date:' start_date NEWLINE* 'end_date:' end_date NEWLINE*;

degree: TEXT;
start_date: TEXT;
end_date: TEXT;

URL: ' '* 'http' 's'? '://' [a-zA-Z0-9./?=&_%-]+;
EMAIL: ' '* [a-zA-Z0-9_.+-]+ '@' [a-zA-Z0-9-]+ '.' [a-zA-Z0-9-.]+;
PHONE: ' '* '+98' [0-9]+;
TEXT : [a-zA-Z0-9_./\- ]+ ;
INTEGER: '0' | [1-9]+ [0-9]*;
//ID: LETTER (LETTER | DIGIT)*;
//fragment DIGIT: [0-9];
//fragment LETTER: [a-zA-Z];

//DATE: [0-9]{4} '-' [0-9]{2} '-' [0-9]{2};
BOOLEAN: 'True' | 'False';

//URL: 'http' 's'? '://' [a-zA-Z0-9./?=&_-]+;
RATING: [1-5];

WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r');
