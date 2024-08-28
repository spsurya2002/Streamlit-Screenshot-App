import streamlit as st
from PIL import Image, ImageGrab

def take_screenshot():
    screenshot = ImageGrab.grab()  # Take a screenshot of the entire screen
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)  # Save the screenshot
    return screenshot_path
    
if st.button("ss"):
    st.write("Taking screenshot...")
    screenshot_path = take_screenshot()
    image = Image.open(screenshot_path)
    st.image(image, caption='Screenshot', use_column_width=True)
