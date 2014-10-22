//
// This is my homework #1, this program include following
// changes over its original C version:
//
//   - changed i/o to make use of the `iostream` library
//   - remove arrays by using the `vector` class
//   - as using `vector`, functions don't make use of a length param
//   - vectors are passed as reference, not as pointers
//   - `sum` converted to an inline function (and it's not a procedure)
//   - converted #defined constants to C++ constants
//   - all comments are now line comments
//

#include <iostream>
#include <vector>

using namespace std;

//
// Calculates the sum of items in the given vector.
//
// Notes:
//   - this is a function, it's not a procedure with an output parameter
//   - vector doesn't need to pass its size parameter
//   - `data` it's received as a constant reference to avoid copying
//
template <class Summable>
inline Summable sum(const vector<Summable> &data) {

    int items_nr = data.size();  // calculate the length of `data`

    Summable accum = 0;
    for (int i = 0; i < items_nr; ++i)
        accum = accum + data[i]; // to avoid assuming `+=` overloading

    return accum;
}

//
// This is the size of our experimental data.
//
const int N = 40;

//
// This is the program's entry-point.
//
int main()
{
    vector<int> data;

    for (int i = 0; i < N; ++i)
        data.push_back(i);  // inserting items back in the vector

    int accum = sum(data);  // using our new terse function call

    cout << "The sum is: " << accum << "!" << endl;

    return 0;
}

