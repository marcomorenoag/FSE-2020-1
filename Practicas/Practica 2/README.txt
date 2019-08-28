
MANEJANDO CADENAS

El código busca imprimir la cadena Hola Mundo por consola auxiliándose de la activación de registros que cuentan con funciones especiales, en este caso la función a formatear es printf.

	.text
	.global _start

_start:
	@ Los registro r7, r0 y r2 llaman a la funcion printf, especificamente deben tener estos vcalores para que funcionen menos r2 el cual es variable dependiendo de la longitud de la cadena
	mov	r7,#4
	mov	r0,#1
	@Mueve dentro del registro r1  la direccion de la primera letra H del mensaje Hola Mundo
	ldr	r1,=message
	mov 	r2,#14
	@svc perimite llamar a la funcion printf despues de modificar los parametros
	svc	#0
	mov	r7,#1
	mov	r0,#0
	svc	#0
    .data

message:
	@Define a message como la cadena Hola Mundo
      .ascii "Hola mundo\n"


PREGUNTAS

(a) ¿Cuál es la diferencia entre las instrucciones swi 0x0, svc #0 y bx lr?



(b) A que se refiere la instrucción .balign 4 en el lenguaje ensamblador para ARM?

Esta instrucción debe contar con un parámetro múltiplo de 2, permite alinear la instrucción o dato inmediatamente después de la directiva en una dirección de memoria que es múltiplo del parámetro, en este caso múltiplo de 4, el propósito es que algunas instrucciones tienen una ejecución más rápida si se alinean en un límite de 4 bytes o 32 bits

(c) Cuántas instrucciones en lenguaje ensamblador hay para la arquitectura ARM11 y cuantos modos de direccionamiento hay (nombrelos)?

Alrededor de 110 instrucciones según el manual de referencia

Tiene 3 modos:

Inmediato, Registro y Registro Escalado