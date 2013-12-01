#
# Makefile: basic definitions to use GCC 4.8 with C++11
#

CXX := g++-4.8
CXXFLAGS += -std=c++11

ira_hw04_hex: ira_hw04_hex.o hex.hpp graph.hpp
	$(CXX) $(CXXFLAGS) -o ira_hw04_hex $<

ira_hw04_hex.o: ira_hw04_hex.cpp hex.hpp graph.hpp

# EOF
