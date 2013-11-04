Homework #2: The Dijkstra's algorithm implementation
===============================================

Introduction
-----------

In this homework we implemented a Monte Carlo simulation to calculate the average shortest path length of a random graph, using the Dijkstra's algorithm \[1\]. With this implementation, we executed two experiments with graphs of size 50 nodes and densities of 20% and 40% respectively.

As result of these experiments, we found that, on average, the shortest path distance between each two nodes from given graphs were: 5.495072 and 3.875268. This results were calculted as the mean of the results from 10 executions of each experiment.

The program was implemented as a single program unit (v.gr. a source file), it compiled as it shows following listing.

````
$ CXX='g++ -std=gnu++11' make ira_hw02_dijkstra
g++ -std=gnu++11     ira_hw02_dijkstra.cpp   -o ira_hw02_dijkstra
````

Then, the following is a listing with the output screen from one of these executions.

```
$ ./ira_hw02_dijkstra
Average shortest path for experiment #1 is: 4.8015
Average shortest path for experiment #2 is: 3.39115
````

The program was compiled using version 4.8.1 of the GNU Compiler Collection (GCC).

Desing and implementation details
------------------------------

The program was implemented using three basic objects: (1) a template class (named `graph`) which implements the abstract data type (ADT) graph, (2) another class (called `shortest_path_finder`) which is a functor object with our Dijkstra's algorithm implementation, and (3) an utility class (called `graph_experiment`) to encapsulate the experiment workflow.

Two utility operators were also implemented to made it easy to print debugging messages. In this way, the program entry-point (v.gr. the `main` function) was keep it as simple as posible like it showed in the following partial listing.

```
int
main () {

    graph_experiment ex1(DEFAULT_SAMPLE_SIZE, 0.2, 1.0, 10.0);
    cout << "Average shortest path for experiment #1 is: " << ex1.simulate() << endl;

    graph_experiment ex2(DEFAULT_SAMPLE_SIZE, 0.4, 1.0, 10.0);
    cout << "Average shortest path for experiment #2 is: " << ex2.simulate() << endl;
}
```

Auxiliary types were also defined, in the scope of each of these basic constructs. For example, a priority queue class inside the `shortest_path_finder` declaration (see source code below).

The graph ADT is based upon the use of the standard template library (STL) \[2\]. The base container selected was the `unordered_map`, because the given low density values. We are assuming here that sparce graph could be implemented most efficiently, with an adjacency list scheme. The use of a template class is justified because we pretend to make use of this graph class in further works.

References
----------

The following resources were consulted during the preparation of this work.

  * \[1\]. Wikipedia's article about "Dijkstra's algorithm". http://en.wikipedia.org/wiki/Dijkstra's_algorithm
  * \[2\]. The cplusplus.com reference site. http://www.cplusplus.com/

Source code
-----------

Following is a complete listing of this homework implementation.

```
//
// ira_hw02_disktra.cpp: Homework #2 from "C++ for C programmers".
//

#include <queue>
#include <vector>
#include <limits>
#include <cassert>
#include <utility>
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

    /// A type declaration for the number of nodes in the graph.
    typedef size_t size_type;


    /// Builds a new graph instance with given number of nodes, or
    /// and empty one if it used as a default constructor.
    graph(size_type size=0) :
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

        for (const auto& it: nodes)
            counter += it.second.size();

        return counter;
    }

    /// Returns a vector with all nodes y such that there is an edge from x to y.
    vector<label_type>
    neighbors(const label_type& x) const {

        vector<label_type> the_neighbors;

        for (const auto& it: nodes.at(x)) // Using `at` to get a const iterator.
            the_neighbors.push_back(it.first);

        return the_neighbors;
    }

    /// Tests whether there is an edge from node x to node y.
    bool
    adjacent(const label_type& x, const label_type& y) const {

        return nodes.count(x) > 0 && nodes[x].count(y) > 0;
    }

    /// Returns the value associated to the edge (x,y).
    cost_type
    get_edge_cost(const label_type& x, const label_type& y) const {

        return nodes.at(x).at(y);  // Using `at` to get a const value.
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

private:
    /// A type declaration for an adjacency list with edge's costs
    /// and target nodes' labels.
    typedef unordered_map<label_type, cost_type> edges_type;

    /// A type declaration for an unordered map of nodes with its
    /// adjacency list (v.gr. edges) as mapped values.
    typedef unordered_map<label_type, edges_type> nodes_type;


    /// An instance to an unordered map of nodes with its labels.
    nodes_type nodes;
};

/**
 * A functor class to calculate the shortest path matrix from
 * an initial node in a given graph, using the Dijkstra's
 * algorithm.
 *
 * NOTE:
 * ----
 *
 * For this homework, this isn't a template class, but it
 * could be generic when we learn how to implement iterators
 * over the nodes and edges of our graph class.
 */
struct shortest_path_finder {

    /// A type declaration for the node's label type.
    typedef int label_type;

    /// A type declaration for the edge's cost type.
    typedef double cost_type;

    /// A type declaration for the graph adt.
    typedef graph<label_type, cost_type> graph_type;


    /// A constant value to represent undefined nodes in the path.
    const label_type UNDEFINED = -1;

    /// A constant value to represent infinity distances.
    const cost_type INFINITY = numeric_limits<cost_type>::infinity();


    /// Constructs an instance of the functor class with given
    /// graph reference and the intial node of the paths.
    shortest_path_finder(const graph_type& parent, const label_type& source=0) :
        parent(parent), source(source), updated(false)
    {}

    /// Returns the shortest path between the initial and given node.
    vector<label_type>
    path_to(const label_type& destination) {

        // Checks if an update of local paths is needed.
        if (!updated)
            updated = update_shortest_paths();

        vector<label_type> the_path;

        auto current = destination;
        do {
            the_path.insert(the_path.begin(), current);
            if (current == source)
                break;
            current = previous[current];
        } while (current != UNDEFINED);

        return the_path;
    }

    /// Returns the cost of a path from initial to the given node.
    double
    distance_to(const label_type& destination) {

        // Checks if an update of local paths is needed.
        if (!updated)
            updated = update_shortest_paths();

        return distance[destination];
    }

private:
    /// A type declaration for an edge to a destination node with a
    /// given cost value.
    typedef pair<label_type, cost_type> edge_type;

    /// A functor object to compare two given edges.
    struct edge_comparator {

        /// This operator makes objects of this class callables.
        /// Returns true if the cost of edge a is greater than b's.
        bool
        operator() (const edge_type& a, const edge_type& b) {
            return a.second > b.second;
        }
    };

    /// A priority queue to temporary store selected edges.
    typedef priority_queue<edge_type, vector<edge_type>, edge_comparator> queue_type;


    /// A reference to the parent graph.
    const graph_type& parent;

    /// The label of the initial node.
    const label_type source;

    /// A vector of calculated distances from the initial node.
    vector<double> distance;

    /// A vector of calculated paths from the initial node.
    vector<int> previous;

    /// A flag to control when to update the paths.
    bool updated;


    /// Implements the Dijkstra's algorithm to find the shortest paths
    /// between initial node and the rest of connected nodes in the
    /// parent graph.
    ///
    /// This function always returns true.
    bool
    update_shortest_paths() {

        size_t vertices = parent.vertices();

        vector<bool> visited;
        queue_type the_queue;

        // Initializes distances, paths, visited nodes and the queue.
        for (int label = 0; label < vertices; ++label) {
            distance.push_back(INFINITY);
            previous.push_back(UNDEFINED);
            visited.push_back(false);
        }

        distance[source] = 0.0;
        the_queue.push({source, distance[source]});

        // Iterates updating shortest paths.
        while (!the_queue.empty()) {

            // Finds next unvisited adjacent node, while discarding visited ones.
            auto current = the_queue.top();
            do {
                the_queue.pop();
                if (!visited[current.first])
                    break;
                current = the_queue.top();
            } while(!the_queue.empty());

            // From here we'll use the Wikipedia's pseudo-code variable names.

            auto u = current.first;
            if (visited[u])
                break;

            visited[u] = true;
            for (const auto& v: parent.neighbors(u)) {

                const auto alt = distance[u] + parent.get_edge_cost(u, v);

                if (alt < distance[v] && !visited[v]) {
                    distance[v] = alt;
                    previous[v] = u;
                    the_queue.push({v, distance[v]});
                }
            }
        }

        return true;
    }
};

/**
 * This is an utility operator to print a graph in verbose experiments.
 */
inline ostream &
operator<< (ostream &out, graph<int, double>& the_graph) {

    size_t vertices = the_graph.vertices();
    for (auto u = 0; u < vertices; ++u) {
        out << endl << "\tNode[" << u << "]: < ";
        for (auto& v: the_graph.neighbors(u))
            out << v << "(" << the_graph.get_edge_cost(u, v) << ") ";
        out << ">";
    }

    return out;
}

/**
 * This is an utility operator to print a path in verbose experiments.
 */
inline ostream &
operator<< (ostream &out, vector<int>& the_path) {

    out << "Path< ";
    for (auto& u: the_path) {
        out << u << " ";
    }
    out << ">";

    return out;
}

/**
 * A class to encapsulate each experiment.
 */
struct graph_experiment {

    /// Constructs an experiment with given experimental parameters.
    graph_experiment(size_t size, double density, double min, double max,
            bool verbose=false) :
        size(size), density(density), min(min), max(max), verbose(verbose)
    {
        assert(size > 0);
        assert(density >= 0.0);
        assert(density <= 1.0);
        assert(min <= max);
    }

    /// Executes the current Monte Carlo expertiment and returns the average
    /// shortest path distance.
    double
    simulate(time_t seed=0) {

        if (!seed)
            seed = time(0);

        if (verbose) {
            cout << "Running experiment with parameters size=" << size
                 << ", density=" << density << ", min=" << min
                 << ", max=" << max << ", seed=" << seed << "..." << endl;
        }

        auto the_graph = create_random_graph(seed);
        auto source = 0;

        if (verbose) {
            cout << "> Generated random graph is:" << the_graph << endl;
        }
        
        shortest_path_finder finder(the_graph, source);

        auto total_cost = 0.0;
        auto paths_found = 0;

        for (auto destination = 0; destination < size; ++destination) {

            if (source == destination)
                continue;

            if (verbose) {
                cout << "> Calculating distance from " << source << " to "
                     << destination << " node..." << endl;
            }

            auto distance = finder.distance_to(destination);

            if (verbose) {
                auto the_path = finder.path_to(destination);

                cout << "> Distance from " << source << " to " << destination
                     << " is: " << distance << " with " << the_path << endl;
            }

            if (distance != finder.INFINITY) {
                total_cost += distance;
                paths_found++;
            }
        }

        auto average_shortest_path_distance = total_cost/paths_found;

        if (verbose)
            cout << "Experiment finished!" << endl;

        return average_shortest_path_distance;
    }

private:
    /// The size of the sample graph.
    size_t size;

    /// The graph density value.
    double density;

    /// The minimum edge cost.
    double min;

    /// The maximum edge cost.
    double max;

    /// A flag to control experiment's verbosity.
    bool verbose;

    /**
    * This function creates an instance of graph<int, double>, with given
    * number of nodes and a set of random edges to make him a connected
    * random graph with a given density value.
    *
    * Edge's costs are also initialized randomly with a uniform random
    * variable in the range (min, max).
    */
    graph<int, double>
    create_random_graph(time_t seed) {

        srand(seed);
        graph<int, double> the_graph(size);

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

    /// A random number generator from a uniform random variable with
    /// parameters min and max.
    ///
    /// This member is an utility static function.
    static double
    runif(double min=0.0, double max=1.0) {
        return min + (max - min) * static_cast<double>(rand())/RAND_MAX;
    }
};


/// A constant value for the default sample size.
const size_t DEFAULT_SAMPLE_SIZE = 50;

int
main () {

    graph_experiment ex1(DEFAULT_SAMPLE_SIZE, 0.2, 1.0, 10.0);
    cout << "Average shortest path for experiment #1 is: " << ex1.simulate() << endl;

    graph_experiment ex2(DEFAULT_SAMPLE_SIZE, 0.4, 1.0, 10.0);
    cout << "Average shortest path for experiment #2 is: " << ex2.simulate() << endl;
}

```

