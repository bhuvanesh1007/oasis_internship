!pip install ipywidgets

from ipywidgets import interact, FloatText, Button, Output, VBox

def calculate_bmi_and_category(weight, height):
    """Calculate BMI given weight (in kilograms) and height (in meters)"""
    bmi = weight / (height ** 2)
    bmi_category = get_bmi_category(bmi)
    return bmi, bmi_category

def get_bmi_category(bmi):
    """Determine BMI category given BMI value"""
    if bmi < 18.5:
        return "You are underweight"
    elif bmi < 25:
        return "You have a normal healthy weight"
    elif bmi < 30:
        return "You are overweight"
    elif bmi < 35:
        return "You have obesity"
    else:
        return "You have severe obesity"

weight_input = FloatText(value=70, description='Enter your weight (kg):')
height_input = FloatText(value=1.75, description='Enter your height (m):')
calculate_button = Button(description='Calculate BMI')
output_bmi = Output()
output_category = Output()

def update_bmi_category(weight, height):
    bmi, category = calculate_bmi_and_category(weight, height)
    with output_bmi:
        output_bmi.clear_output()
        print(f"Your BMI is: {bmi:.2f}")
    with output_category:
        output_category.clear_output()
        print(f"{category}")

calculate_button.on_click(lambda b: update_bmi_category(weight_input.value, height_input.value))

VBox([weight_input, height_input, calculate_button, output_bmi, output_category])
