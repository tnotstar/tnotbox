#include <iostream>

using namespace std;

template <class T, size_t N>
class simple_array {
public:
    typedef T value_type;

    // This is a default constructor.
    simple_array() :
        data_(nullptr)
    {
        data_ = new value_type[N];
    }

    // This is an ordinary `copy constructor`,
    // but see the next remark about
    // "construction delegation".
    simple_array(const simple_array& other) :
        simple_array()
    {
        for (size_t i = 0; i < N; ++i)
            data_[i] = other[i];
    }

    // This is a conversion constructor, but
    // with an `explicit` keyword to
    // suppress automatic coercion & it's a
    // sample of a C++11 feature named:
    //  * Delegate construction:
    //    - to make use of an already defined
    //      constructor
    explicit simple_array(value_type *other) :
        simple_array()
    {
        for (size_t i = 0; i < N; ++i)
            data_[i] = other[i];
    }

    ~simple_array()
    {
        delete[] data_;
    }

private:
    value_type* data_;
};

int
main () {
    simple_array<int, 10> arr;
    return 0;
}
