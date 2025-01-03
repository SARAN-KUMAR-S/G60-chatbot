import streamlit as st
from streamlit_option_menu import option_menu

from PIL import Image

import google.generativeai as genai 

st.set_page_config(page_title='G60 AI',page_icon="🤖")

with st.sidebar:
  selected = option_menu("G60 AI",["Ask me anything","image description","Invoice Extractor"],menu_icon='robot',icons =['chat-dots-fill','images','receipt-cutoff'])




#setting logo with link
#st.logo("Untitled.png",link="https://srng60.rf.gd/")

st.logo("Untitled.png")

genai.configure(api_key="AIzaSyCeS5H2EKIESgk_LrDTs5cpmWGifqUkLyE")


model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(inp):
  response=model.generate_content(inp)
  custom_response = response.text.replace("developed by Google", "developed by G60 SOLUTIONS")
  custom_response = custom_response.replace("I am Gemini", "I am G60 ")
  custom_response = custom_response.replace("trained by Google", "developed by G60 SOLUTIONS")
  custom_response = custom_response.replace("My name is Gemini", "I am G60")

  return custom_response

if selected == "Ask me anything":
  st.title("💬I am here to help you")
  inp=st.text_input("Ask G60 SRii",key="inp")
 

  try:
    bt=st.button("Generate")
    if bt:
        response1=get_gemini_response(inp)
        st.write(response1)
  except:
    st.write("Enter prompt")



#image description content
def get_image_description_response(input,image):
  model1 = genai.GenerativeModel("gemini-1.5-flash")
  description_response = model1.generate_content([input,image])
  return description_response.text

#input="write 3 caption for the image"
if selected == "image description":
  st.title("📷 Snap Narrate")
  user_input2=st.text_input("Ask Sri")
  #default_input="write  caption for social media post"
  photo=st.file_uploader("Upload image:",type=['jpeg','jpg','png'])
  if photo:

    image2= Image.open(photo)
    resized_image = image2.resize((350,350))
    st.image(resized_image,caption="Image uploaded")


  if st.button("Narrate the Snap"):
    if photo and user_input2!="" :
      response2 = get_image_description_response(user_input2,resized_image)
      st.info(response2)
    else:
      st.warning("Give input")


def get_invoice(input3,image3):
  try:
    model3 = genai.GenerativeModel("gemini-1.5-flash")
    description_response3 = model3.generate_content([input3,image3])
    return description_response3.text
  except:
    return "Try different prompt"

#input="write 3 caption for the image"
if selected == "Invoice Extractor":
  st.title("🧾MultiLanguage Invoice Reader")
  user_input3=st.text_input("Ask Questions on Invoice")
  prompt="""
  You are an expert in understanding invoices.we will upload a image as invoice
  and you will have to answer any  questions based on the uploaded invoice, and dont return none return atleast some ans ,the question is:"""
  if user_input3!="":
    prompt = prompt+" "+ str(user_input3)
  #default_input="write  caption for social media post"
  photo=st.file_uploader("Upload image:",type=['jpeg','jpg','png'])
  if photo:
      image3= Image.open(photo)
      #esized_image = image.resize((300,300))
      st.image(image3,caption="Image uploaded",use_column_width=True)

  if st.button("Generate Description"):
    if photo and user_input3!="" :
      #prompt="Now you are an Invoice expert and now you have answer for the query according to the questions i ask from the invoices"
      response2 = get_invoice(prompt,image3)
      st.info(response2)
    else:
      st.warning("Upload Invoice and Ask your Question")

st.sidebar.caption("Developed by Saran Kumar")


#<button kind="headerNoPadding" data-testid="baseButton-headerNoPadding" class="st-emotion-cache-yfhhig ef3psqc5" fdprocessedid="u4xxa9"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" class="eyeqlp53 st-emotion-cache-1pbsqtx ex0cdmw0"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></button>





