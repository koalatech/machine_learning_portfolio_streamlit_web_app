import streamlit as st


st.header('Image Classification App')
st.subheader('This python code is implemented for Streamlit')
st.code('''
        import pickle
from img2vec_pytorch import Img2Vec
from PIL import Image
import streamlit as st
# from rembg import remove
from PIL import Image
from io import BytesIO
import base64


with open('pages/sky_condition_model.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()



## Streamlit Web App Interface
st.set_page_config(layout="wide", page_title="Image Classification for Weather")

st.write("## Let's try to see what weather is in the image!")
st.write(
    ":grin: We'll try to predict the weather depicted in your uploaded image :grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image
@st.cache_data 
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="jpg")
    byte_im = buf.getvalue()
    return byte_im

@st.cache_data 
def fix_image(upload):
    image = Image.open(upload)
    col1.write("Image to be predicted :camera:")
    col1.image(image)

    # fixed = remove(image)
    col2.write("Category :wrench:")
    # image_path = './example/rain.jpeg'
    img = Image.open(my_upload)
    features = img2vec.get_vec(img)
    pred = model.predict([features])

    # print(pred)
    col2.header(pred)
    # st.sidebar.markdown("\n")
    # st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    st.write("by koalatech...")
    # fix_image("./zebra.jpg")
    ''')
