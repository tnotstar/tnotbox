#

CC=gcc
CFLAGS=-DCHM_MT

LD=gcc
LDFLAGS=-lpthread -lchm

%.o: %.c
	${CC} -c -o $@ $^ ${CFLAGS}


all: testme1

testme1: testme1.o
	${LD} -o $@ $^ ${LDFLAGS}

testme.o: testme1.c

# EOF
