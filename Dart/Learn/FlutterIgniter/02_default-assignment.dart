// 02_default-assignment.dart

main () {
   var bones;

   bones ??= 1;    // Or: bones = bones ?? 1
   print(bones);   // Must to show `1`
}

// EOF
