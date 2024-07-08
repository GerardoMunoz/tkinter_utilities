# Powered by ChatGPT
import tkinter as tk

class ZoomCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.scale_factor = 1.0
        self.bind("<MouseWheel>", self.on_mouse_wheel)
        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-2>", self.start_scroll)  # Middle mouse button
        self.bind("<B2-Motion>", self.scroll)  # Mouse movement with middle button pressed
        self.scan_mark_x = 0
        self.scan_mark_y = 0
        self.rectangles = []  # List to store rectangles and their texts
        self.text_items = []  # List to store text item IDs and their original font sizes

    def on_mouse_wheel(self, event):
        if event.state & 0x0008:  # Mod1 (Alt)
            if event.state & 0x0001:  # Shift
                self.xview_scroll(-1 * (event.delta // 120), "units")  # Horizontal scroll
            elif event.state & 0x0004:  # Control
                self.zoom(event)
            else:
                self.yview_scroll(-1 * (event.delta // 120), "units")  # Vertical scroll
        else:
            self.yview_scroll(-1 * (event.delta // 120), "units")  # Default to vertical scroll if no modifier

    def start_scroll(self, event):
        self.scan_mark_x = event.x
        self.scan_mark_y = event.y
        self.scan_mark(event.x, event.y)

    def scroll(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

    def zoom(self, event):
        scale = 1.1 if event.delta > 0 else 0.9
        self.scale_factor *= scale
        self.scale("all", 0, 0, scale, scale)
        self.configure(scrollregion=self.bbox("all"))
        
        # Adjust font size for zoom for all text items
        for text_id, original_font_size in self.text_items:
            new_font_size = int(original_font_size * self.scale_factor)
            new_font = f"TkDefaultFont {new_font_size}"
            self.itemconfig(text_id, font=new_font)

    def on_resize(self, event):
        self.configure(scrollregion=self.bbox("all"))

    def create_zoomable_rectangle_with_text(self, x1, y1, x2, y2, **kwargs):
        rect_id = self.create_rectangle(x1, y1, x2, y2, **kwargs)
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        text_id = self.create_zoomable_text(center_x, center_y, text="Hello", font="TkDefaultFont 10")
        self.rectangles.append((rect_id, text_id))

    def create_zoomable_text(self, x, y, **kwargs):
        text_id = self.create_text(x, y, **kwargs)
        font_info = self.itemcget(text_id, 'font').split()
        original_font_size = int(font_info[1]) if len(font_info) > 1 else 10  # Default to 10 if not specified
        self.text_items.append((text_id, original_font_size))
        return text_id

def main():
    root = tk.Tk()
    root.title("Zoomable and Scrollable Canvas")

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    zoom_canvas = ZoomCanvas(frame)
    zoom_canvas.grid(row=0, column=0, sticky="nsew")

    v_scrollbar = tk.Scrollbar(frame, orient="vertical", command=zoom_canvas.yview)
    h_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=zoom_canvas.xview)
    zoom_canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Create multiple rectangles with text
    zoom_canvas.create_zoomable_rectangle_with_text(50, 50, 150, 150, fill="blue")
    zoom_canvas.create_zoomable_rectangle_with_text(200, 50, 300, 150, fill="green")
    zoom_canvas.create_zoomable_rectangle_with_text(50, 200, 150, 300, fill="red")

    zoom_canvas.configure(scrollregion=zoom_canvas.bbox("all"))

    root.mainloop()

if __name__ == "__main__":
    main()
