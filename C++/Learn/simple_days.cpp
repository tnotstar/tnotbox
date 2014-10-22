#include <iostream>

using namespace std;

typedef enum days {
    SUN, MON, TUE, WED, THU, FRI, SAT
};

inline days
operator+ (days d) {  // Note: this is an unary operator '+'!
    return static_cast<days>((static_cast<int>(d) + 1) % 7);
}

ostream &
operator<< (ostream &out, days d) {
    switch (d) {
        case SUN: out << "Sunday"; break;
        case MON: out << "Monday"; break;
        case TUE: out << "Tuesday"; break;
        case WED: out << "Wednesday"; break;
        case THU: out << "Thursday"; break;
        case FRI: out << "Friday"; break;
        case SAT: out << "Saturday"; break;
    }

    return out;  // Note: This is critical!
}

int
main () {
    days today = SUN;
    cout << today << endl;

    days tomorrow = +today;
    cout << tomorrow << endl;

    return 0;
}

