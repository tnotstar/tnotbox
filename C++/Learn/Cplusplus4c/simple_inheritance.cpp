#include <iostream>
#include <string>

using namespace std;

class student {
public:
    student(const string& name) :
        name_(name)
    {}

    void
    print() const {
        cout << "Student[" << name_ << "]" << endl;
    }

    virtual void
    vprint() const {
        cout << "* Student[" << name_ << "]" << endl;
    }

protected:
    string name_;
};

class graduate_student :
    public student
{
public:
    graduate_student(const string& name, const string &thesis) :
        student(name), thesis_(thesis)
    {}

    void
    print() const {
        cout << "Graduate Student[" << name_ << ": " << thesis_ << "]" << endl;
    }

    virtual void
    vprint() const {
        cout << "* Graduate Student[" << name_ << ": " << thesis_ << "]" << endl;
    }

protected:
    string thesis_;
};

int
main () {
    student joe("Hello, I'm Joe!");
    joe.print();

    graduate_student mike("Hello, I'm Mike!", "The main theory!");
    mike.print();

    student* ptr;

    ptr = &joe;
    ptr->print();
    ptr->vprint();

    ptr = &mike;
    ptr->print();
    ptr->vprint();

    return 0;
}

