/**
 * `main` function could have arguments!!
 */
void main(List<String> args) {
    if (args.length > 0)
        print("Hello, " + args[0] + "!");
    else
        print("Hello, world!");
}
