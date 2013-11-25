//
// graph.hpp: a implementation of the graph adt and some of its algorithms.
//

#ifndef GRAPH_HPP_INCLUDED
#define GRAPH_HPP_INCLUDED

#include <set>
#include <limits>
#include <iostream>
#include <algorithm>
#include <unordered_map>

namespace graph {

    /**
     * A template class to store a sparse undirected graph, with node
     * labels of type `NodeLabel`, values of type `NodeValue`, and
     * edge's costs of the type `EdgeCost`.
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

        /// A type declaration for the number of nodes and edges.
        typedef typename std::size_t size_type;

    public:
        /// This is the default explicit constructor for objects of this type.
        explicit sparse_graph(const size_type& size=0) :
            nodes_(size)
        {}

        /// Adds a node with given label 'x' and value 'v',
        /// without any neighbours.
        void
        add_node(const label_type& x, const value_type& v) {
            nodes_.insert(
                std::make_pair(x, std::make_pair(v, adjacency_list_type()))
            );
        }

        /// Adds an edge between labelled nodes 'x' and 'y',
        /// with edge's cost equals to 'c'.
        void
        add_edge(const label_type& x, const label_type& y, const cost_type& c) {
            if (exists(x)) {
                nodes_[x].second.insert(std::make_pair(y, c));

                // This assignment is used in undirected graphs only.
                if (!exists(y))
                    add_node(y, nodes_[x].first);
                nodes_[y].second.insert(std::make_pair(x, c));
            }
        }

        /// Returns `true` if there's a node with given label `x`,
        /// otherwise returns `false`.
        bool
        exists(const label_type& x) const {
            return nodes_.count(x) > 0;
        }

        /// Returns the current number of nodes in the graph.
        size_type
        nodes() const {
            return nodes_.size();
        }

        /// Returns the current number of edges in the graph.
        size_type
        edges() const {
            size_type counter = 0;
            for (auto &n: nodes_)
                counter += n.second.second.size();
            return counter;
        }

        /// Returns the number of edges from given node `x`, or
        /// zero (0) if given node doesn't exists.
        size_type
        edges_at(const label_type& x) const {
            if (!exists(x))
                return 0;
            return nodes_.at(x).second.size();
        }

        /// Returns the current value from given node `x`.
        value_type
        value_at(const label_type& x) const {
            return nodes_.at(x).first;
        }

        /// Returns the cost associated with the edge between the
        /// nodes `x` and `y`.
        cost_type
        cost_at(const label_type& x, const label_type& y) const {
            return nodes_.at(x).second.at(y);
        }
/*
        /// Returns the first node in the graph.
        label_type
        get_first_node() const {
            for (auto &n: _nodes)
                return n.first;
        }

        /// Returns a vector with all nodes "y" such that exists an edge (x,y).
        std::vector<label_type>
        neighbours(const label_type& x) const {
            std::vector<label_type> the_neighbours;

            for (auto &it: _nodes.at(x)) // Using `at` to get a const iterator.
                the_neighbours.push_back(it.first);

            return the_neighbours;
        }*/

    protected:
        // A protected type declaration for the adjacency list of a node.
        typedef typename std::unordered_map<label_type, cost_type> adjacency_list_type;

        // A protected type declaration for the type of each node.
        typedef typename std::pair<value_type, adjacency_list_type> node_type;

        // Internal graph representation as a map from labels to nodes.
        std::unordered_map<label_type, node_type> nodes_;
    };

    /**
     * A template class to calculate the minimum spanning tree from
     * a given graph, which store its results for future uses of them.
     *
     * The class implements the Prim's algorithm.
     *
    template <typename Graph>
    class minimum_spanning_tree {
    public:
        /// A type declaration for the graph ADT.
        typedef Graph graph_type;

        /// A type declaration for the node's label type.
        typedef typename Graph::label_type label_type;

        /// A type declaration for the edge's cost type.
        typedef typename Graph::cost_type cost_type;

        /// A type declaration for an edge between two nodes with
        /// a given cost value.
        typedef std::pair<std::pair<label_type, label_type>, cost_type> edge_type;

        /// A type declaration to store a minimum spanning tree.
        typedef std::vector<edge_type> edges_type;


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
            std::set<label_type> selected;

            cost_type minimal;
            label_type x, y;

            selected.insert(parent.get_first_node());

            auto vertices = parent.nodes();
            while (selected.size() < vertices) {

                minimal = std::numeric_limits<cost_type>::infinity();
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
                if (minimal == std::numeric_limits<cost_type>::infinity())
                    return false;

                // Adds selected neighbor and its edge
                selected.insert(y);
                edges.push_back({{x, y}, minimal});
            }

            return true;
        }

        /// A `friend` declaration to implement a tree extractor (`<<`).
        template <typename G>
        friend std::ostream &
        operator<< (std::ostream& out, const minimum_spanning_tree<G>& tree);
    };

    /**
     * An utility operator to print the content of given tree into
     * the given output stream.
     * /
    template <typename G>
    std::ostream &
    operator<< (std::ostream& out, const minimum_spanning_tree<G>& the_tree) {
        out << "MST<" << std::endl;
        for (const auto& edge: the_tree.edges) {
            out << " (" << edge.first.first << ", " << edge.first.second
                << ") = " << edge.second << std::endl;
        }
        out << ">";

        return out;
    }*/

} // namespace graph

#endif // GRAPH_HPP_INCLUDED
