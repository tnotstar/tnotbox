--
-- main.lua
--

function love.load()
	text = "Hello, world!"
end


function love.draw()
	love.graphics.print(text, 10, 10)
end

-- EOF