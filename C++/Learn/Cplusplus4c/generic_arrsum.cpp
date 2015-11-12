#include <iostream>

using namespace std;

template <class Summable>
Summable arrsum(T *arr, int n) {

    Summable sum = 0;
    for (int i = 0; i < n; i++)
        sum += arr[i];

    return sum;
}

int
main () {

    double arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout << "The sum of following " << n << " items: ";
    for (int i = 0; i < n; ++i) {
        if (i > 0)
            cout << ", ";
        cout << arr[i];
    }
    cout << "; it's " << arrsum(arr, n) << endl;
    return 0;
}

