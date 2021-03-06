grammar m;

main: (functions)+                            #MainExp;
    

assignVariable 
    : type=typeSpecifier name=WORD '=' value=expr     #AssignExpr
    | name=WORD '=' value=expr                        #AssignVar
    | name=WORD '=' functionCall                      #AssignFunction
    ; 

functions
    : functionDefinition
    | macroDefinition
    | include
    ;

operation: opera ';'?;

opera
    : assignVariable                           
    | defineVariable                           
    | returnStatement                          
    | functionCall
    | macroCall
    ;

expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr           
    | atom=INT                                 # NumberExpr
    | '(' expr ')'                             # ParenExpr
    | atom=WORD                                # VariableExpr
    ;

defineVariable: type=typeSpecifier name=WORD             #DefineVar;

typeSpecifier
    : 'int'                                    
    ;

compoundStatement
    :   '{' operation* '}'
    ;

param: type=typeSpecifier name=WORD;

returnStatement: 'return' value=expr;

paramList
    :   param (',' param)*
    ;

callParam
    : name=WORD
    | INT;

callParamList
    : callParam (',' callParam)*
    ;

functionDefinition
    :   typeSpecifier name=WORD '(' paramList? ')' compoundStatement
    ;

functionCall
    : name=WORD '(' callParamList? ')'
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;

//Preprocessor

macroDefinition
    :   'macro' name=WORD '(' macroParamList? ')' Codeblock
    ;

Codeblock: '[!' .*? '!]';

include: '#include' STRING;

macroParamList
    :   macroParam (',' macroParam)*
    ;

macroParam: name=WORD;

macroCall
    : '!' name=WORD '(' macroCallParamList? ')'
    ;

macroCallParam
    : name=WORD
    | STRING
    | INT
    ;

macroCallParamList
    : macroCallParam (',' macroCallParam)*
    ;

INT  : [0-9]+         ;
STRING : '"' .*? '"'  ;
WS   : [ \t]+ -> skip ;
Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;
WORD: [a-zA-Z_]+   ;