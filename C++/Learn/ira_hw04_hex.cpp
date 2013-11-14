//
// ira_hw03_mst.cpp: Homework #4 from "C++ for C programmers".
//

#include "dense_graph.hpp"

#include <iostream>

using namespace std;

const size_t DEFAULT_GRAPH_SIZE = 1000000;

/**
 * This is the program's entry-point.
 */
int
main () {

    dense_graph<double> g(DEFAULT_GRAPH_SIZE);

    g.add_edge(0, 1, 1.2);
    g.add_edge(0, 3, 1.2);
    g.add_edge(0, 4, 1.2);
    g.add_edge(2, 3, 1.2);
    g.add_edge(3, 4, 1.2);

    return 0;
}

