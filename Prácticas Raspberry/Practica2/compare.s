@ Syscall defines
.equ SYSCALL_EXIT,     1

.text
	.global _start

_start:
	@Mueve al registro el valor de las constantes
	mov r4, #5
	mov r3, #5
	@Compara los registros
	cmp r4, r3
	@Si son iguales salta a la etiqueta igual si no sigue
  	beq igual
	@Realiza resta
	subs r5, r4, r3
	@Si el resultado de la resta es negativo
  	blt menor
	@Si es positivo
	bgt mayor

	@Similar a escribir return 0 en C
	mov r7,#SYSCALL_EXIT
	swi 0x0

@Imprime la cadena para numero mayor
mayor:
	mov	r7,#4
	mov	r0,#1
	ldr	r1,=message_mayor
	mov 	r2,#27
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0

@Imprime la cadena para numero menor
menor:
	mov	r7,#4
	mov	r0,#1
	ldr	r1,=message_menor
	mov 	r2,#27
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0

@Imprime la cadena para numeros iguales
igual:
	mov	r7,#4
	mov	r0,#1
	ldr	r1,=message_igual
	mov 	r2,#24
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0

@Establece valor de las constantes
message_mayor:
      .ascii "El Primer numero es mayor\n"

message_menor:
	.ascii "El segundo numero es mayor\n"

message_igual:
	.ascii "Los numeros son iguales\n"
