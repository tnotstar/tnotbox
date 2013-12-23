//
// ira_hw05_mst.cpp: Homework #5 from "C++ for C programmers".
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
#if 0
    game game(DEFAULT_BOARD_SIZE);
    game.play();
#endif // 0
    graph::sparse_graph<int, double, double> g;

    cout << "Adding the node #0: " << g.add_node(0, 1.0) << endl;

    cout << "Current number of nodes: " << g.nodes() << endl;
    cout << "Current number of edges: " << g.edges() << endl;
    cout << "Edges at node #0: " << g.edges_at(0) << endl;

    for (int i = 1; i < 1000; i++) {
        if (!g.add_node(i, static_cast<double>(i))) {
            cout << "Oops! something is wrong!" << endl;
            break;
        }
    }
    cout << "Total nodes inserted: " << g.nodes() << endl;

    return 0;
}
