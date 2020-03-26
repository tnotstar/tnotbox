--
-- main.lua
--

function love.load()
	print("Loading...")
	
	x = 10
	player_name = "Eamonn"
	y = 20
	gold = "100"

	print("Loaded!")
end

function love.update(dt)

end

function love.draw()

end

function love.focus(bool)
	print(bool)
end

function love.textinput(text)
	print("Unicode char is " .. text)
end

function love.resize(w, h)
	print("New window width: " .. w .. 
		", new window height: " .. h .. "!")
end

function love.keypressed(key)
	print("Key: " .. key .. "!")
end

function love.keyreleased(key)
	print("Key: " .. key .. "!")
end

-- EOF