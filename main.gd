extends Control

# @onready means: wait until this node and its children exist in the tree,
# then grab a reference to MyLabel and store it in this variable.
# The $ is shorthand for "find a child node at this path."
@onready var label: Label = $MyLabel


# This function runs automatically once, when the scene first loads.
func _ready() -> void:
	# .pressed is a *signal* — an event that the Button node broadcasts
	# whenever it gets clicked. Signals are Godot's version of a general
	# CS pattern called "event-driven programming": instead of your code
	# constantly checking "has the button been clicked yet? has it now? now?",
	# you register a function to be called automatically when the event happens.
	# Same underlying idea as onClick in JavaScript or a callback in Python.
	$MyButton.pressed.connect(_on_my_button_pressed)


# This is the function we just told the button to call.
# It only runs when the signal actually fires — i.e. on click.
func _on_my_button_pressed() -> void:
	label.text = "The button works. Hello from GDScript."
	print("Button was clicked.")  # this shows up in Godot's bottom "Output" panel
