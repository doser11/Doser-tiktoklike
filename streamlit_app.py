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

    /* إخفاء كل عناصر Streamlit الافتراضية تماماً */
    #MainMenu, footer, header, .stDeployButton, .stAppToolbar, .stActionButton, .st-emotion-cache-1dp5vir, .st-emotion-cache-15ecox0, .st-emotion-cache-1wbqy5l {{
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        pointer-events: none !important;
    }}
    
    /* منع ظهور أي عناصر إضافية */
    .st-emotion-cache-1avcm0n, .st-emotion-cache-18ni7ap, .st-emotion-cache-1dp5vir, .st-emotion-cache-15ecox0 {{
        display: none !important;
    }}
    
    /* إخفاء الشريط العلوي */
    .stApp header {{
        display: none !important;
    }}
    
    /* إزالة المساحات الفارغة */
    .main > div {{
        padding-top: 0rem !important;
    }}
    
    /* تنسيق الصورة الشخصية */
    .profile-container {{
        display: flex;
        justify-content: center;
        margin: 20px 0 20px 0;
    }}
    .hero-img {{
        width: 200px;
        height: 200px;
        border-radius: 35%;
        border: 2px solid rgba(255, 215, 0, 0.3);
        object-fit: cover;
        box-shadow: 0 10px 30px rgba(255, 215, 0, 0.2);
    }}

    /* العنوان الرئيسي - اللون الجديد (ذهبي) */
    .main-title {{
        font-size: 2.8rem;
        font-weight: 700;
        color: #FFD700; /* لون ذهبي */
        margin-bottom: 5px;
        letter-spacing: -1px;
        text-align: center;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
    }}
    
    /* الحاوية الزجاجية للجملة */
    .glass-quote-container {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%);
        border: 1px solid rgba(255, 215, 0, 0.2);
        border-radius: 40px;
        padding: 20px 25px;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        margin: 25px auto 35px auto;
        width: 90%;
        max-width: 700px;
    }}
    
    /* تنسيق الجملة داخل الحاوية الزجاجية */
    .quote-text {{
        color: rgba(255, 255, 255, 0.85);
        font-size: 1.4rem;
        font-weight: 400;
        margin: 0;
        line-height: 1.5;
    }}

    /* تحسين شكل المدخلات */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 215, 0, 0.2) !important;
        color: white !important;
        height: 50px !important;
        direction: rtl !important;
        text-align: right !important;
    }}
    
    /* تنسيق الـ select box */
    .stSelectbox [data-baseweb="select"] > div {{
        background: transparent !important;
        color: white !important;
    }}
    
    /* تنسيق القائمة المنسدلة */
    .stSelectbox [data-baseweb="popover"] {{
        background: rgba(15, 23, 42, 0.95) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 215, 0, 0.2) !important;
        border-radius: 15px !important;
    }}
    
    .stSelectbox [data-baseweb="popover"] li {{
        color: white !important;
        background: transparent !important;
    }}
    
    .stSelectbox [data-baseweb="popover"] li:hover {{
        background: rgba(255, 215, 0, 0.2) !important;
    }}

    /* زر التشغيل - ذهبي */
    .stButton>button {{
        background: linear-gradient(135deg, #FFD700, #FDB931) !important;
        color: #000 !important;
        border-radius: 18px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        height: 55px !important;
        width: 100% !important;
        border: none !important;
        margin-top: 20px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    }}
    .stButton>button:hover {{
        transform: scale(0.98);
        background: linear-gradient(135deg, #FDB931, #FFD700) !important;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.4) !important;
    }}
    
    /* إخفاء أي رسائل افتراضية */
    .st-emotion-cache-1y4p8pa {{
        display: none !important;
    }}
    
    /* تنسيق الفوتر */
    .footer-text {{
        text-align: center;
        color: rgba(255, 215, 0, 0.5);
        font-size: 0.9rem;
        margin-top: 40px;
        font-weight: 400;
        letter-spacing: 1px;
        text-shadow: 0 0 5px rgba(255, 215, 0, 0.2);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- الهيكل البصري الجديد ---

# 1. الصورة في المنتصف
if img_base:
    st.markdown(f'<div class="profile-container"><img src="data:image/png;base64,{img_base}" class="hero-img"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="profile-container"><div class="hero-img" style="background:gray;"></div></div>', unsafe_allow_html=True)

# 2. العنوان الرئيسي (باللون الذهبي)
st.markdown('<h1 class="main-title">Doser || Abdelrahman</h1>', unsafe_allow_html=True)

# 3. الحاوية الزجاجية للجملة
st.markdown("""
    <div class="glass-quote-container">
        <div class="quote-text">الهندسة الذكية لخدمات الرشق المتطورة</div>
    </div>
""", unsafe_allow_html=True)

# 4. الحقول والزر
col_input = st.columns([0.1, 0.8, 0.1])[1]
with col_input:
    service = st.selectbox("", ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"], label_visibility="collapsed")
    st.write("")
    url_input = st.text_input("", placeholder="أدخل الرابط هنا...", label_visibility="collapsed")
    
    # 5. زر التنفيذ
    execute_btn = st.button("تفعيل الخدمة الآن")

# --- Logic (الباك إند) ---
def process_request(url, link):
    with st.spinner("جاري المعالجة بنظام Doser..."):
        sleep(2)
        random_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        # هنا تضع كود الـ requests الفعلي
        st.success(f"✅ تم الإرسال بنجاح | IP: {random_ip}")
        st.balloons()

if execute_btn:
    if url_input:
        process_request(service, url_input)
    else:
        st.error("يرجى إدخال الرابط أولاً")

# --- Footer ---
st.markdown('<p class="footer-text">تم التطوير بواسطه Doser || Abdelrahman</p>', unsafe_allow_html=True)
