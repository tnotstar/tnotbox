//
// graph.hpp: an implementation of the graph adt and some of its algorithms.
//

#ifndef GRAPH_HPP_INCLUDED
#define GRAPH_HPP_INCLUDED

#include <set>
#include <limits>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

namespace graph {

    /**
     * A template class to store a sparse undirected graph, with node
     * labels from type `NodeLabel`, values from type `NodeValue`, and
     * edge's costs from type `EdgeCost`.
     */
    template <typename NodeLabel, typename NodeValue, typename EdgeCost>
    struct sparse_graph {

        /// A type declaration for the node's label type.
        typedef NodeLabel label_type;

        /// A type declaration for the node's value type.
        typedef NodeValue value_type;

        /// A type declaration for the edge's cost type.
        typedef EdgeCost cost_type;

        /// A type declaration for the number of elements (nodes and edges).
        typedef typename std::size_t size_type;

        /// This is the default explicit constructor for objects of this type.
        explicit sparse_graph(const size_type& size=0) :
            nodes_(size)
        {}

        /// Adds a node with given label 'x' and value 'v',
        /// without any neighbours.
        bool
        add_node(const label_type& x, const value_type& v) {
            auto result = nodes_.insert(
                std::make_pair(x, std::make_pair(v, adjacency_list_type()))
            );

            return result.second;
        }

        /// Adds an edge between labelled nodes 'x' and 'y',
        /// with edge's cost equals to 'c'.
        bool
        add_edge(const label_type& x, const label_type& y, const cost_type& c) {
            if (!exists(x))
                return false;

            auto result = nodes_[x].second.insert(std::make_pair(y, c));
            if (!result.second)
                return false;

            // Following insert is used on undirected graphs only.
            if (!exists(y)) {
                if (!add_node(y, nodes_[x].first))
                    return false;
            }

            return nodes_[y].second.insert(std::make_pair(x, c)).second;
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
        /// nodes labelled `x` and `y`.
        cost_type
        cost_between(const label_type& x, const label_type& y) const {
            return nodes_.at(x).second.at(y);
        }

        /// Returns a set with the neighbour's labels from given node `x`.
        std::set<label_type>
        neighbours_from(const label_type& x) const {
            std::set<label_type> neighbours;

            // Tests if there is a node `x` in the graph.
            if (nodes_.count(x) == 0)
                return neighbours;

            for (const auto& node: nodes_.at(x).second)
                neighbours.insert(node.first);

            return neighbours;
        }

#if 0
        /// Returns a set with the node's labels from a minimum spanning
        /// tree calculated using the Prim's algorithm.
        std::pair<std::set<label_type>, bool>
        minimum_spanning_tree() {
            cost_type minimal_cost;
            label_type best_node;
            label_type best_neighbour;
            std::set<label_type> selected_nodes;

            // Try to seletec the first node in the graph, if any.
            for (const auto& node: nodes_) {
                selected_nodes.insert(node.first);
                break;
            }

            // Finds a set of adjacent nodes with minimal cost.
            while (selected_nodes.size() < nodes_.size()) {
                minimal_cost = std::numeric_limits<cost_type>::infinity();
                for (const auto& node: selected_nodes) {
                    for (const auto& neighbour: neighbours_from(node)) {
                        // Tests if this neighbour has been selected already
                        if (selected_nodes.count(neighbour) > 0)
                            continue;

                        // Tests if it's the nearest node right now
                        cost_type current_cost = cost_between(node, neighbour);
                        if (current_cost < minimal_cost) {
                            minimal_cost = current_cost;
                            best_node = node;
                            best_neighbour = neighbour;
                        }
                    }
                }

                // Tests if we found a better neighbour
                if (minimal_cost == std::numeric_limits<cost_type>::infinity())
                    return std::make_pair(selected_nodes, false);

                // Adds the best neighbour to the set of selected node.
                selected_nodes.insert(best_neighbour);
            }

            // A solution has been found, returning it!
            return std::make_pair(selected_nodes, selected_nodes.size() == nodes_.size());
        }

        /// Loads the graph from a file with given name.
        bool
        load_from_file(const std::string& filename) {
            label_type x, y;
            cost_type cost;
            size_type nodes;

            std::ifstream input(filename, std::ios::in);
            if (!input.good() || input.eof())
                return false;

            input >> nodes;
            while (!input.eof()) {
                input >> x >> y >> cost;
                std::cout << x << "x" << y << ": " << cost << std::endl;

                add_node(x, std::numeric_limits<cost_type>::infinity());
                add_node(y, std::numeric_limits<cost_type>::infinity());

                add_edge(x, y, cost);
            }
            input.close();

            return true;
        }
#endif // 0

    protected:
        // A protected type declaration for the adjacency list of a node.
        typedef typename std::unordered_map<label_type, cost_type> adjacency_list_type;

        // A protected type declaration for the type of each node.
        typedef typename std::pair<value_type, adjacency_list_type> node_type;

        // Internal graph representation as a map from labels to nodes.
        std::unordered_map<label_type, node_type> nodes_;
    };

} // namespace graph

#endif // GRAPH_HPP_INCLUDED
