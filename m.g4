grammar m;

main: (functions)+                            #MainExp;
    

assignVariable 
    : type=typeSpecifier name=WORD '=' value=expr     #AssignExpr
    | name=WORD '=' value=expr                        #AssignVar
    | name=WORD '=' functionCall                      #AssignFunction
    ; 

functions
    : functionDefinition
    ;

operation: opera ';';

opera
    : assignVariable                           
    | defineVariable                           
    | returnStatement                          
    | functionCall
    | selectionStatement
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

statement
    : compoundStatement
    | selectionStatement
    ;

condition
    : expr ('=='| '!=' | '<'|'>'|'<='|'>=') expr
    ;

selectionStatement
    :   'if' '(' condition ')' statement ('else' statement)?
    |   'switch' '(' condition ')' statement
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
    :   typeSpecifier name=WORD '(' paramList? ')' statement
    ;

functionCall
    : name=WORD '(' callParamList? ')'
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
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