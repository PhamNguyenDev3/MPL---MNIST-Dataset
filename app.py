import tkinter as tk
from tkinter import Canvas, Button, Label, PhotoImage
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

class HandwrittenDigitRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Handwritten Digit Recognition")
        self.master.geometry("400x500")
        self.master.configure(bg="#f0f0f0")

        self.label_title = Label(self.master, text="Digit Recognition", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        self.label_title.pack(pady=(20, 10))

        self.canvas = Canvas(self.master, width=280, height=280, bg="white", highlightthickness=0)
        self.canvas.pack()

        self.button_clear = Button(self.master, text="Clear", command=self.clear_canvas, font=("Arial", 14), bg="#333", fg="#fff", bd=0, padx=10)
        self.button_clear.pack(pady=(10, 5))

        self.button_predict = Button(self.master, text="Predict", command=self.predict_digit, font=("Arial", 14), bg="#333", fg="#fff", bd=0, padx=10)
        self.button_predict.pack(pady=5)

        self.label_result = Label(self.master, text="Prediction: None", font=("Arial", 16), bg="#f0f0f0", fg="#333")
        self.label_result.pack(pady=(20, 10))

        self.label_probabilities = Label(self.master, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        self.label_probabilities.pack(pady=5)

        self.image = Image.new("L", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)

        # Load the trained model
        self.model = tf.keras.models.load_model('models/model2.keras')

    def draw_on_canvas(self, event):
        x, y = event.x, event.y
        r = 10
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.label_result.config(text="Prediction: None")
        self.label_probabilities.config(text="")

    def predict_digit(self):
        resized_image = self.image.resize((28, 28))
        resized_image_array = np.array(resized_image)
        
        # Chuyển nền đen và chữ trắng
        inverted_image_array = 255 - resized_image_array
        normalized_image_array = inverted_image_array / 255.0
        
        prediction = self.model.predict(normalized_image_array.reshape((1, 28, 28)))
        predicted_label = np.argmax(prediction)
        self.label_result.config(text=f"Prediction: {predicted_label}")
        
        probabilities = [f"{i}: {prob*100:.4f}" for i, prob in enumerate(prediction[0])]
        self.label_probabilities.config(text="\n".join(probabilities))
        
        # Display the drawn image
        plt.imshow(normalized_image_array, cmap='gray')
        plt.axis('off')
        plt.show()

def main():
    root = tk.Tk()
    app = HandwrittenDigitRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
