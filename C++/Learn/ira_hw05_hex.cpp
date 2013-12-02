//
// ira_hw05_mst.cpp: Homework #5 from "C++ for C programmers".
//

#include "hex.hpp"
#include "graph.hpp"

#include <iostream>

using namespace std;
//using namespace hex;

const size_t DEFAULT_BOARD_SIZE = 11;

/**
 * This is the program's entry-point.
 */
int
main () {
    game game(DEFAULT_BOARD_SIZE);
    game.play();
}
