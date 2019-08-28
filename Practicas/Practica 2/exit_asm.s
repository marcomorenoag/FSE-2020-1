
@ Syscall defines
.equ SYSCALL_EXIT,     1

        .global _start
_start:
        @Da un salto ahacia la etiqueta exit
        b exit

exit:

	@Mueve el numero 42 hacia el registro r0
	mov r0,#42

        @Similar a escribir return 0 en C
	mov r7,#SYSCALL_EXIT
	swi 0x0
