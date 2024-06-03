grammar Resume;

resume: section+;

section: 'section' ID '{' (entry|text)* '}';

entry: ID ':' STRING;

text: STRING;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' ~["]* '"';
WS: [ \t\r\n]+ -> skip;
