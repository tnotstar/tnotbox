package com.example.hello;

import java.util.Arrays;

public class Main {

    static public void main(String[] args) {
        if (args.length > 0)
            System.out.println("Hello, " + Arrays.toString(args) + "!");
        else
            System.out.println("Hello, world!");
    }
}
