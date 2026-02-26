import streamlit as st
import requests
import random
import base64
from user_agent import generate_user_agent
from time import sleep

# --- وظيفة معالجة الصورة البرمجية ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Doser || TikTok", page_icon="⚔️", layout="centered")

img_base = get_base64_image("icon.png")

# --- CSS: هندسة تصميم iOS 26 (Glassmorphism & Soft Gradients) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&family=Cairo:wght@700&display=swap');
    
    /* خلفية iOS 26 الديناميكية */
    .stApp {{
        background: linear-gradient(135deg, #1e2a4a 0%, #0f172a 50%, #1e1b4b 100%);
        background-attachment: fixed;
        font-family: 'SF Pro Display', 'Cairo', sans-serif;
    }}

    /* الحاوية الزجاجية الرئيسية */
    .ios-glass-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 40px;
        padding: 40px 20px;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
    }}

    /* تنسيق الصورة الشخصية - حجم كبير وتوسط مطلق */
    .profile-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 25px;
    }}
    .hero-img {{
        width: 200px;
        height: 200px;
        border-radius: 35%; /* شكل iOS Squircle */
        border: 2px solid rgba(255, 255, 255, 0.2);
        object-fit: cover;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }}

    /* نصوص iOS */
    .main-title {{
        font-size: 2.8rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }}
    .ios-subtitle {{
        color: rgba(255, 255, 255, 0.7);
        font-size: 1.1rem;
        font-weight: 400;
        background: rgba(255, 255, 255, 0.1);
        padding: 8px 20px;
        border-radius: 50px;
        display: inline-block;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}

    /* تحسين شكل المدخلات لتطابق نظام iOS */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        height: 50px !important;
    }}

    /* زر التشغيل - iOS Style */
    .stButton>button {{
        background: rgba(255, 255, 255, 0.95) !important;
        color: #000 !important;
        border-radius: 18px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        height: 55px !important;
        width: 100% !important;
        border: none !important;
        margin-top: 20px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}
    .stButton>button:hover {{
        transform: scale(0.98);
        background: #ffffff !important;
        box-shadow: 0 0 20px rgba(255,255,255,0.2) !important;
    }}

    /* إخفاء الزوائد */
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- الهيكل البصري للهندسة الذكية ---
st.markdown('<div class="ios-glass-card">', unsafe_allow_html=True)

# 1. الصورة في المنتصف
if img_base:
    st.markdown(f'<div class="profile-container"><img src="data:image/png;base64,{img_base}" class="hero-img"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="profile-container"><div class="hero-img" style="background:gray;"></div></div>', unsafe_allow_html=True)

# 2. العنوان
st.markdown('<h1 class="main-title">Doser || Abdelrahman</h1>', unsafe_allow_html=True)

# 3. الجملة المطلوبة داخل الـ Container الزجاجي بشكل أنيق
st.markdown('<div class="ios-subtitle">الهندسة الذكية لخدمات الرشق المتطورة</div>', unsafe_allow_html=True)

# 4. الحقول (توسيط المحتوى الداخلي)
col_input = st.columns([0.1, 0.8, 0.1])[1]
with col_input:
    service = st.selectbox("", ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"], label_visibility="collapsed")
    st.write("")
    url_input = st.text_input("", placeholder="أدخل الرابط هنا...", label_visibility="collapsed")
    
    # 5. زر التنفيذ
    execute_btn = st.button("تفعيل الخدمة الآن")

st.markdown('</div>', unsafe_allow_html=True) # نهاية الكارت الزجاجي

# --- Logic (الباك إند) ---
def process_request(url, link):
    with st.spinner("جاري المعالجة بنظام  Doser..."):
        sleep(2)
        random_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        # هنا تضع كود الـ requests الفعلي كما في النسخ السابقة
        st.success(f"✅ تم الإرسال بنجاح | IP: {random_ip}")
        st.balloons()

if execute_btn:
    if url_input:
        process_request(service, url_input)
    else:
        st.error("يرجى إدخال الرابط أولاً")

# --- Footer Meta ---
st.markdown('<p style="text-align:center; color:rgba(255,255,255,0.3); font-size:0.8rem; margin-top:30px;">Architecture: iOS 26 Glass Engine | 2026</p>', unsafe_allow_html=True)
