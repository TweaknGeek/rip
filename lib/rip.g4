grammar rip;

// Parser rules
program: statement* EOF;

statement
    : assignment
    | expression
    | printStmt
    ;

assignment: ID '=' expression;

expression
    : expression ('+'|'-') expression
    | expression ('*'|'/') expression
    | '(' expression ')'
    | ID
    | NUMBER
    ;

printStmt: 'print' '(' expression ')';

// Lexer rules
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;

