/* this code has been stolen from https://www.youtube.com/watch?v=7hyXeD48pPU */

SndBuf buffer => dac;
me.dir() + "windowBreak.wav" => buffer.read;

/* length method returns duration of the read file */
buffer.length() => now;