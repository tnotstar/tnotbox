#include <iostream>

using namespace std;

class point {

public:
    point(double x = 0, double y = 0) :
        x_(x), y_(y)
    {}

    double getx() const {
        return x_;
    }

    double gety() const {
        return y_;
    }

    void setx(double v) {
        x_ = v;
    }

    void sety(double v) {
        y_ = v;
    }

private:
    double x_, y_;
};

point
operator+ (const point& l, const point& r) {
    return point(l.getx() + r.getx(), l.gety() + r.gety());
}

ostream&
operator<< (ostream& out, const point& p) {
    out << "(" << p.getx() << ", " << p.gety() << ")";
    return out;
}

int
main () {

    point a(3.5, 2.5);
    point b(2.5, 4.5);

    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    cout << "sum = " << a + b << endl;

    return 0;
}

