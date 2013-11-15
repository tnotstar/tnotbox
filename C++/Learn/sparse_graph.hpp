//
// sparse_graph.hpp: a graph implementation based on adjacency lists
//

#ifndef SPARSE_GRAPH_H
#define SPARSE_GRAPH_H

#include <iostream>
#include <unordered_map>

/**
 * TODO
 */
template <typename NodeLabel, typename NodeValue, typename EdgeCost>
class sparse_graph {
public:
    /// TODO
    typedef NodeLabel label_type;

    /// TODO
    typedef NodeValue value_type;

    /// TODO
    typedef EdgeCost cost_type;

    /// TODO
    typedef std::size_t size_type;

    /// TODO
    typedef size_type index_type;

    /// TODO
    sparse_graph(size_type size=0) :
        nodes(size)
    {}

    /// TODO
    void
    add_edge(const label_type& x, const label_type& y, const cost_type& value) {
    }

private:
    // TODO
    typedef typename std::unordered_map<label_type, cost_type> adjacency_list;

    // TODO
    struct node_type {
        value_type value;
        adjacency_list neighbours;
    };

    // TODO
    std::unordered_map<label_type, node_type> nodes;

    // TODO
    template <typename L, typename V, typename C>
    friend std::ostream&
    operator<< (std::ostream& out, const sparse_graph<L, V, C>& graph);
};

template <typename L, typename V, typename C>
std::ostream&
operator<< (std::ostream& out, const sparse_graph<L, V, C>& graph) {
    out << graph.nodes.size();
    return out;
}

#endif // SPARSE_GRAPH_H
