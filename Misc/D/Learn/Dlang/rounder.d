//
// rounder.d - round floating point numbers
//

import std.algorithm,
       std.functional,
       std.math,
       std.conv,
       std.regex,
       std.stdio;

// transforms input into a real number,
// rounds it, then converts it to a string
alias round = pipe!(to!real, lround, to!string);

// matches numbers that look like they need rounding
static rxFloatingPoint = ctRegex!`[0-9]+\.[0-9]+`;


void
main(string[] args) {
    // if arguments, process those and exit,
    // otherwise wait around for input on stdin
    if (args.length > 1)
        args[1..$].map!round.joiner(" ").writeln;
    else
        // replace anything that looks like a real number
        // with the rounded equivalent.
        stdin.byLine(KeepTerminator.yes)
            .map!(l => l.replaceAll!(c => c.hit.round)(rxFloatingPoint))
            .copy(stdout.lockingTextWriter());
}

// EOF
