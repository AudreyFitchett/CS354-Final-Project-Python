

# app.py
# This will be the main GUI application class.

import customtkinter as ctk

# --- Import predict_heart_disease from predict.py ---
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from predict import predict_heart_disease

###### Window

# Consistent color scheme
BG_COLOR = "#23272e"  # dark background
FRAME_COLOR = "#23272e"  # same as background for consistency

app = ctk.CTk()
app.title("Heart Disease Predictor")
app.geometry("1200x600")
app.resizable(False, False)
app.configure(bg=BG_COLOR)


###### Header frame
header = ctk.CTkFrame(app, height=50, corner_radius=0, fg_color=FRAME_COLOR)
header.pack(side="top", fill="x")

# Title label
# TODO: Add a logo to the left of the title label
title_label = ctk.CTkLabel(header, text="Heart Disease Predictor", font=("Arial", 20, "bold"))
title_label.pack(side="left", padx=20, pady=10)

###### Buttons
informationButton = ctk.CTkButton(header, text="About", width=250, font=("Arial", 16))
informationButton.pack(side="right", padx=20)

# Function to show About popup

def show_about():
	about_popup = ctk.CTkToplevel(app)
	about_popup.title("About")
	about_popup.geometry("500x320")
	about_popup.resizable(False, False)
	about_popup.configure(bg=BG_COLOR)
	about_popup.transient(app)  # Always on top of main window
	about_popup.grab_set()      # Modal behavior

	# Center the popup on the main window
	app.update_idletasks()
	x = app.winfo_x() + (app.winfo_width() // 2) - 250
	y = app.winfo_y() + (app.winfo_height() // 2) - 160
	about_popup.geometry(f"500x320+{x}+{y}")

	about_label = ctk.CTkLabel(
		about_popup,
		text="Heart Disease Predictor\n\nThis application predicts the likelihood of heart disease based on user input.\n\nDeveloped for CS354 Final Project.",
		font=("Arial", 16),
		justify="center"
	)
	about_label.pack(expand=True, padx=20, pady=20)

informationButton.configure(command=show_about)

settingsButton = ctk.CTkButton(header, text="Settings", width=250, font=("Arial", 16))
settingsButton.pack(side="right", padx=20)


# Function to clear all input fields and reset dropdowns
def clear_inputs():
	age_entry.delete(0, 'end')
	bmi_entry.delete(0, 'end')
	phys_entry.delete(0, 'end')
	mental_entry.delete(0, 'end')
	gender_var.set("M/F")
	smoking_var.set("Y/N")
	alcohol_var.set("Y/N")
	stroke_var.set("Y/N")
	walk_var.set("Y/N")

clearButton = ctk.CTkButton(header, text="Clear", width=250, font=("Arial", 16), command=clear_inputs)
clearButton.pack(side="right", padx=20)

# TODO: Possibly add another button that leads to the model used for prediction, or to the dataset used for training the model.



###### Main content frame
# Create a main frame to hold the left (inputs) and right (prediction) sections

main_frame = ctk.CTkFrame(app, fg_color=FRAME_COLOR)
main_frame.pack(fill="both", expand=True)

# Function to clear focus from any input box
def clear_focus(event):
	app.focus_set()



# Left frame for input fields (now with two horizontal rows, centered)
input_frame = ctk.CTkFrame(main_frame, width=700, fg_color=FRAME_COLOR)
input_frame.pack(side="left", fill="both", expand=True, padx=40, pady=40)

# Center container for input rows
center_container = ctk.CTkFrame(input_frame, fg_color=FRAME_COLOR)
center_container.pack(expand=True)



# Two horizontal frames for input rows, centered horizontally
row1 = ctk.CTkFrame(center_container, fg_color=FRAME_COLOR)
row1.pack(pady=(0, 10))
row2 = ctk.CTkFrame(center_container, fg_color=FRAME_COLOR)
row2.pack()

# Bind left mouse click on all relevant frames to clear focus
main_frame.bind("<Button-1>", clear_focus)
input_frame.bind("<Button-1>", clear_focus)
center_container.bind("<Button-1>", clear_focus)
row1.bind("<Button-1>", clear_focus)
row2.bind("<Button-1>", clear_focus)


# Right: Prediction percentage label
percentage_label = ctk.CTkLabel(main_frame, text="Prediction: 100%", font=("Arial", 40), width=400, anchor="center")
percentage_label.pack(side="right", padx=20, pady=30, fill="y", expand=True)



###### Questions (Input fields)



# --- Input validation functions ---
def validate_age(new_value):
	if new_value == "":
		return True
	try:
		val = int(new_value)
		return 1 <= val <= 100
	except ValueError:
		return False

def validate_bmi(new_value):
	if new_value == "":
		return True
	try:
		val = float(new_value)
		return 0 <= val <= 60
	except ValueError:
		return False

def validate_days(new_value):
	if new_value == "":
		return True
	try:
		val = int(new_value)
		return 0 <= val <= 30
	except ValueError:
		return False

vcmd_age = app.register(validate_age)
vcmd_bmi = app.register(validate_bmi)
vcmd_days = app.register(validate_days)

# First row: Gender, Age, BMI, Smoking, Alcohol
gender_label = ctk.CTkLabel(row1, text="Gender:", font=("Arial", 16))
gender_label.grid(row=0, column=0, sticky="w", padx=(0, 2), pady=(0, 2))
gender_var = ctk.StringVar(value="M/F")
gender_option = ctk.CTkOptionMenu(row1, variable=gender_var, values=["Male", "Female"])
gender_option.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

age_label = ctk.CTkLabel(row1, text="Age:", font=("Arial", 16))
age_label.grid(row=0, column=1, sticky="w", padx=(0, 2), pady=(0, 2))
age_entry = ctk.CTkEntry(row1, placeholder_text="Enter age", validate="key", validatecommand=(vcmd_age, '%P'))
age_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

bmi_label = ctk.CTkLabel(row1, text="BMI:", font=("Arial", 16))
bmi_label.grid(row=0, column=2, sticky="w", padx=(0, 2), pady=(0, 2))
bmi_entry = ctk.CTkEntry(row1, placeholder_text="Enter BMI", validate="key", validatecommand=(vcmd_bmi, '%P'))
bmi_entry.grid(row=1, column=2, padx=(0, 10), pady=(0, 10))

smoking_label = ctk.CTkLabel(row1, text="Smoking:", font=("Arial", 16))
smoking_label.grid(row=0, column=3, sticky="w", padx=(0, 2), pady=(0, 2))
smoking_var = ctk.StringVar(value="Y/N")
smoking_option = ctk.CTkOptionMenu(row1, variable=smoking_var, values=["Yes", "No"])
smoking_option.grid(row=1, column=3, padx=(0, 10), pady=(0, 10))

alcohol_label = ctk.CTkLabel(row1, text="Alcohol Consumption:", font=("Arial", 16))
alcohol_label.grid(row=0, column=4, sticky="w", padx=(0, 2), pady=(0, 2))
alcohol_var = ctk.StringVar(value="Y/N")
alcohol_option = ctk.CTkOptionMenu(row1, variable=alcohol_var, values=["Yes", "No"])
alcohol_option.grid(row=1, column=4, padx=(0, 10), pady=(0, 10))

# Second row: Stroke, Difficulty Walking, Bad Physical Health, Bad Mental Health
stroke_label = ctk.CTkLabel(row2, text="Stroke:", font=("Arial", 16))
stroke_label.grid(row=0, column=0, sticky="w", padx=(0, 2), pady=(0, 2))
stroke_var = ctk.StringVar(value="Y/N")
stroke_option = ctk.CTkOptionMenu(row2, variable=stroke_var, values=["Yes", "No"])
stroke_option.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

walk_label = ctk.CTkLabel(row2, text="Difficulty Walking:", font=("Arial", 16))
walk_label.grid(row=0, column=1, sticky="w", padx=(0, 2), pady=(0, 2))
walk_var = ctk.StringVar(value="Y/N")
walk_option = ctk.CTkOptionMenu(row2, variable=walk_var, values=["Yes", "No"])
walk_option.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))


phys_label = ctk.CTkLabel(row2, text="Bad Physical Health Days (last 30):     ", font=("Arial", 16))
phys_label.grid(row=0, column=2, sticky="w", padx=(0, 2), pady=(0, 2))
phys_entry = ctk.CTkEntry(row2, placeholder_text="Enter number of days", validate="key", validatecommand=(vcmd_days, '%P'))
phys_entry.grid(row=1, column=2, padx=(0, 10), pady=(0, 10))

mental_label = ctk.CTkLabel(row2, text="Bad Mental Health Days (last 30):", font=("Arial", 16))
mental_label.grid(row=0, column=3, sticky="w", padx=(0, 2), pady=(0, 2))
mental_entry = ctk.CTkEntry(row2, placeholder_text="Enter number of days", validate="key", validatecommand=(vcmd_days, '%P'))
mental_entry.grid(row=1, column=3, padx=(0, 10), pady=(0, 10))




# --- Submit button callback ---
def on_submit():
	# Collect user input from GUI
	user_input = {
		"BMI": float(bmi_entry.get()) if bmi_entry.get() else 0,
		"Smoking": smoking_var.get(),
		"AlcoholDrinking": alcohol_var.get(),
		"Stroke": stroke_var.get(),
		"PhysicalHealth": int(phys_entry.get()) if phys_entry.get() else 0,
		"MentalHealth": int(mental_entry.get()) if mental_entry.get() else 0,
		"DiffWalking": walk_var.get(),
		"Sex": gender_var.get(),
		# The following fields are not in the GUI, so use default values or placeholders
		"AgeCategory": "55-59",  # Default, update if you add to GUI
		"Race": "White",         # Default, update if you add to GUI
		"Diabetic": "No",       # Default, update if you add to GUI
		"PhysicalActivity": "No", # Default, update if you add to GUI
		"GenHealth": "Good",    # Default, update if you add to GUI
		"SleepTime": 7,          # Default, update if you add to GUI
		"Asthma": "No",         # Default, update if you add to GUI
		"KidneyDisease": "No",  # Default, update if you add to GUI
		"SkinCancer": "No"      # Default, update if you add to GUI
	}
	try:
		result = predict_heart_disease(user_input)
		percentage_label.configure(text=f"Prediction: {'Yes' if result == 1 else 'No'}")
	except Exception as e:
		percentage_label.configure(text=f"Error: {e}")

submit_button = ctk.CTkButton(center_container, text="Submit", font=("Arial", 18, "bold"), fg_color="#FFD600", text_color="#23272e", hover_color="#FFE066", corner_radius=8, height=40, width=200, command=on_submit)
submit_button.pack(pady=(30, 0))



app.mainloop()


