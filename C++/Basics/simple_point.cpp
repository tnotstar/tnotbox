#include <iostream>

using namespace std;

class point {

public:
    double x, y;
};

point
operator+ (point& left, point& right) {
    point results = {left.x + right.x, left.y + right.y};
    return results;
}

ostream&
operator<< (ostream& out, point p) {
    out << "(" << p.x << ", " << p.y << ")";
    return out;
}

int
main () {

    point a = {3.5, 2.5};
    point b = {2.5, 4.5};

    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    cout << "sum = " << a + b << endl;

    return 0;
}

