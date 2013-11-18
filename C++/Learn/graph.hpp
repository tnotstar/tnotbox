//
// graph.hpp: some implementations of graph type and its algorithms
//

#ifndef GRAPH_HPP_INCLUDED
#define GRAPH_HPP_INCLUDED

#include <iostream>
#include <algorithm>
#include <unordered_map>

namespace graph {

    /**
     * A template class to store a sparse undirected graph, with node
     * labels of type `NodeLabel`, values of type `NodeValue` and
     * edge's costs of type `EdgeCost`.
     *
     * This class is based upon the use of the STL type `unordered_map`.
     * With this implementation algorithms are trivial and so we put all
     * them in its inlined form.
     */
    template <typename NodeLabel, typename NodeValue, typename EdgeCost>
    class sparse_graph {
    public:
        /// A type declaration for the node's label type.
        typedef NodeLabel label_type;

        /// A type declaration for the node's value type.
        typedef NodeValue value_type;

        /// A type declaration for the edge's cost type.
        typedef EdgeCost cost_type;

        /// A type declaration for the graph sizes.
        typedef std::size_t size_type;

        /// This is the default explicit constructor for objects of this type.
        explicit sparse_graph(size_type size=0) :
            _nodes(size)
        {}

        /// Adds a node with given label and value, without any neighbor.
        void
        add_node(const label_type& x, const value_type& v) {
            _nodes[x] = {v, {}};
        }

        /// Adds an edge between nodes "x" and "y", if it is not there.
        void
        add_edge(const label_type& x, const label_type& y, const cost_type& c) {
            _nodes[x].neighbours[y] = {c};
            _nodes[y].neighbours[x] = {c};  // Second assign for undirected graphs
        }

        /// Returns the current number of nodes in the graph.
        size_type
        nodes() const {
            return _nodes.size();
        }

        /// Returns the current number of edges in the graph.
        size_type
        edges() const {
            size_type counter = 0;
            for (auto &n: _nodes)
                counter += n.second.neighbours.size();
            return counter;
        }

        /// Returns the current number of edges from a given node `x`, or
        /// zero (0) if given node doesn't exists.
        size_type
        edges_at(const label_type& x) const {
            if (_nodes.count(x) == 0)
                return 0;
            return _nodes[x].neighbours.size();
        }

        /// Returns `true` if there's a node with given label `x`,
        /// otherwise returns `false`.
        bool
        exists(const label_type& x) const {
            return _nodes.count(x) > 0;
        }

        /// Returns the current value of a given node `x`, or zero (0)
        /// if `x` doesn't exists.
        value_type
        value_at(const label_type& x) const {
            return _nodes.at(x).value;
        }

    private:
        // A private type declaration for the adjacency list.
        typedef typename std::unordered_map<label_type, cost_type> adjacency_list;

        // A private type declaration for each node type.
        struct node_type {
            value_type value;
            adjacency_list neighbours;
        };

        // Internal graph representation as a map of objects of type node.
        std::unordered_map<label_type, node_type> _nodes;
    };

} // namespace graph

#endif // GRAPH_HPP_INCLUDED
