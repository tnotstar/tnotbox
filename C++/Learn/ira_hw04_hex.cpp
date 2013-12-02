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

    graph::sparse_graph<int, double, double> g(20);

#if 0
    cout << "Adding: " << g.add_node(0, 1.5) << endl;
    cout << "Adding: " << g.add_node(1, 2.5) << endl;
    cout << "Adding: " << g.add_edge(0, 1, 10.5) << endl;
#endif

    if (g.load_from_file("ira_hw04_mst.dat"))
        cout << "Data loaded!" << endl;
    else
        cout << "Oops! Something's wrong!" << endl;

    cout << "Number of nodes: " << g.nodes() << endl;
    cout << "Number of edges: " << g.edges() << endl;
    cout << "Edges at 0: " << g.edges_at(0) << endl;
    cout << "Value at 0: " << g.value_at(0) << endl;
    cout << "Edges at 1: " << g.edges_at(1) << endl;
    cout << "Value at 1: " << g.value_at(1) << endl;
    cout << "Cost between 0 and 1: " << g.cost_between(0, 1) << endl;

    auto mst = g.minimum_spanning_tree();
    if (mst.second) {
        cout << "MST: ";
        for (const auto& node: mst.first)
            cout << node << ", ";
        cout << endl;
    }

    return 0;
}
