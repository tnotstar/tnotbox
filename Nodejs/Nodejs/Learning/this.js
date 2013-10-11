var abc = 1;

function foo () {
    function baz() {
        console.log(abc);
    }
    console.log(abc);
    baz();
}

function bar () {
    function baz() {
        console.log(this);
    }
    console.log(this);
    baz();
}

foo();
bar();

var Proxymier = function (options) {

    if (!options)
        throw new Error("Missing 'options' value");

    var self = this;

    self.options = options;
}

var p =