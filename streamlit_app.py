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
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600;700&family=Cairo:wght@400;700&display=swap');
    
    /* خلفية iOS 26 الديناميكية */
    .stApp {{
        background: linear-gradient(135deg, #1a1f35 0%, #0b0f1a 50%, #1a1530 100%);
        background-attachment: fixed;
        font-family: 'SF Pro Display', 'Cairo', sans-serif;
    }}

    /* إخفاء كل عناصر Streamlit الافتراضية تماماً */
    #MainMenu, footer, header, .stDeployButton, .stAppToolbar, .stActionButton, 
    .st-emotion-cache-1dp5vir, .st-emotion-cache-15ecox0, .st-emotion-cache-1wbqy5l,
    .st-emotion-cache-1avcm0n, .st-emotion-cache-18ni7ap {{
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
        border: 3px solid rgba(255, 215, 0, 0.4);
        object-fit: cover;
        box-shadow: 0 10px 40px rgba(255, 215, 0, 0.3);
    }}

    /* العنوان الرئيسي - ذهبي */
    .main-title {{
        font-size: 3rem;
        font-weight: 700;
        color: #FFD700;
        margin-bottom: 5px;
        letter-spacing: -1px;
        text-align: center;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
    }}
    
    /* الحاوية الزجاجية للجملة */
    .glass-quote-container {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(25px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 50px;
        padding: 25px 30px;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 215, 0, 0.1);
        margin: 30px auto 40px auto;
        width: 90%;
        max-width: 750px;
    }}
    
    /* تنسيق الجملة داخل الحاوية الزجاجية - أبيض ناصع */
    .quote-text {{
        color: #FFFFFF;  /* أبيض ناصع */
        font-size: 1.6rem;
        font-weight: 600;  /* زيادة سمك الخط */
        margin: 0;
        line-height: 1.5;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);  /* ظل خفيف للوضوح */
        letter-spacing: 0.5px;
    }}

    /* تحسين شكل المدخلات */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {{
        background: rgba(255, 255, 255, 0.07) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        color: white !important;
        height: 55px !important;
        direction: rtl !important;
        text-align: right !important;
        font-size: 1rem !important;
        padding: 0 20px !important;
    }}
    
    .stTextInput input:focus, .stSelectbox [data-baseweb="select"]:focus {{
        border-color: #FFD700 !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3) !important;
    }}
    
    /* تنسيق الـ select box */
    .stSelectbox [data-baseweb="select"] > div {{
        background: transparent !important;
        color: white !important;
    }}
    
    /* تنسيق القائمة المنسدلة */
    .stSelectbox [data-baseweb="popover"] {{
        background: rgba(10, 15, 30, 0.95) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 20px !important;
    }}
    
    .stSelectbox [data-baseweb="popover"] li {{
        color: white !important;
        background: transparent !important;
        font-size: 1rem !important;
        padding: 12px 20px !important;
    }}
    
    .stSelectbox [data-baseweb="popover"] li:hover {{
        background: rgba(255, 215, 0, 0.2) !important;
        color: #FFD700 !important;
    }}

    /* زر التشغيل - ذهبي متطور */
    .stButton>button {{
        background: linear-gradient(135deg, #FFD700, #FFA500, #FFD700) !important;
        background-size: 200% 200% !important;
        color: #000 !important;
        border-radius: 25px !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        height: 60px !important;
        width: 100% !important;
        border: none !important;
        margin-top: 25px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-shadow: 0 1px 3px rgba(255, 255, 255, 0.3) !important;
        letter-spacing: 1px !important;
    }}
    .stButton>button:hover {{
        transform: scale(0.97);
        background: linear-gradient(135deg, #FFA500, #FFD700, #FFA500) !important;
        background-size: 200% 200% !important;
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.6) !important;
    }}
    
    /* تنسيق رسائل النجاح والخطأ */
    .stAlert {{
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 20px !important;
        color: white !important;
        font-weight: 500 !important;
        text-align: center !important;
    }}
    
    .stSuccess {{
        background: rgba(255, 215, 0, 0.15) !important;
        border-color: #FFD700 !important;
    }}
    
    /* تنسيق الـ spinner */
    .stSpinner > div {{
        border-color: #FFD700 transparent transparent transparent !important;
    }}
    
    /* إخفاء أي رسائل افتراضية */
    .st-emotion-cache-1y4p8pa {{
        display: none !important;
    }}
    
    /* تنسيق الفوتر */
    .footer-text {{
        text-align: center;
        color: rgba(255, 215, 0, 0.6);
        font-size: 1rem;
        margin-top: 50px;
        font-weight: 500;
        letter-spacing: 1.5px;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- الهيكل البصري الجديد ---

# 1. الصورة في المنتصف
if img_base:
    st.markdown(f'<div class="profile-container"><img src="data:image/png;base64,{img_base}" class="hero-img"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="profile-container"><div class="hero-img" style="background:linear-gradient(135deg, #FFD700, #FFA500);"></div></div>', unsafe_allow_html=True)

# 2. العنوان الرئيسي (ذهبي)
st.markdown('<h1 class="main-title">Doser || Abdelrahman</h1>', unsafe_allow_html=True)

# 3. الحاوية الزجاجية للجملة (النص الآن أبيض ناصع)
st.markdown("""
    <div class="glass-quote-container">
        <div class="quote-text">الهندسة الذكية لخدمات الرشق المتطورة</div>
    </div>
""", unsafe_allow_html=True)

# 4. الحقول والزر
col_input = st.columns([0.1, 0.8, 0.1])[1]
with col_input:
    service = st.selectbox("", ["✨ إعجابات يوتيوب", "✨ إعجابات تيك توك", "✨ حفظ إنستغرام", "✨ مشاهدات تيك توك"], label_visibility="collapsed")
    st.write("")
    url_input = st.text_input("", placeholder="أدخل الرابط هنا...", label_visibility="collapsed")
    
    # 5. زر التنفيذ
    execute_btn = st.button("⚡ تفعيل الخدمة الآن ⚡")

# --- Logic (الباك إند) ---
def process_request(url, link):
    with st.spinner("⚙️ جاري المعالجة بنظام Doser..."):
        sleep(2)
        random_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        # هنا تضع كود الـ requests الفعلي
        st.success(f"✅ تم الإرسال بنجاح | IP: {random_ip}")
        st.balloons()

if execute_btn:
    if url_input:
        process_request(service, url_input)
    else:
        st.error("❌ يرجى إدخال الرابط أولاً")

# --- Footer ---
st.markdown('<p class="footer-text">تم التطوير بواسطة Doser || Abdelrahman ✦ 2026</p>', unsafe_allow_html=True)
