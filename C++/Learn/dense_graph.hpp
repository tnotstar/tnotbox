//
// dense_graph.h: a matrix based template class for dense graphs.
//

#ifndef DENSE_GRAPH_H
#define DENSE_GRAPH_H

#include <vector>

/**
 * TODO
 */
template <typename T>
class dense_graph {
public:
    /// TODO
    typedef std::size_t size_type;

    /// TODO
    typedef size_type index_type;

    /// TODO
    typedef T value_type;

    /// TODO
    typedef value_type& reference;

    /// TODO
    typedef const value_type& const_reference;

    /// TODO
    dense_graph(size_type size=0) :
        nodes(size)
    {}

    /// TODO
    void
    add_edge(index_type x, index_type y, const_reference value) {
    }

private:
    // TODO
    typedef typename std::vector<value_type> adjacency_list;

    // TODO
    std::vector<adjacency_list> nodes;
};

#endif // DENSE_GRAPH_H

