

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
app.geometry("1200x750")
app.resizable(False, False)
app.configure(bg=BG_COLOR)


###### Header frame
header = ctk.CTkFrame(app, height=50, corner_radius=0, fg_color=FRAME_COLOR)
header.pack(side="top", fill="x")

# Title label
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
	sleep_entry.delete(0, 'end')
	gender_var.set("M/F")
	smoking_var.set("Y/N")
	alcohol_var.set("Y/N")
	stroke_var.set("Y/N")
	walk_var.set("Y/N")
	race_var.set("Select")
	diabetic_var.set("Select")
	phys_activity_var.set("Y/N")
	gen_health_var.set("Select")
	asthma_var.set("Y/N")
	kidney_var.set("Y/N")
	skin_cancer_var.set("Y/N")

clearButton = ctk.CTkButton(header, text="Clear", width=250, font=("Arial", 16), command=clear_inputs)
clearButton.pack(side="right", padx=20)


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



# Four horizontal frames for input rows, centered horizontally
row1 = ctk.CTkFrame(center_container, fg_color=FRAME_COLOR)
row1.pack(pady=(0, 10))
row2 = ctk.CTkFrame(center_container, fg_color=FRAME_COLOR)
row2.pack(pady=(0, 10))
row3 = ctk.CTkFrame(center_container, fg_color=FRAME_COLOR)
row3.pack(pady=(0, 10))
row4 = ctk.CTkFrame(center_container, fg_color=FRAME_COLOR)
row4.pack()

# Bind left mouse click on all relevant frames to clear focus
main_frame.bind("<Button-1>", clear_focus)
input_frame.bind("<Button-1>", clear_focus)
center_container.bind("<Button-1>", clear_focus)
row1.bind("<Button-1>", clear_focus)
row2.bind("<Button-1>", clear_focus)
row3.bind("<Button-1>", clear_focus)
row4.bind("<Button-1>", clear_focus)


# Right: Prediction percentage label
percentage_label = ctk.CTkLabel(main_frame, text="", font=("Arial", 40), width=400, anchor="center", wraplength=380, justify="center")
percentage_label.pack(side="right", padx=20, pady=30, fill="y", expand=True)



###### Questions (Input fields)




# --- Input validation functions ---
def validate_age(new_value):
	if new_value == "":
		return True
	if not new_value.isdigit():
		return False
	return int(new_value) <= 100

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

def validate_sleep(new_value):
	if new_value == "":
		return True
	if not new_value.isdigit():
		return False
	return int(new_value) <= 24

vcmd_age = app.register(validate_age)
vcmd_bmi = app.register(validate_bmi)
vcmd_days = app.register(validate_days)
vcmd_sleep = app.register(validate_sleep)

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

bmi_label = ctk.CTkLabel(row1, text="BMI:", font=("Arial", 16), text_color="#3399FF", cursor="hand2")
bmi_label.grid(row=0, column=2, sticky="w", padx=(0, 2), pady=(0, 2))

def open_bmi_url(event=None):
	import webbrowser
	webbrowser.open_new_tab("https://www.calculator.net/bmi-calculator.html") 

bmi_label.bind("<Button-1>", open_bmi_url)
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

# Third row: Race, Diabetic, Physical Activity, General Health
race_label = ctk.CTkLabel(row3, text="Race:", font=("Arial", 16))
race_label.grid(row=0, column=0, sticky="w", padx=(0, 2), pady=(0, 2))
race_var = ctk.StringVar(value="Select")
race_option = ctk.CTkOptionMenu(row3, variable=race_var, values=["White", "Black", "Asian", "American Indian/Alaskan Native", "Hispanic", "Other"])
race_option.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

diabetic_label = ctk.CTkLabel(row3, text="Diabetic:", font=("Arial", 16))
diabetic_label.grid(row=0, column=1, sticky="w", padx=(0, 2), pady=(0, 2))
diabetic_var = ctk.StringVar(value="Select")
diabetic_option = ctk.CTkOptionMenu(row3, variable=diabetic_var, values=["No", "No, borderline diabetes", "Yes", "Yes (during pregnancy)"])
diabetic_option.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

phys_activity_label = ctk.CTkLabel(row3, text="Physically Active:", font=("Arial", 16))
phys_activity_label.grid(row=0, column=2, sticky="w", padx=(0, 2), pady=(0, 2))
phys_activity_var = ctk.StringVar(value="Y/N")
phys_activity_option = ctk.CTkOptionMenu(row3, variable=phys_activity_var, values=["Yes", "No"])
phys_activity_option.grid(row=1, column=2, padx=(0, 10), pady=(0, 10))

gen_health_label = ctk.CTkLabel(row3, text="General Health:", font=("Arial", 16))
gen_health_label.grid(row=0, column=3, sticky="w", padx=(0, 2), pady=(0, 2))
gen_health_var = ctk.StringVar(value="Select")
gen_health_option = ctk.CTkOptionMenu(row3, variable=gen_health_var, values=["Poor", "Fair", "Good", "Very good", "Excellent"])
gen_health_option.grid(row=1, column=3, padx=(0, 10), pady=(0, 10))

# Fourth row: Sleep Time, Asthma, Kidney Disease, Skin Cancer
sleep_label = ctk.CTkLabel(row4, text="Sleep Time (hours/night):    ", font=("Arial", 16))
sleep_label.grid(row=0, column=0, sticky="w", padx=(0, 2), pady=(0, 2))
sleep_entry = ctk.CTkEntry(row4, placeholder_text="Enter hours", validate="key", validatecommand=(vcmd_sleep, '%P'))
sleep_entry.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

asthma_label = ctk.CTkLabel(row4, text="Asthma:", font=("Arial", 16))
asthma_label.grid(row=0, column=1, sticky="w", padx=(0, 2), pady=(0, 2))
asthma_var = ctk.StringVar(value="Y/N")
asthma_option = ctk.CTkOptionMenu(row4, variable=asthma_var, values=["Yes", "No"])
asthma_option.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

kidney_label = ctk.CTkLabel(row4, text="Kidney Disease:", font=("Arial", 16))
kidney_label.grid(row=0, column=2, sticky="w", padx=(0, 2), pady=(0, 2))
kidney_var = ctk.StringVar(value="Y/N")
kidney_option = ctk.CTkOptionMenu(row4, variable=kidney_var, values=["Yes", "No"])
kidney_option.grid(row=1, column=2, padx=(0, 10), pady=(0, 10))

skin_cancer_label = ctk.CTkLabel(row4, text="Skin Cancer:", font=("Arial", 16))
skin_cancer_label.grid(row=0, column=3, sticky="w", padx=(0, 2), pady=(0, 2))
skin_cancer_var = ctk.StringVar(value="Y/N")
skin_cancer_option = ctk.CTkOptionMenu(row4, variable=skin_cancer_var, values=["Yes", "No"])
skin_cancer_option.grid(row=1, column=3, padx=(0, 10), pady=(0, 10))




# --- Submit button callback ---
def on_submit():

	# Collect user input from GUI
	# Validate required fields (all except mental and physical health days)
	age_val = age_entry.get()
	try:
		age_int = int(age_val)
		if not (18 <= age_int <= 100):
			raise ValueError()
	except ValueError:
		percentage_label.configure(text="Enter valid age (18-100)", text_color="#FFD600")
		return

	if not bmi_entry.get() or gender_var.get() not in ["Male", "Female"] \
		or any(v.get() not in ["Yes", "No"] for v in [smoking_var, alcohol_var, stroke_var, walk_var, phys_activity_var, asthma_var, kidney_var, skin_cancer_var]) \
		or race_var.get() == "Select" or diabetic_var.get() == "Select" or gen_health_var.get() == "Select" \
		or not sleep_entry.get():
		percentage_label.configure(text="Please fill out all fields.", text_color="#FFD600")
		return

	def get_age_category(age):
		if age <= 24:
			return "18-24"
		elif age <= 29:
			return "25-29"
		elif age <= 34:
			return "30-34"
		elif age <= 39:
			return "35-39"
		elif age <= 44:
			return "40-44"
		elif age <= 49:
			return "45-49"
		elif age <= 54:
			return "50-54"
		elif age <= 59:
			return "55-59"
		elif age <= 64:
			return "60-64"
		elif age <= 69:
			return "65-69"
		elif age <= 74:
			return "70-74"
		elif age <= 79:
			return "75-79"
		else:
			return "80 or older"

	user_input = {
		"BMI": float(bmi_entry.get()),
		"Smoking": smoking_var.get(),
		"AlcoholDrinking": alcohol_var.get(),
		"Stroke": stroke_var.get(),
		"PhysicalHealth": int(phys_entry.get()) if phys_entry.get() else 0,
		"MentalHealth": int(mental_entry.get()) if mental_entry.get() else 0,
		"DiffWalking": walk_var.get(),
		"Sex": gender_var.get(),
		"AgeCategory": get_age_category(age_int),
		"Race": race_var.get(),
		"Diabetic": diabetic_var.get(),
		"PhysicalActivity": phys_activity_var.get(),
		"GenHealth": gen_health_var.get(),
		"SleepTime": int(sleep_entry.get()),
		"Asthma": asthma_var.get(),
		"KidneyDisease": kidney_var.get(),
		"SkinCancer": skin_cancer_var.get(),
	}
	def flash_label():
		# Fade out
		percentage_label.configure(text="Processing...", text_color="#FFD600")
		percentage_label.update()
		app.after(300, show_prediction)

	def show_prediction():
		try:
			result = predict_heart_disease(user_input)
			if result == 1:
				percentage_label.configure(text="Prediction: Yes", text_color="#FF3333")  # Red
			else:
				percentage_label.configure(text="Prediction: No", text_color="#33CC33")   # Green
		except Exception as e:
			percentage_label.configure(text=f"Error: {e}", text_color="#FFD600")

	flash_label()

submit_button = ctk.CTkButton(center_container, text="Submit", font=("Arial", 18, "bold"), fg_color="#FFD600", text_color="#23272e", hover_color="#FFE066", corner_radius=8, height=40, width=200, command=on_submit)
submit_button.pack(pady=(30, 0))



app.mainloop()


