#include <iostream>
#include <vector> 
#include <algorithm> 

using namespace std;

int
main1 () {

    int a = 2, b = -3, c = 2;
    bool tval1 = false, tval2 = true; 
    char ch = 'b';

    cout << "Q01. " << (b + c * a) << endl;
    cout << "Q02. " << (c % 5 / 2) << endl;
    cout << "Q03. " << (-a * c++) << endl;
    cout << "Q04. " << (tval1 && tval2) << endl;
    cout << "Q05. " << (ch += 2) << endl;

    return 0;
}

template <class T1, class T2> 
int mystery(T1& a, T2 b, int c) 
{ 
      T1 t = a; 
      a = a + b; 
      return ( a - t + c); 
}

int main2(void) 
{ 
      int a = 3; 
      double b = 2.5; 
      int c = 1; 
      
      cout << " answer 1 is  " << mystery(a, 2, c) << endl; 
      cout << " answer 2 is  " << mystery(a, 1, c) << endl; 
      a = 5; 
      cout << " answer 3 is  " << mystery(a, b, c) << endl; 
      a = 2; 
      b = 2.5; 
      cout << " answer 4 is  " << mystery(a, b, b) << endl; 
      cout << " answer 5 is  " << mystery(a,mystery(a, b, b),c)<< endl; 
      return 0; 
}

int main3() 
{ 
    int data[5]={1,7,46,9,6}; 
    vector<int> data_vec(data, data+5); 
    int modulus = 3; 
    //use of lambda's for predicates in find_if 
    auto q =  find_if( data_vec.begin(),data_vec.end(), 
                      [](int elem)->bool{ if (elem % 2 ==0 ) return true; 
                                                    else  return false;} 
    ) ;

    cout << "first *q " << *q << endl;

    //next lambda has a capture by value

    q =  find_if( data_vec.begin(),data_vec.end(), 
                      [=](int elem)->bool{ if (elem % modulus ==0 ) return true;   
                                                    else  return false;}

    ) ;

    cout << "second *q " << *q << endl; 
}

int main4()
{
    vector<int> data(5,1);
    int sum {0};

    cout << sum << endl;
    
    for(auto element : data)
         sum += element;
    cout << sum << endl;

    for(auto p = ++data.begin(); p != --data.end(); ++p)
         sum += *p;
    cout << sum << endl;
  
    sum = 0;
    data.push_back(2);
    data.push_back(3);
    
    for(auto element : data)
         sum += element;
    cout << sum << endl;

    cout << accumulate(data.begin(), data.end(), data[0]) << endl;
}

class Animal {
public:  
    virtual void speak()=0;
    virtual  void purr() { cout << "Purr\n"; }
};
class Cat : public Animal {
public:  
    void speak() { cout << "Meow\n";purr(); }
};
class Lion : public Cat {
public:  
    void speak() { cout << "ROAR\n"; }
    void purr() { cout << "ROAR\n"; }
};
int main() {
  Animal* c = new Cat();
  Cat napster;
  Lion googly;

  c->speak(); 
 
  napster.speak();
  googly.speak();
  return 0; 
}


