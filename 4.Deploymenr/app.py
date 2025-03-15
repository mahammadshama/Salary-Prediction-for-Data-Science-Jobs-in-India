import os
os.environ["SOLARA_ASSETS_PROXY"] = "false"
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
import solara
import pandas as pd
import joblib

# Load trained stacking model
model = joblib.load("stacking_model.pkl")  # Ensure your trained model file exists

# *Dropdown Mappings (Same as Model Training)*
role_mapping = {
    'Data Scientist Associate' : 0, 'Junior Data Scientist' : 1,
       'Data Scientist' : 2, 'Machine Learning Engineer' : 3,
       'Artificial Intelligence Engineer' : 4, 'Senior Data Scientist' : 5,
       'Lead Data Scientist' : 6, 'Principal Data Scientist' : 7,
       'Data Science Manager' : 8, 'Data Science Analyst' : 9, 'Data Analyst' : 10,
       'Lead Data Analyst' : 11, 'Senior Data Analyst' : 12, 'Data Engineer' : 13,
       'Lead Data Engineer' : 14, 'Senior Data Engineer' : 15
}

company_mapping = {'Product-Based' : 0, 'Service-Based' : 1, 'Other' : 2, 'Mid-Size' : 3, 'MNC' : 4,
       'Startup' : 5}
city_mapping = {'Metro' : 0, 'Non-Metro' : 1}
location_mapping = {'Bengaluru':0, 'Hyderabad':1, 'Not Applicable':2, 'Kolkata':3, 'Mumbai':4, 'Noida':5,
       'Chennai':6, 'Gurugram':7, 'Kochi':8, 'Pune':9, 'Other':10, 'Navi Mumbai':11,
       'Ahmedabad':12, 'New Delhi':13, 'Indore':14, 'Jaipur':15}
job_mapping = {'Onsite':0, 'Hybrid':1, 'Remote':2}
salary_category_mapping = {'Medium': 0, 'High' : 1, 'Low' : 2, 'Very High' : 3}
region_mapping = {'South' : 0, 'Not Applicable' : 1, 'East' : 2, 'West' : 3, 'North' : 4, 'Other' : 5,
       'Central' : 6}
joblevel_mapping = {'Junior' : 0, 'Mid' : 1, 'Senior' : 2, 'Lead' : 3, 'Principal' : 4, 'Manager' : 5}
explevel_mapping = {'Junior' : 0, 'Mid' : 1, 'Senior' : 2, 'Entry' : 3, 'Expert' : 4, 'nan' : 5}




# *UI Elements (Reactive Inputs)*
experience = solara.reactive("0")
job_role = solara.reactive("Data Scientist")
company_type = solara.reactive("MNC")
location = solara.reactive("Hyderabad")
job_mode = solara.reactive("Onsite")

# Dropdown options
job_roles = list(role_mapping.keys())
company_types = list(company_mapping.keys())
locations = list(location_mapping.keys())
job_modes = list(job_mapping.keys())

# *Prediction result (Reactive)*
prediction_result = solara.reactive("")

# *Preprocess Input*
def preprocess_input():
    try:
        exp = float(experience.value)  # Convert experience to float
    except ValueError:
        prediction_result.value = "⚠ Please enter a valid number for experience."
        return None  # Stop if input is invalid

    data = {
        "role": role_mapping.get(job_role.value, -1),
        "company_type": company_mapping.get(company_type.value, -1),
        "Avg_Experience": exp,
        "primary_location": location_mapping.get(location.value, -1),
        "Job_Mode": job_mapping.get(job_mode.value, -1),
        "salary_category":0,
        "City_Type":0,
        "Region":0,
        "experience_level":0,
        "job_level":0,

    }
    return pd.DataFrame([data])

# Predict Salary with Range
def predict():
    input_data = preprocess_input()
    if input_data is not None:
        predicted_salary = model.predict(input_data)[0]  # Predict salary
        lower_bound = max(predicted_salary - 2, 0)  # Ensure non-negative salary
        upper_bound = predicted_salary + 2  # Adding a small range
        prediction_result.value = f"💰 Estimated Salary Range: {lower_bound:,.2f} Lacs - {upper_bound:,.2f} Lacs per Annum"


# *UI Layout*
@solara.component
def Page():
    solara.Markdown(
        "# 🚀 Salary Prediction App",
        style="font-size: 36px; font-weight: bold; text-align: center; color: #2c3e50; padding: 15px; background-color: #f1f1f1; border-radius: 10px; width: 80%; margin: auto;"
    )

    with solara.Row(justify="center", style="margin-top: 20px;"):
        with solara.Card(
            style="padding: 30px; width: 80%; max-width: 700px; box-shadow: 5px 5px 20px rgba(0,0,0,0.3); border-radius: 12px; text-align: center;"
        ):
            solara.Markdown("## 🎯 Enter Your Details", style="color: #16a085; font-weight: bold; text-align: center; font-size: 24px;")

            solara.InputText(label="🛠 *Years of Experience*", value=experience, style="margin-bottom: 15px; font-size: 16px; width: 100%;")
            solara.Select("🧑‍💻 *Job Role*", job_roles, job_role, style="margin-bottom: 15px; font-size: 16px; width: 100%;")
            solara.Select("🏢 *Company Type*", company_types, company_type, style="margin-bottom: 15px; font-size: 16px; width: 100%;")
            solara.Select("📍 *Location*", locations, location, style="margin-bottom: 15px; font-size: 16px; width: 100%;")
            solara.Select("💼 *Job Mode*", job_modes, job_mode, style="margin-bottom: 15px; font-size: 16px; width: 100%;")

            solara.Button(
                "💰 Predict Salary",
                on_click=predict,
                style="background-color: #e67e22; color: white; font-size: 20px; font-weight: bold; border-radius: 5px; width: 100%; padding: 12px;"
            )

    with solara.Row(justify="center", style="margin-top: 30px;"):
        with solara.Card(
            style="padding: 20px; width: 80%; max-width: 600px; border-radius: 10px; background-color: #f9ebea; text-align: center; box-shadow: 3px 3px 15px rgba(0,0,0,0.2);"
        ):
            solara.Markdown(
                f"## {prediction_result.value}",
                style="text-align: center; color: #c0392b; font-weight: bold; font-size: 24px;"
            )