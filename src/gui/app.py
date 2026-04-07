# app.py
# This will be the main GUI application class.

import customtkinter as ctk


###### Window

app = ctk.CTk() # Create an instance of the CTk class, which is the main application window
# TODO: Make a logo for window icon
app.title("Heart Disease Predictor") # Set the title of the window
app.geometry("1200x600") # Set the size of the window
app.resizable(False, False) # Make the window non-resizable


###### Header frame
header = ctk.CTkFrame(app, height=50, corner_radius=0)
header.pack(side="top", fill="x")

# Title label
# TODO: Add a logo to the left of the title label
title_label = ctk.CTkLabel(header, text="Heart Disease Predictor", font=("Arial", 20, "bold"))
title_label.pack(side="left", padx=20, pady=10)

###### Buttons
informationButton = ctk.CTkButton(header, text="About", width=250)
informationButton.pack(side="right", padx=20)

settingsButton = ctk.CTkButton(header, text="Settings", width=250)
settingsButton.pack(side="right", padx=20)

clearButton = ctk.CTkButton(header, text="Clear", width=250)
clearButton.pack(side="right", padx=20)

# TODO: Possibly add another button that leads to the model used for prediction, or to the dataset used for training the model.


###### Prediction percentage label

# Text that shows the percentage of the prediction on the right side of the window
# TODO: Update this label with the actual prediction percentage when the model is implemented and integrated with the GUI. 
# Needs to be able to update dynamically based on the model's output.
# TODO: Consider changing font style and color depending on the percentage: green lower than 50%, yellow between 50% and 75%, 
# red above 75%.

percentage_label = ctk.CTkLabel(app, text="Prediction: 0%", font=("Arial", 40))
percentage_label.pack(side="right", padx=20, pady=10)


###### Input boxes

# Gender (M/F)

# Age (int)

# BMI (float number)

# Smoking (T/F)

# Alcohol Consumption (T/F)

# Stroke (T/F)

# Difficulty Walking (T/F)

# Last 30 days bad physical health (int)

# Last 30 days bad mental health (int)



app.mainloop()


