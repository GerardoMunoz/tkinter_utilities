# tkinter_utilities

## ZoomCanvas Class
The ZoomCanvas class is a custom Tkinter canvas widget that supports zooming, panning, and scrolling functionalities. This class is designed to handle graphical elements, allowing users to zoom in and out while keeping the text elements correctly scaled.

### Features
* Zooming: Easily zoom in and out using the mouse wheel while holding the Control key.
* Panning: Pan across the canvas using the middle mouse button (mouse wheel button).
* Scrolling: Scroll vertically and horizontally using the mouse wheel with the Alt and Shift keys respectively.
* Auto-Adjusting Scroll Region: Automatically adjusts the scroll region to fit the canvas content after resizing or zooming.
* Text Scaling: Text items on the canvas scale appropriately with the zoom level.

### Usage
To use the ZoomCanvas class, instantiate it within a Tkinter application and add graphical elements to it. Below is an example of how to use the ZoomCanvas in a simple application.

### Methods
* create_zoomable_rectangle_with_text(self, x1, y1, x2, y2, **kwargs): Creates a rectangle with centered text on the canvas.
* create_zoomable_text(self, x, y, **kwargs): Creates text on the canvas and stores its original font size for correct scaling.

### Powered by ChatGPT
