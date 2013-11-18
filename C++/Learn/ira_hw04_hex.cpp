//
// ira_hw03_mst.cpp: Homework #4 from "C++ for C programmers".
//

#include "hex.hpp"

#include <iostream>

using namespace std;
using namespace hex;

const size_t DEFAULT_BOARD_SIZE = 11;

/**
 * This is the program's entry-point.
 */
int
main () {

    game game(DEFAULT_BOARD_SIZE);
    game.play();

    return 0;
}
