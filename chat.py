import streamlit as st
from streamlit_option_menu import option_menu

from PIL import Image

import google.generativeai as genai 

st.set_page_config(page_title='G60 AI',page_icon="🤖")

with st.sidebar:
  selected = option_menu("G60 AI",["Ask me anything","image description"],menu_icon='robot',icons =['chat-dots-fill','images'])




#setting logo
st.logo("Untitled.png",link="https://srng60.rf.gd/")

genai.configure(api_key="AIzaSyADkPW1r_bkHcurSG5fYkC_LOcE2GUasLI")


model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(inp):
  response=model.generate_content(inp)
  return response.text

if selected == "Ask me anything":
  inp=st.text_input("Ask Sri",key="inp")
 

  try:
    bt=st.button("Generate")
    if bt:
      response1=get_gemini_response(inp)
      st.write(response1)
  except:
    st.write("Enter prompt")

#image content with input

def get_image_response(input,image):
  model1 = genai.GenerativeModel("gemini-1.5-flash")
  ans = model1.generate_content([input,image])
  return ans.text

#image description content
def get_image_description_response(input,image):
  model1 = genai.GenerativeModel("gemini-1.5-flash")
  description_response = model1.generate_content([input,image])
  return description_response.text

#input="write 3 caption for the image"
if selected == "image description":
  st.title("📷 Get your image description")
  user_input=st.text_input("Ask Sri")
  default_input="write  caption for social media post"
  photo=st.file_uploader("Upload image:",type=['jpeg','jpg','png'])
  col1, col2 = st.columns(2)

  if st.button("Generate Description"):
    if photo and user_input!="" :
      image= Image.open(photo)
      resized_image = image.resize((300,300))
      st.image(resized_image)
      response2 = get_image_description_response(user_input,image)
      st.info(response2)
