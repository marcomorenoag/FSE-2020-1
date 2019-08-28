
.text
	.global _start

_start:
	@ Los registro r7, r0 y r2 llaman a la funcion printf, especificamente deben tener estos vcalores para que funcionen menos r2 el cual es variable dependiendo de la longitud de la cadena
	mov	r7,#4
	mov	r0,#1
	@Mueve dentro del registro r1  la direccion de la primera letra del mensaje
	ldr	r1,=message
	mov 	r2,#17
	@svc perimite llamar a la funcion printf despues de modificar los parametros
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0
    .data

message:
	@Define a message como la cadena 
      .ascii "FSE2020-1 is cool"