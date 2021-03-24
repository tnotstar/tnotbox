/* this code has been stolen from https://www.youtube.com/watch?v=7hyXeD48pPU */

/* instantiate a "Sine Oscillatoor" named "tone" and connect it
to the digital-to-analog converter */
SinOsc tone => dac;

/* set frequency to 440hz */
440 => tone.freq;
/* make sure it's not too loud */
.6 => tone.gain;
/* run the audio engine for one second */
1::second => now;