#
# Learn from: https://www.youtube.com/watch?v=5ySuDzSMGSU
#

# beat
live_loop :drums do
  tick
  sample :sn_dolf if (ring 1,0,0,1,0,1,0,0).look == 1
  sample :drum_bass_hard if (ring 1,0,0,0,1,0,0,0).look == 1
  sample :drum_cymbal_pedal if (ring 0,0,1,0,0,0,1,0).look == 1
  sleep 0.25
end
