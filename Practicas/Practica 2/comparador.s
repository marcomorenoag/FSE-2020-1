	.text
	.global _start

.text
	.global _start

_start:

	mov r3, #4
	mov r4, #5
	cmp r4, r3
  	beq igual

       .data

mayor:
	mov	r7,#4
	mov	r0,#1
	ldr	r1,=message_mayor
	mov 	r2,#25
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0
menor:
	mov	r7,#4
	mov	r0,#1
	ldr	r1,=message_menor
	mov 	r2,#25
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0
igual:
	mov	r7,#4
	mov	r0,#1
	ldr	r1,=message_mayor
	mov 	r2,#23
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0
message_mayor:
      .ascii "El primer numero es mayor"
message_menor:
	.ascii "El segundo numero es mayor"

message_igual:
	.ascii "Los numeros son iguales"