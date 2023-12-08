
import tkinter as tk
from tkinter import ttk
import logging


def configure_logging():
  # Configures logging settings for the application.
  logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()])


class ShippingCalculatorApp:
  # Main application class for the Shipping Calculator.
    def __init__(self, root):
       # Initializes the ShippingCalculatorApp with the main GUI components.
        self.root = root
        self.root.title("Shipping Calculator")

        # Configure a custom style for the labels and buttons
        style = ttk.Style()
        style.configure("TLabel", background="#ECECEC", padding=8)
        style.configure("TButton", background="#4CAF50", padding=10, foreground="white")

        self.root.configure(padx=15, pady=15)  # Set padx and pady for the root window

        # Labels
        self.weight_label = ttk.Label(root, text="Enter the package weight:", style="TLabel")
        self.weight_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Entry
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Button
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_shipping, style="TButton")
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = ttk.Label(root, text=None, style="TLabel")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid_remove()  # Hide the label initially


    def calculate_shipping(self):
        # Calculates shipping prices based on user input and displays the result.
        try:
            weight = float(self.weight_entry.get())
            if weight > 0:
                ground_price = calculate_ground_price(weight)
                drone_price = calculate_drone_price(weight)

                result_text = (
                    f"Your price for Ground Shipping: ${ground_price:.2f}\n"
                    "Your price for Ground Shipping Premium: $125.00\n"
                    f"Your price for Drone Shipping: ${drone_price:.2f}"
                )

                self.result_label.config(text=result_text)
                self.result_label.grid()  # Show the label
                logging.info("Shipping calculation successful.")

            else:
                self.result_label.config(text="Weight must be greater than 0. Please try again.")
                self.result_label.grid()  # Show the label
                logging.warning("Invalid weight entered.")

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid numeric value.")
            self.result_label.grid()  # Show the label
            logging.error(f"Invalid input: {self.weight_entry.get()}")
            
  
def calculate_ground_price(weight):
    if weight <= 2:
        return 1.50 * weight + 20
    elif 2 < weight <= 6:
        return 3 * weight + 20
    elif 6 < weight <= 10:
        return 4 * weight + 20
    elif weight > 10:
        return 4.75 * weight + 20

def calculate_drone_price(weight):
    if weight <= 2:
        return 4.50 * weight
    elif 2 < weight <= 6:
        return 9 * weight
    elif 6 < weight <= 10:
        return 12 * weight
    elif weight > 10:
        return 14.25 * weight

def main(): 
    configure_logging()
    logging.info("Shipping Calculator App started.")

    root = tk.Tk()
    ShippingCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
      main()













