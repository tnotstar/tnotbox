/* this code has been stolen from https://www.youtube.com/watch?v=7hyXeD48pPU */

/* instantiate a "Sound Buffer" named "buffer" and connect it
to digital-to-analog converter */
SndBuf buffer => dac;

/* read the file into the buffer */
me.dir() + "windowBreak.wav" => buffer.read;

/* run the audio engine for one second */
5::second => now;