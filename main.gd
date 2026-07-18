extends Node2D

# Configuration
var API_URL: String = "http://127.0.0.1:8000/site"
var ROWS: int = 200
var COLS: int = 200
var TILE_SIZE: int = 32
var TILE_COLOR: Color = Color(0.2, 0.6, 0.2)

# Zoom limits
var MIN_ZOOM: float = 0.05  # More zoomed out (smaller zoom value)
var MAX_ZOOM: float = 2.0   # More zoomed in (larger zoom value)

# Internal references
var grid_container: Node2D = null
var http_request: HTTPRequest = null
var camera: Camera2D = null
var grid_width_pixels: int = 0
var grid_height_pixels: int = 0


func _ready():
	# Create the camera
	camera = Camera2D.new()
	camera.zoom = Vector2(0.25, 0.25)
	add_child(camera)
	
	http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(_on_request_completed)
	
	grid_container = Node2D.new()
	grid_container.name = "GridContainer"
	add_child(grid_container)
	
	fetch_map(ROWS, COLS)


func _unhandled_input(event):
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_WHEEL_UP:
			# Zoom in (make zoom bigger = more zoomed in)
			camera.zoom *= 1.15
		elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
				# Zoom out (make zoom smaller = more zoomed out)
			camera.zoom *= 0.85
		
			# Clamp zoom to limits
		camera.zoom.x = clamp(camera.zoom.x, MIN_ZOOM, MAX_ZOOM)
		camera.zoom.y = clamp(camera.zoom.y, MIN_ZOOM, MAX_ZOOM)
		
		# Re-center camera on grid when zoom changes
		_reset_camera_position()
		print("Zoom: ", camera.zoom)


func fetch_map(rows: int, cols: int):
	if grid_container != null:
		for child in grid_container.get_children():
			child.queue_free()
	
	print("Requesting map data for %dx%d..." % [rows, cols])
	var url: String = API_URL + "?rows=%d&cols=%d" % [rows, cols]
	var err: int = http_request.request(url)
	if err != OK:
		printerr("Failed to request map data!")


func _on_request_completed(result: int, response_code: int, headers: PackedStringArray, body: PackedByteArray):
	if response_code == 200:
		var json := JSON.new()
		var parse_err: int = json.parse(body.get_string_from_utf8())
		if parse_err != OK:
			printerr("Failed to parse JSON!")
			return
		
		var data: Dictionary = json.data
		var res_rows: int = int(data["rows"])
		var res_cols: int = int(data["cols"])
		
		print("Received map: %dx%d" % [res_rows, res_cols])
		render_grid(data["grid"])
	else:
		printerr("HTTP Error: %d" % response_code)


func render_grid(grid_data):
	if grid_container == null:
		grid_container = Node2D.new()
		grid_container.name = "GridContainer"
		add_child(grid_container)
	
	# Clear old tiles
	for child in grid_container.get_children():
		child.queue_free()
	
	# Calculate grid size in pixels
	grid_width_pixels = grid_data[0].size() * TILE_SIZE
	grid_height_pixels = grid_data.size() * TILE_SIZE
	
	# For each cell in the grid
	for y in range(grid_data.size()):
		for x in range(grid_data[y].size()):
			var cell_val = grid_data[y][x]
			
			if cell_val != -1:
				var tile := ColorRect.new()
				tile.size = Vector2(TILE_SIZE, TILE_SIZE)
				# Position from top-left corner of the grid (no centering offset)
				tile.position = Vector2(x * TILE_SIZE, y * TILE_SIZE)
				tile.color = TILE_COLOR
				grid_container.add_child(tile)
	
	# Move the camera to look at the CENTER of the grid
	_reset_camera_position()
	
	print("Grid: %d x %d pixels" % [grid_width_pixels, grid_height_pixels])
	print("Camera positioned at: ", camera.position)
	print("Zoom level: ", camera.zoom)


func _reset_camera_position():
	# Center camera on the grid
	var center_x: float = grid_width_pixels / 2
	var center_y: float = grid_height_pixels / 2
	camera.position = Vector2(center_x, center_y)

	