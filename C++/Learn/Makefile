#
# Makefile: basic definitions to use GCC 4.8 with C++11
#

#CXX := g++-4.8
CXX := g++
CXXFLAGS += -std=c++11

ira_hw04_hex: ira_hw04_hex.o hex.hpp graph.hpp
	$(CXX) $(CXXFLAGS) -o ira_hw04_hex $<

ira_hw04_hex.o: ira_hw04_hex.cpp hex.hpp graph.hpp

ira_hw05_hex: ira_hw05_hex.o hex.hpp graph.hpp
	$(CXX) $(CXXFLAGS) -o ira_hw05_hex $<

ira_hw05_hex.o: ira_hw05_hex.cpp hex.hpp graph.hpp

# EOF
