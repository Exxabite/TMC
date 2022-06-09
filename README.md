# TMC
The M Compiler, a compiler for the M language. 

[![CodeFactor](https://www.codefactor.io/repository/github/exxabite/tmc/badge)](https://www.codefactor.io/repository/github/exxabite/tmc)

Temporary documentation.


Strucure:

	{
	function:
		[operaton],
	}
	

	
operations:

	0 mov	var, var
		var, imm
		
	1 add	var, var
		var, imm
		
	2 sub	var, var
		var, imm
		
	3 mul	var, var
		var, imm
		
	4 div	var, var
		var, imm
		
	5 push	var
	
	6 pop	var
	
	7 call	function
	
operation strucure:

	[0 ["foo", "bar"]]
