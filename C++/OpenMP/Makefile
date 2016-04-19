#
# Makefile - a make file to build OpenMP's source code examples
#

.DEFAULT: all

NTHREADS=3

CC=gcc
CFLAGS=-fopenmp
CXXFLAGS=

LD=gcc
LDFLAGS=
LLIBS=-lstdc++ -lomp


all: test

hello: hello.o
	@$(LD) $(LDFLAGS) -o $@ $< $(LLIBS)

hello.o: hello.cxx
	@$(CC) $(CFLAGS) $(CXXFLAGS) -c $<

clean:
	-@$(RM) $(RMFLAGS) hello.o

distclean: clean
	-@$(RM) $(RMFLAGS) hello

test: hello
	OMP_NUM_THREADS=$(NTHREADS) ./hello

# EOF
