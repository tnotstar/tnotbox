#include <iostream>

using namespace std;

template <class T>
inline void
my_swap(T& a, T& b) {
    T aux;
    aux = a;
    a = b;
    b = aux;
}

int
main () {
    cout << "Beginning..." << endl;

    int m = 10, n = 5;
    cout << "> m = " << m << ", n = " << n << endl;
    my_swap(m, n);
    cout << "> m = " << m << ", n = " << n << endl;

    double x = 1.2, y = 2.3;
    cout << "> x = " << x << ", y = " << y << endl;
    my_swap(x, y);
    cout << "> x = " << x << ", y = " << y << endl;

    cout << "Finished!" << endl;
    return 0;
}

