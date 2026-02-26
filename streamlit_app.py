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

    /* تنسيق الصورة الشخصية - حجم كبير وتوسط مطلق */
    .profile-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px; /* تقليل المسافة قليلاً */
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
        /* تم تغيير اللون هنا إلى الأزرق الفاتح */
        color: #7ab2ff; 
        margin-bottom: 5px;
        letter-spacing: -1px;
        text-align: center;
    }}
    
    /* --- الحاوية الزجاجية الجديدة (الشفافة) للجملة فقط --- */
    .glass-quote-container {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 40px;
        padding: 20px 25px; /* حشوة داخلية مناسبة */
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        margin: 25px auto 35px auto; /* توسيط أفقي مع مسافة خارجية */
        width: 90%; /* عرض مناسب */
        max-width: 700px; /* أقصى عرض */
    }}
    
    /* تنسيق الجملة داخل الحاوية الزجاجية */
    .quote-text {{
        color: rgba(255, 255, 255, 0.85);
        font-size: 1.4rem; /* حجم خط مناسب */
        font-weight: 400;
        margin: 0;
        line-height: 1.5;
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

# --- الهيكل البصري الجديد ---

# 1. الصورة في المنتصف (خارج أي container شفاف)
if img_base:
    st.markdown(f'<div class="profile-container"><img src="data:image/png;base64,{img_base}" class="hero-img"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="profile-container"><div class="hero-img" style="background:gray;"></div></div>', unsafe_allow_html=True)

# 2. العنوان (تحت الصورة، خارج الحاوية الشفافة)
st.markdown('<h1 class="main-title">Doser || Abdelrahman</h1>', unsafe_allow_html=True)

# 3. الحاوية الزجاجية (الشفافة) التي تحتوي على الجملة فقط
st.markdown("""
    <div class="glass-quote-container">
        <div class="quote-text">الهندسة الذكية لخدمات الرشق المتطورة</div>
    </div>
""", unsafe_allow_html=True)

# 4. الحقول والزر (باقي المحتوى)
col_input = st.columns([0.1, 0.8, 0.1])[1]
with col_input:
    service = st.selectbox("", ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"], label_visibility="collapsed")
    st.write("")
    url_input = st.text_input("", placeholder="أدخل الرابط هنا...", label_visibility="collapsed")
    
    # 5. زر التنفيذ
    execute_btn = st.button("تفعيل الخدمة الآن")

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

# --- Footer Meta (تم التعديل) ---
st.markdown('<p style="text-align:center; color:rgba(255,255,255,0.3); font-size:0.8rem; margin-top:30px;">تم التطوير بواسطه Doser || Abdelrahman</p>', unsafe_allow_html=True)
