//
// ira_hw03_mst.cpp: Homework #4 from "C++ for C programmers".
//

//#include "hex.hpp"

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

    //game game(DEFAULT_BOARD_SIZE);
    //game.play();

    graph::sparse_graph<int, double, int> g(10);

    g.add_node(0, 1.0);
    g.add_node(1, 2.0);
    g.add_edge(0, 1, 10);

    cout << "Number of nodes: " << g.nodes() << endl;
    cout << "Number of edges: " << g.edges() << endl;
    cout << "Edges at 0: " << g.edges_at(0) << endl;
    cout << "Value at 0: " << g.value_at(0) << endl;
    cout << "Edges at 1: " << g.edges_at(1) << endl;
    cout << "Value at 1: " << g.value_at(1) << endl;
    cout << "Cost from 0 to 1: " << g.cost_at(0, 1) << endl;

    return 0;
}
