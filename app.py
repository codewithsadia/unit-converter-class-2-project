import streamlit as st # type: ignore
import random
from datetime import datetime

# Page configuration and styling
st.set_page_config(page_title="Enhanced Unit Converter", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stSelectbox {
        border-radius: 10px;
    }
    .success-message {
        padding: 20px;
        border-radius: 10px;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    </style>
    """, unsafe_allow_html=True)

def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701,
        'nanometers': 1e9,  # Added new units
        'micrometers': 1e6,
        'light years': 1.057e-16
    }
    value_in_meters = value / length_units[from_unit]
    return value_in_meters * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'milligrams': 1000000,
        'pounds': 2.20462,
        'ounces': 35.274,
        'metric tons': 0.001,  # Added new units
        'stone': 0.157473,
        'grains': 15432.4
    }
    value_in_kg = value / weight_units[from_unit]
    return value_in_kg * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def get_chatbot_response(query):
    # Simple chatbot responses
    responses = {
        "hello": "Hi! How can I help you with unit conversion today?",
        "help": "I can help you convert between different units of length, weight, and temperature. Just select the conversion type and units!",
        "thank": "You're welcome! Let me know if you need any other help.",
        "bye": "Goodbye! Come back anytime for more conversions!",
    }
    
    query = query.lower()
    for key in responses:
        if key in query:
            return responses[key]
    return "I'm here to help with unit conversions. Try asking about length, weight, or temperature conversions!"

def main():
    # Header with gradient background
    st.markdown("""
        <div style='background: linear-gradient(45deg, #1e88e5, #1565c0); padding: 20px; border-radius: 15px;'>
            <h1 style='color: white; text-align: center;'>✨ Enhanced Unit Converter ✨</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar with gradient background
    with st.sidebar:
        st.markdown("""
            <div style='background: linear-gradient(45deg, #43a047, #2e7d32); padding: 10px; border-radius: 10px;'>
                <h2 style='color: white; text-align: center;'>Settings</h2>
            </div>
        """, unsafe_allow_html=True)
        
        conversion_type = st.selectbox(
            "Choose conversion type",
            ["Length", "Weight", "Temperature"]
        )

    # Main conversion interface
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
                <h3 style='color: #1565c0;'>Convert Units</h3>
            </div>
        """, unsafe_allow_html=True)
        
        value = st.number_input("Enter value to convert", value=0.0)
        
        if conversion_type == "Length":
            units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches", 
                    "nanometers", "micrometers", "light years"]
            from_unit = st.selectbox("From", units)
            to_unit = st.selectbox("To", units)
            
            if st.button("Convert!", key="length"):
                result = length_converter(value, from_unit, to_unit)
                st.balloons()  # Celebration effect
                st.markdown(f"""
                    <div class='success-message'>
                        <h3>🎉 Result:</h3>
                        <p>{value} {from_unit} = {result:.4f} {to_unit}</p>
                    </div>
                """, unsafe_allow_html=True)
                
        elif conversion_type == "Weight":
            units = ["kilograms", "grams", "milligrams", "pounds", "ounces", "metric tons", "stone", "grains"]
            from_unit = st.selectbox("From", units)
            to_unit = st.selectbox("To", units)
            
            if st.button("Convert!", key="weight"):
                result = weight_converter(value, from_unit, to_unit)
                st.balloons()  # Celebration effect
                st.markdown(f"""
                    <div class='success-message'>
                        <h3>🎉 Result:</h3>
                        <p>{value} {from_unit} = {result:.4f} {to_unit}</p>
                    </div>
                """, unsafe_allow_html=True)
                
        elif conversion_type == "Temperature":
            units = ["celsius", "fahrenheit", "kelvin"]
            from_unit = st.selectbox("From", units)
            to_unit = st.selectbox("To", units)
            
            if st.button("Convert!", key="temp"):
                result = temp_converter(value, from_unit, to_unit)
                st.balloons()  # Celebration effect
                st.markdown(f"""
                    <div class='success-message'>
                        <h3>🎉 Result:</h3>
                        <p>{value} {from_unit} = {result:.4f} {to_unit}</p>
                    </div>
                """, unsafe_allow_html=True)

    # AI Chatbot interface
    with col2:
        st.markdown("""
            <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
                <h3 style='color: #1565c0;'>AI Conversion Assistant 🤖</h3>
            </div>
        """, unsafe_allow_html=True)
        
        user_input = st.text_input("Ask me anything about unit conversion!", key="chat_input")
        if user_input:
            response = get_chatbot_response(user_input)
            st.markdown(f"""
                <div style='background: #e3f2fd; padding: 15px; border-radius: 10px; margin-top: 10px;'>
                    <p><strong>🤖 Assistant:</strong> {response}</p>
                </div>
            """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background: #f8f9fa; border-radius: 10px;'>
            <p>Made with ❤️ | Current time: {}</p>
        </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

if __name__ == "__main__":
    main()