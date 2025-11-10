# BMI Calculator (Streamlit)

A clean, medical‑styled Streamlit app that calculates **Body Mass Index (BMI)** from height and weight in either metric or imperial units, shows the **BMI category** with color coding, and provides **simple health tips**. Includes an **educational disclaimer**.

## Features
- Professional look with clear title and clinical styling
- Inputs for height (**cm** or **inches**) and weight (**kg** or **lbs**)
- Accurate unit conversion to metric behind the scenes
- BMI value with color‑coded category: **Underweight**, **Normal**, **Overweight**, **Obese**
- Short, practical recommendations aligned with each category
- Expandable “What does this mean?” section for context
- Educational disclaimer (not medical advice)

## Getting Started

### 1) Create & activate a virtual environment (recommended)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the app
```bash
streamlit run app.py
```

The app will open in your browser (typically at `http://localhost:8501`).

## Project Structure
```
app.py
requirements.txt
README.md
```

## Notes & Limitations
- BMI is a **screening** metric and doesn’t account for all individual factors (e.g., body composition, age, sex, ethnicity, and fitness).
- For personal medical guidance, consult your clinician.

## License
MIT
