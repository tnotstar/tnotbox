module HelloWorld

import Random
import JSON

greet() = print("Hello, world!")
greet_alien() = print("Hello, ", Random.string(8), "!")

end # module