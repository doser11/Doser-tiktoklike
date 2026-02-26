import streamlit as st
import requests
import random
import base64
from user_agent import generate_user_agent
from time import sleep

# --- معالجة الصورة ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

st.set_page_config(page_title="Doser || Abdelrahman", layout="centered")

img_base = get_base64_image("icon.png")

# --- CSS: تصميم iOS 26 الاحترافي ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {{
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        font-family: 'Cairo', sans-serif;
    }}

    /* تنسيق الصورة - في المنتصف تماماً فوق الكونتينة */
    .img-container {{
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: -50px; /* تداخل بسيط ليعطي شكل هندسي */
        position: relative;
        z-index: 10;
    }}
    .hero-img {{
        width: 220px;
        height: 220px;
        border-radius: 50px; /* iOS Squircle */
        border: 5px solid rgba(255, 255, 255, 0.1);
        object-fit: cover;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }}

    /* الـ Container الزجاجي الكبير (تحت الصورة) */
    .ios-card {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 40px;
        padding: 70px 30px 40px 30px; /* حشوة علوية كبيرة بسبب تداخل الصورة */
        text-align: center;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        width: 100%;
    }}

    /* لون الاسم الجديد */
    .doser-name {{
        font-size: 2.5rem;
        font-weight: 900;
        color: #00d4ff; /* لون سماوي احترافي متوهج */
        margin-bottom: 5px;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
    }}

    /* الجملة داخل الكونتينة */
    .smart-eng {{
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 400;
        opacity: 0.9;
        margin-bottom: 30px;
    }}

    /* تنسيق المدخلات */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {{
        background: rgba(0, 0, 0, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 15px !important;
    }}

    /* الزر الرئيسي */
    .stButton>button {{
        background: #ffffff !important;
        color: #000 !important;
        font-weight: 700 !important;
        border-radius: 20px !important;
        height: 60px !important;
        width: 100% !important;
        border: none !important;
        transition: 0.3s ease;
    }}
    .stButton>button:hover {{
        transform: scale(0.97);
        opacity: 0.9;
    }}

    /* إخفاء الهيدر والفوتر الخاص بـ streamlit */
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- الهيكل البصري ---

# 1. الصورة في الأعلى حرة
st.markdown(f"""
    <div class="img-container">
        <img src="data:image/png;base64,{img_base if img_base else ''}" class="hero-img">
    </div>
    """, unsafe_allow_html=True)

# 2. الـ Container الزجاجي (تحت الصورة)
st.markdown('<div class="ios-card">', unsafe_allow_html=True)

st.markdown('<div class="doser-name">Doser || Abdelrahman</div>', unsafe_allow_html=True)
st.markdown('<div class="smart-eng">الهندسة الذكية لخدمات الرشق المتطورة</div>', unsafe_allow_html=True)

# عناصر التحكم
col_in = st.columns([0.05, 0.9, 0.05])[1]
with col_in:
    option = st.selectbox("", ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"], label_visibility="collapsed")
    v_url = st.text_input("", placeholder="ضع الرابط هنا...", label_visibility="collapsed")
    st.write("")
    if st.button("🚀 بدأ التنفيذ"):
        if v_url:
            with st.spinner("جاري المعالجة..."):
                sleep(2)
                st.success("تمت العملية بنجاح!")
                st.balloons()
        else:
            st.error("أدخل الرابط!")

st.markdown('</div>', unsafe_allow_html=True) # نهاية الـ ios-card

# --- التذييل الجديد ---
st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: rgba(255,255,255,0.4);">
        تم التطوير بواسطه Doser || Abdelrahman
    </div>
    """, unsafe_allow_html=True)
