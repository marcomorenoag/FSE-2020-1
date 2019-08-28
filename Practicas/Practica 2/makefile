LD = ld 
AS = as
ASFLAGS_THUMB = -mthumb-interwork
LDFLAGS_THUMB = --thumb-entry=_start

CC = gcc
CFLAGS = -O2 -Wall
LFLAGS =


all:	compare


compare:	compare.o
	$(LD) $(LDFLAGS) -o compare compare.o

compare.o:	compare.s
	$(AS) $(ASFLAGS) -o compare.o compare.s


submit:	compare.s Makefile README
	tar -czvf P3_FSEsubmit.tar.gz compare.s Makefile README

clean:
	rm -f *~ *.o compare
