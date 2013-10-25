#
# Makefile: a simple template for Hello, world! programs
#

CXX=g++

TARGET=hello.exe
SOURCES=hello.cpp
HEADERS=hello.h

OBJECTS=$(SOURCES:.cpp=.o)
DEPENDS=$(SOURCES:.cpp=.d)

INCLUDES+=
LIBRARIES+=

.PHONY: all clean clean_all

all: $(TARGET)

clean:
	$(RM) $(RMFLAGS) $(OBJECTS) $(DEPENDS)

clean_all: clean
	$(RM) $(RMFLAGS) $(TARGET)

.SUFFIXES:
.SUFFIXES: .c .cpp .o

.cpp.o:
	$(CXX) -c $(CXXFLAGS) -o $@ $<

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJECTS) $(LDFLAGS) $(LIBRARIES)

-include $(DEPENDS)

# EOF