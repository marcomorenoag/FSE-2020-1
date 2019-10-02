	.text
	.global _start

_start:
	mov	r7,#4
	mov	r0,#1
	ldr	r1,=message
	mov 	r2,#18
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0
       .data

message:
       .ascii "FSE2020-1 is cool\n"
