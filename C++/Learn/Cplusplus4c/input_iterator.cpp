#include <iostream>
#include <fstream>
#include <numeric>
#include <iterator>

using namespace std;

int
main () {

    ifstream input("input_iterator.dat");

    istream_iterator<int> iter(input);
    istream_iterator<int> eos;

    cout << "Sum of data is "
         << accumulate(iter, eos, 0)
         << endl;

    return 0;
}

