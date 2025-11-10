import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🏥",
    layout="centered"
)

# Custom CSS for professional medical look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0052a3;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and header
st.markdown("<h1 style='text-align: center; color: #0066cc;'>🏥 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666;'>Body Mass Index Assessment Tool</h3>", unsafe_allow_html=True)
st.markdown("---")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("Height")
    height_unit = st.selectbox("Unit", ["cm", "inches"], key="height_unit")
    height_value = st.number_input(
        f"Enter height ({height_unit})",
        min_value=0.0,
        max_value=300.0 if height_unit == "cm" else 120.0,
        value=170.0 if height_unit == "cm" else 67.0,
        step=0.1
    )

with col2:
    st.subheader("Weight")
    weight_unit = st.selectbox("Unit", ["kg", "lbs"], key="weight_unit")
    weight_value = st.number_input(
        f"Enter weight ({weight_unit})",
        min_value=0.0,
        max_value=500.0 if weight_unit == "kg" else 1100.0,
        value=70.0 if weight_unit == "kg" else 154.0,
        step=0.1
    )

# Convert to metric if necessary
def convert_to_metric(height, height_unit, weight, weight_unit):
    # Convert height to meters
    if height_unit == "inches":
        height_m = height * 0.0254
    else:
        height_m = height / 100
    
    # Convert weight to kg
    if weight_unit == "lbs":
        weight_kg = weight * 0.453592
    else:
        weight_kg = weight
    
    return height_m, weight_kg

# Calculate BMI
def calculate_bmi(height_m, weight_kg):
    if height_m > 0:
        return weight_kg / (height_m ** 2)
    return 0

# Get BMI category and color
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "#3498db", "ℹ️"
    elif 18.5 <= bmi < 25:
        return "Normal Weight", "#27ae60", "✅"
    elif 25 <= bmi < 30:
        return "Overweight", "#f39c12", "⚠️"
    else:
        return "Obese", "#e74c3c", "🔴"

# Get health recommendations
def get_recommendations(category):
    recommendations = {
        "Underweight": [
            "Consult with a healthcare provider or registered dietitian",
            "Focus on nutrient-dense, calorie-rich foods",
            "Consider strength training to build muscle mass",
            "Ensure adequate protein intake in your diet"
        ],
        "Normal Weight": [
            "Maintain your current healthy lifestyle",
            "Continue regular physical activity (150 min/week)",
            "Eat a balanced diet with fruits, vegetables, and whole grains",
            "Monitor your weight regularly"
        ],
        "Overweight": [
            "Consult with a healthcare provider for personalized advice",
            "Aim for gradual weight loss (1-2 lbs per week)",
            "Increase physical activity to at least 150-300 min/week",
            "Focus on portion control and reducing processed foods"
        ],
        "Obese": [
            "Schedule an appointment with your healthcare provider",
            "Consider working with a dietitian and fitness professional",
            "Start with small, sustainable lifestyle changes",
            "Focus on both diet modification and regular exercise"
        ]
    }
    return recommendations.get(category, [])

# Calculate button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Calculate BMI"):
    if height_value > 0 and weight_value > 0:
        # Convert to metric
        height_m, weight_kg = convert_to_metric(height_value, height_unit, weight_value, weight_unit)
        
        # Calculate BMI
        bmi = calculate_bmi(height_m, weight_kg)
        
        # Get category and color
        category, color, icon = get_bmi_category(bmi)
        
        # Display results
        st.markdown("---")
        st.markdown("<h2 style='text-align: center;'>Results</h2>", unsafe_allow_html=True)
        
        # BMI value with color
        st.markdown(
            f"<div style='text-align: center; padding: 20px; background-color: {color}; "
            f"border-radius: 10px; margin: 20px 0;'>"
            f"<h1 style='color: white; margin: 0;'>{icon} {bmi:.1f}</h1>"
            f"<h3 style='color: white; margin: 10px 0;'>{category}</h3>"
            f"</div>",
            unsafe_allow_html=True
        )
        
        # BMI Scale Reference
        st.markdown("### 📊 BMI Scale Reference")
        st.markdown("""
        - **Underweight:** BMI < 18.5
        - **Normal Weight:** BMI 18.5 - 24.9
        - **Overweight:** BMI 25 - 29.9
        - **Obese:** BMI ≥ 30
        """)
        
        # Health recommendations
        st.markdown(f"### 💡 Health Recommendations for {category}")
        recommendations = get_recommendations(category)
        for rec in recommendations:
            st.markdown(f"- {rec}")
        
    else:
        st.error("Please enter valid height and weight values.")

# Disclaimer
st.markdown("---")
st.markdown("### ⚠️ Disclaimer")
st.info(
    "**This BMI calculator is for educational purposes only.** "
    "BMI is a screening tool and does not diagnose body fatness or health. "
    "It does not account for factors such as muscle mass, bone density, age, or sex. "
    "Please consult with a qualified healthcare professional for personalized medical advice, "
    "diagnosis, or treatment. Do not disregard professional medical advice or delay seeking it "
    "because of information obtained from this tool."
)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666; font-size: 0.9em;'>"
    "© 2024 BMI Calculator | For Educational Use Only</p>",
    unsafe_allow_html=True
)
