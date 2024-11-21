import tkinter as tk
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2

class DrawingApp:
    def __init__(self, root, model, radius=10):
        self.radius = radius
        
        self.root = root
        self.root.title("MNIST Drawing Pad")
        self.canvas = tk.Canvas(root, width=280, height=280, bg='white')
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.predict)
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear)
        self.clear_button.pack()
        
        self.image = Image.new("L", (280, 280), 255)  # Create a white image (255)
        self.draw_image = ImageDraw.Draw(self.image)
        self.model = model

        # Setup matplotlib figure
        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim(0, 1)
        self.ax.set_xticks(range(10))
        self.ax.set_xticklabels(range(10))
        self.bar_container = self.ax.bar(range(10), [0]*10)

        self.canvas_chart = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_chart.get_tk_widget().pack(side=tk.RIGHT)


    def draw(self, event):
        x, y = event.x, event.y
        x1, y1 = (x - self.radius), (y - self.radius)
        x2, y2 = (x + self.radius), (y + self.radius)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)
        self.draw_image.ellipse([x1, y1, x2, y2], fill="black")

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), 255)
        self.draw_image = ImageDraw.Draw(self.image)
    
    def predict(self, event=None):
        img_array = np.array(self.image)
        img_array=cv2.resize(img_array,(28,28))
        img_array = 255 - img_array
        img_array = img_array.flatten() / 255.0
        
        # Simulated model prediction
        prediction = self.model.use([img_array])[0]  # Replace with actual model call

        for rect, pred in zip(self.bar_container, prediction):
            rect.set_height(pred)
        self.canvas_chart.draw()

if __name__ == "__main__":
    root = tk.Tk()
    
    # Load your trained MNIST model here
    model = None  # Placeholder
    
    app = DrawingApp(root, model)
    root.mainloop()
