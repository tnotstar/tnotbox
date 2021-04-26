// compile with: tsc greeter.ts

function greeter (person: string) {
    return 'Hello, ' + person + '!';
}

let user = 'Jane User';
document.getElementById('output1').textContent = greeter(user);

let data = [1, 2, 3];
document.getElementById('output2').textContent = greeter(data);


interface Person {
    firstName: string;
    lastName: string;
}

function greeterWithPerson (person: Person) {
    return 'Hello, ' + person.firstName + ' ' + person.lastName + '!';
}

let person = { firstName: 'Jane', lastName: 'User' };
document.getElementById('output3').textContent = greeterWithPerson(person);

class Student {
    fullName: string;
    constructor (public firstName: string, public middleInitial: string,
      public lastName: string)
    {
        this.fullName = firstName + ' ' + middleInitial + ' ' + lastName;
    }
}

let student  = new Student('Jane', 'M.', 'User');
document.getElementById('output4').textContent = greeterWithPerson(student);

// EOT