#
# Makefile - a minimalistic make file for compiling a gtk+ 3.0 program
#

CC=gcc
CFLAGS := $(shell pkg-config --cflags gtk+-3.0)
LIBS := $(shell pkg-config --libs gtk+-3.0)

PROGRAM=hello
SOURCES=hello.c
OBJECTS=$(SOURCES:.c=.o)


all : $(PROGRAM)

clean :
	-$(RM) $(RMFLAGS) $(OBJECTS)

distclean : clean
	-$(RM) $(RMFLAGS) $(PROGRAM)

$(PROGRAM) : $(OBJECTS)
	$(CC) $(LDFLAGS) -o $(PROGRAM) $(OBJECTS) $(LIBS)

hello.o : hello.c

# EOF
