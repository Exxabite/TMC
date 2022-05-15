grammar m;

main: (functions)+                            #MainExp;
    

assignVariable 
    : type=typeSpecifier name=WORD '=' value=expr     #AssignExpr
    | name=WORD '=' value=expr                        #AssignVar
    ; 

functions
    : functionDefinition
    ;

operation: opera ';';

opera
    : assignVariable                           #SegAssign
    | defineVariable                           #SegDefine
    | returnStatement                          #retStatement
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

returnStatement: 'return' name=WORD;

paramList
    :   param (',' param)*
    ;

functionDefinition
    :   typeSpecifier name=WORD '(' paramList? ')' compoundStatement
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