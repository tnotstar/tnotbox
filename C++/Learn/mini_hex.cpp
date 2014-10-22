#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class graph {

    graph(const size_t& size=0) :
        node_(size)
    {}

    void
    add_edge(const size_t& x, const size_t& y) {
        if (nodes_.size() < x)
            nodes_.resize(x);
    }
 
protected:
    vector<deque<int> > node_;

    friend
    ostream&
    operator<< (ostream& out, const graph& g);
};

ostream&
operator<< (ostream& out, const graph& g) {
    out << "Hello, world!";
    return out;
}

int
main () {

    graph g;
    cout << g << endl;

    return 0;
}

