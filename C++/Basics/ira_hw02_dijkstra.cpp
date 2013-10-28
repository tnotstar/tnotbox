#include <iostream>
#include <vector>
#include <utility>

using namespace std;

struct digraph {

    typedef int vertex;
    typedef pair<vertex, vertex> edge;

    typedef vector<vertex> vertices;
    typedef vector<edge> edges;

public:
    digraph(const vertices& v, const edges& e) {
        for (vertices::const_iterator it = v.begin(); it != v.end(); it++)
            cout << *it << endl;
    }

private:
};

int
main () {
    cout << "Beginning..." << endl;

    digraph::vertex v[] = {1, 2, 3, 4, 5};
    digraph::vertices vv(v, v + sizeof(v)/sizeof(v[0]));

    digraph::edges ee;

    digraph g(vv, ee);

    cout << "Finished!" << endl;

    return 0;
}

