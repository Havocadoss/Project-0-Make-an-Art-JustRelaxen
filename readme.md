# Project Proposal

1. A house with four windows, a door, and a chimmeny.


2. **line_color**: This variable controls the color of the lines used to outline the shapes. You can change the value assigned to `line_color` to any valid color name or code to modify the outline color of the house, roof, door, windows, and chimney. **fill_color**: This variable determines the fill color of the shapes. You can change the value assigned to `fill_color` to any valid color name or code to modify the fill color of the house, roof, door, windows, and chimney.


3. Color Specification: The line color and fill color are specified multiple times in the code when drawing different shapes.
Shape Drawing: The draw_shape function is used to draw rectangles, and it's called for drawing the main house, the roof, the door, the windows, and the chimney. Window Positions: The window positions are specified in a list, and a loop is used to draw windows at these positions.


4. The main parts of the drawing are:
   - The house (including the main body and the roof).
   - The door.
   - The windows.
   - The chimney.


5. window's position. The for loop iterates over each tuple in window_positions, and the loop variable position takes on each tuple's value in each iteration. Inside the loop, the draw_shape function is called with different position values to draw windows at different positions based on the values in the list. This way, the same object (window) is repeated at different locations in the house. So, the loop is used to create a repeated pattern of windows in the house, where each window is drawn with a slightly different position specified in the window_positions list.