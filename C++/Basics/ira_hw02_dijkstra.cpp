//
// ira_hw02_disktra.cpp: The homework #2 from "C++ for C programmers".
//

#include <limits>
#include <vector>
#include <utility>
#include <iostream>
#include <unordered_map>

using namespace std;

/**
 * A template class to store an undirected `graph`, with a node labels
 * of the parametrics type `NodeLabel` and edges, with cost values of
 * type `EdgeCost`.
 *
 * This class is based upon the use of the STL type `unordered_map`.
 * With this implementation algorithms are trivial and so we put all
 * them in its `inline` form by writting in a Java-style.
 */
template <typename NodeLabel, typename EdgeCost>
struct graph {

    /// A type declaration for the node's label type.
    typedef NodeLabel label_type;

    /// A type declaration for the edge's cost type.
    typedef EdgeCost cost_type;

    /// A type declaration for an adjacency list with edge's costs
    /// and target nodes' labels.
    typedef unordered_map<label_type, cost_type> edges_type;

    /// A type declaration for an unordered map of nodes with its
    /// adjacency list (v.gr. edges) as mapped values.
    typedef unordered_map<label_type, edges_type> nodes_type;

    /// A type declaration for the number of nodes in the graph.
    typedef typename nodes_type::size_type size_type;


    /// Builds a new graph instance with given number of nodes, or
    /// and empty one if it used as a default constructor.
    graph(size_type size = 0) :
        nodes(size)
    {}

    /// Returns the number of vertices in the graph.
    size_type
    vertices() const {

        return nodes.size();
    }

    /// Returns the number of edges in the graph.
    size_type
    edges() const {

        size_type counter = 0;

        for (const auto &it: nodes)
            counter += it.second.size();

        return counter;
    }

    /// Returns a vector with all nodes y such that there is an edge from x to y.
    vector<label_type>
    neighbors(const label_type& x) const {

        vector<label_type> results;

        for (const auto &it: nodes.at(x)) // Using `at` to get a const iterator.
            results.push_back(it.first);

        return results;
    }

    /// Tests whether there is an edge from node x to node y.
    bool
    adjacent(const label_type& x, const label_type& y) const {

        return nodes.count(x) > 0 && nodes[x].count(y) > 0;
    }

    /// Adds to graph a node with given label and without neighbors.
    void
    add_node(const label_type& x) {

        edges_type empty;
        nodes[x] = empty;
    }

    /// Adds to graph an edge between nodes x and y, if it is not there.
    void
    add_edge(const label_type& x, const label_type& y, const cost_type& v) {

        nodes[x][y] = v;
        nodes[y][x] = v;    // Second assign as this is an undirected graph.
    }

    /// Removes from graph the edge between x and y, if it is there.
    void
    remove_edge(const label_type& x, const label_type& y) {

        nodes[x].erase(y);
        nodes[y].erase(x);  // Second erase as this is un undirected graph.
    }

    /// Returns the value associated to the edge (x,y).
    cost_type
    get_edge_value(const label_type& x, const label_type& y) {

        return nodes[x][y];
    }

    /// Sets the value associated to the edge (x,y) to v.
    void
    set_edge_value(const label_type& x, const label_type& y, const cost_type& v) {

        nodes[x][y] = v;
        nodes[y][x] = v;    // Second assign as this is an undirected graph.
    }

private:
    /// An instance to an unordered map of nodes with its labels.
    nodes_type nodes;
};

/**
 * A random number generator for a uniform random variable with
 * parameters min and max.
 */
inline double
runif(double min=0.0, double max=1.0) {
    return min + (max - min) * static_cast<double>(rand())/RAND_MAX;
}

/**
 * This function creates an instance of graph<int, double>, with given
 * number of nodes and a set of random edges to make him a connected
 * random graph with a given density value.
 *
 * Edge's costs are also initialized randomly with a uniform random
 * variable in the range (min, max).
 */
inline graph<int, double>
create_random_graph(size_t size, double density, double min, double max) {

    graph<int, double> the_graph(size);

    srand(time(0));
    for (size_t i = 0; i < size; ++i) {
        for (size_t j = 0; j < size; ++j) {
            // First, adds the node i to the graph
            if (j == 0)
                the_graph.add_node(i);

            // Skips self-loops
            if (i == j)
                continue;

            // Randomly creates an edge between nodes i and j
            if (runif() < density)
                the_graph.add_edge(i, j, runif(min, max));
        }
    }

    return the_graph;
}

/**
 * Implements the Dijkstra's algorithm to find the shortest path
 * between the nodes begin and end in given graph.
 */
int
dijkstra_shortest_path(const graph<int, double>& the_graph, int begin, int end) {

    const double INFINITY = numeric_limits<double>::max();
    const int UNDEFINED = -1;

    size_t nodes_nr = the_graph.vertices();

    double distance[nodes_nr];
    int previous[nodes_nr];
    bool visited[nodes_nr];
    
    // Initializes distances, previous and visited trackers.
    for (int i = 0; i < nodes_nr; ++i) {
        distance[i] = INFINITY;
        previous[i] = UNDEFINED;
        visited[i] = false;
    }

    // Prepares the initial node
    distance[begin] = 0;
    queue.add(begin);

// http://en.wikipedia.org/wiki/Dijkstra's_algorithm
// http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
// http://comsci.liu.edu/~jrodriguez/cs631sp08/c++priorityqueue.html
// 
//    for (int i = 0; i < DEFAULT_NODES_NR; ++i) {
//        cout << "Node[" << i << "]:" << endl;
//        for (auto &j: the_graph.neighbors(i))
//            cout << "\t" << j << "=" << the_graph.get_edge_value(i, j) << endl;
//    }

}

/// A type declaration for an edge to a destination node
/// with a cost value.
typedef pair<label_type, cost_type> edge_type;

/**
 * A functor object to compare two given edges.
 *
 * Edges are represented as a pair of a destination node label and
 * its corresponding edge's cost.
 */
template <typename NodeLabel, typename EdgeCost>
struct edge_comparator {

    /// This operator makes objects of this class callables.
    /// Returns true if the edge a is least than edge b.
    bool
    operator() (const edge_type& a, const edge_type& b) {
        return a.second < b.second;
    }
};

typedef priority_queue<

const size_t DEFAULT_NODES_NR = 50;

int
main () {
    cout << "Beginning..." << endl;

    auto the_graph = create_random_graph(DEFAULT_NODES_NR, 0.2, 1.0, 10.0);

    for (int i = 0; i < DEFAULT_NODES_NR; ++i) {
        auto the_path = dijkstra_shortest_path(the_graph, 1, i);
    }

    cout << "Finished!" << endl;
}

