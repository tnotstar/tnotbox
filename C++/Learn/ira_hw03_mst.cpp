//
// ira_hw03_mst.cpp: Homework #3 from "C++ for C programmers".
//

#include <set>
#include <limits>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <unordered_map>

using namespace std;

/**
 * A template class to store an undirected `graph`, with node labels
 * of the parametric type `NodeLabel` and edges with cost values of
 * type `EdgeCost`.
 *
 * This class is based upon the use of the STL type `unordered_map`.
 * With this implementation algorithms are trivial and so we put all
 * them in its inlined form.
 */
template <typename NodeLabel, typename EdgeCost>
struct graph {

    /// A type declaration for the node's label type.
    typedef NodeLabel label_type;

    /// A type declaration for the edge's cost type.
    typedef EdgeCost cost_type;

    /// A type declaration for the number of components in the graph.
    typedef size_t size_type;


    /// Builds a new graph instance with a given number of
    /// pre-allocated nodes.
    graph(size_type size=0) :
        nodes(size)
    {}

    // Builds a new graph instance with data loaded from the file
    // with given name.
    graph(const string &filename) :
        nodes(0)
    {
        load_from_file(filename);
    }

    /// Adds a node with given label and without any neighbor.
    void
    add_node(const label_type& x) {
        nodes[x] = {};
    }

    /// Adds an edge between nodes "x" and "y", if it is not there.
    void
    add_edge(const label_type& x, const label_type& y, const cost_type& v) {
        nodes[x][y] = v;
        nodes[y][x] = v;    // Second assign as this is an undirected graph.
    }

    /// Returns the number of vertices in the graph.
    size_type
    vertices() const {
        return nodes.size();
    }

    /// Returns the number of edges in the graph.
    size_type
    edges() const {
        size_type counter = 0;

        for (const auto& node: nodes)
            counter += node.second.size();

        return counter;
    }

    /// Returns a vector with all nodes "y" such that exists an edge (x,y).
    vector<label_type>
    neighbors(const label_type& x) const {
        vector<label_type> the_neighbors;

        for (const auto& it: nodes.at(x)) // Using `at` to get a const iterator.
            the_neighbors.push_back(it.first);

        return the_neighbors;
    }

    /// Tests whether there is an edge from node "x" to node "y".
    bool
    adjacent(const label_type& x, const label_type& y) const {
        return nodes.count(x) > 0 && nodes[x].count(y) > 0;
    }

    /// Returns the value associated to the edge (x,y).
    cost_type
    get_edge_cost(const label_type& x, const label_type& y) const {
        return nodes.at(x).at(y);  // Using `at` to get a const value.
    }

    /// Returns the label of the first node in the graph.
    label_type
    get_first_node() const {
        for (const auto& node: nodes)
            return node.first;
    }

private:
    /// A type declaration for an adjacency list with edge's costs
    /// and target nodes' labels.
    typedef unordered_map<label_type, cost_type> edges_type;

    /// A type declaration for an unordered map of nodes with its
    /// adjacency list (v.gr. edges) as mapped values.
    typedef unordered_map<label_type, edges_type> nodes_type;


    /// An instance to an unordered map of nodes with its labels.
    nodes_type nodes;


    /// A private member to load the graph from a file with given name.
    void
    load_from_file(const string& filename) {
        label_type x, y;
        cost_type h;
        size_type n;

        ifstream input(filename, ios::in);
        if (!input.eof())
            input >> n;

        while (!input.eof()) {
            input >> x >> y >> h;
            add_edge(x, y, h);
        }

        input.close();
    }

    /// A `friend` declaration to implement a graph extractor (`<<`).
    template <typename L, typename C>
    friend ostream &
    operator<< (ostream& out, const graph<L, C>& tree);
};

/**
 * An utility operator to print the content of given graph into
 * the given output stream.
 */
template <typename L, typename C>
ostream &
operator<< (ostream& out, const graph<L,C>& the_graph) {
    out << "graph output {" << endl;
    for (const auto& node: the_graph.nodes) {
        for (const auto& neighbor: node.second)
            out << "\t"         << node.first
                << " -- "       << neighbor.first
                << " [label=\"" << neighbor.second
                << "\"];"
                << endl;
    }
    out << "}" << endl;

    return out;
}

/**
 * A template class to calculate the minimum spanning tree from
 * a given graph, which store its results for future uses of them.
 *
 * The class implements the Prim's algorithm.
 */
template <typename Graph>
struct minimum_spanning_tree {

    /// A type declaration for the graph ADT.
    typedef Graph graph_type;

    /// A type declaration for the node's label type.
    typedef typename Graph::label_type label_type;

    /// A type declaration for the edge's cost type.
    typedef typename Graph::cost_type cost_type;

    /// A type declaration for an edge between two nodes with
    /// a given cost value.
    typedef pair<pair<label_type, label_type>, cost_type> edge_type;

    /// A type declaration to store a minimum spanning tree.
    typedef vector<edge_type> edges_type;


    /// A constant with the infinity value from given edge cost type.
    const cost_type INFINITY = numeric_limits<cost_type>::infinity();


    /// Constructs an instance of the class with the given graph
    /// reference used as its parent graph.
    minimum_spanning_tree(const graph_type& parent) :
        edges(0)
    {
        calculate_by_prim(parent);
    }

    /// Returns the total cost from the calculated spanning tree.
    cost_type
    total_cost() const {
        cost_type accum = 0;

        for (const auto& edge: edges)
            accum += edge.second;

        return accum;
    }

private:
    /// Stores the resulting tree calculated from the given graph.
    edges_type edges;

    /// Implements the Prim's algorithm to find the minimum spanning
    /// tree from the given parent graph.
    bool
    calculate_by_prim(const graph_type& parent) {
        set<label_type> selected;
        cost_type minimal;
        label_type x, y;
        
        selected.insert(parent.get_first_node());

        auto vertices = parent.vertices();
        while (selected.size() < vertices) {

            minimal = INFINITY;
            for (const auto& node: selected) {
                for (const auto& neighbor: parent.neighbors(node)) {

                    // Checks if neighbor has been selected already
                    if (selected.count(neighbor) > 0)
                        continue;

                    // Checks if it's the nearest node right now
                    auto current = parent.get_edge_cost(node, neighbor);
                    if (current < minimal) {
                        minimal = current;
                        x = node;
                        y = neighbor;
                    }
                }
            }

            // Checks if there is any neighbor to add to selected
            if (minimal == INFINITY)
                return false;

            // Adds selected neighbor and its edge
            selected.insert(y);
            edges.push_back({{x, y}, minimal});
        }

        return true;
    }

    /// A `friend` declaration to implement a tree extractor (`<<`).
    template <typename G>
    friend ostream &
    operator<< (ostream& out, const minimum_spanning_tree<G>& tree);
};

/**
 * An utility operator to print the content of given tree into
 * the given output stream.
 */
template <typename G>
ostream &
operator<< (ostream& out, const minimum_spanning_tree<G>& the_tree) {
    out << "MST<" << endl;
    for (const auto& edge: the_tree.edges) {
        out << " (" << edge.first.first << ", " << edge.first.second
            << ") = " << edge.second << endl;
    }
    out << ">";

    return out;
}


/// A global constant to store the default name of the input file.
const string DEFAULT_FILENAME = "ira_hw03_mst.dat";


int
main () {
    typedef graph<int, double> graph_type;

    graph_type the_graph(DEFAULT_FILENAME);

    minimum_spanning_tree<graph_type> the_mst(the_graph);

    cout << "The minimum spanning tree is: " << the_mst
         << ", and it has a cost of: " << the_mst.total_cost() << endl;

    return 0;
}

