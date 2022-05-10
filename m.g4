grammar m;

main: (segment ';')+                            #MainExp;
    

assignVariable 
    : type=typeSpecifier name=WORD '=' value=expr     #AssignExpr
    | name=WORD '=' value=expr                        #AssignVar
    ; 

segment
    : assignVariable                           #SegAssign
    | defineVariable                           #SegDefine
    ;

expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr           
    | atom=INT                                 # NumberExpr
    | '(' expr ')'                             # ParenExpr
    ;

defineVariable: type=typeSpecifier name=WORD             #DefineVar;

typeSpecifier
    : 'int'                                    
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