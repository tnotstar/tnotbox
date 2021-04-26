// compile with: tsc greeter.ts
function greeter(person) {
    return 'Hello, ' + person + '!';
}
var user = 'Jane User';
document.getElementById('output1').textContent = greeter(user);
var data = [1, 2, 3];
document.getElementById('output2').textContent = greeter(data);
function greeterWithPerson(person) {
    return 'Hello, ' + person.firstName + ' ' + person.lastName + '!';
}
var person = { firstName: 'Jane', lastName: 'User' };
document.getElementById('output3').textContent = greeterWithPerson(person);
var Student = /** @class */ (function () {
    function Student(firstName, middleInitial, lastName) {
        this.firstName = firstName;
        this.middleInitial = middleInitial;
        this.lastName = lastName;
        this.fullName = firstName + ' ' + middleInitial + ' ' + lastName;
    }
    return Student;
}());
var student = new Student('Jane', 'M.', 'User');
document.getElementById('output4').textContent = greeterWithPerson(student);
// EOT
