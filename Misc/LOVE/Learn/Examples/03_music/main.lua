--

function love.load()
    sound = love.audio.newSource("music.ogg", "stream")
    love.audio.play(sound)
end

-- EOF
