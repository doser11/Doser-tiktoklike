import streamlit as st
import requests
import random
from user_agent import generate_user_agent
from time import sleep
import os

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Doser | Social Booster",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS لإخفاء العناصر غير المرغوبة وتصغير الهوامش
st.markdown("""
    <style>
    /* إخفاء شعار GitHub */
    .stApp > header {
        display: none !important;
    }
    
    /* إخفاء شريط Streamlit العلوي */
    .stAppDeployButton {
        display: none !important;
    }
    
    /* إخفاء footer الافتراضي */
    footer {
        display: none !important;
    }
    
    /* إخفاء زر القائمة */
    .st-emotion-cache-1avcm0n {
        display: none !important;
    }
    
    /* إزالة الهوامش العلوية */
    .stApp {
        margin-top: -80px !important;
    }
    
    /* تقليل الهوامش العامة */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        max-width: 100% !important;
    }
    
    /* إخفاء أي عناصر إضافية */
    #MainMenu {
        visibility: hidden;
    }
    
    /* تصميم عام */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    * { 
        font-family: 'Tajawal', sans-serif; 
        margin: 0;
        padding: 0;
    }
    
    .stApp { 
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
        min-height: 100vh;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.5); }
        50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.8); }
    }
    
    .logo-container {
        text-align: center;
        margin-bottom: 20px;
    }
    
    .logo-img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 3px solid #00d4ff;
        object-fit: cover;
        animation: float 4s ease-in-out infinite, glow 3s ease-in-out infinite;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.4);
    }
    
    .title-text {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
        letter-spacing: 3px;
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1rem;
        margin-bottom: 30px;
    }
    
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 10px !important;
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 10px !important;
        color: white !important;
        text-align: center;
    }
    
    .stButton > button {
        width: 100%;
        padding: 15px;
        border-radius: 10px;
        background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
        color: white;
        font-weight: bold;
        border: none;
        margin-top: 10px;
        transition: 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0, 212, 255, 0.4);
    }
    
    .custom-footer {
        text-align: center;
        padding: 20px;
        margin-top: 30px;
        border-top: 1px solid rgba(0, 212, 255, 0.2);
        color: #00d4ff;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- التحقق من وجود الصورة ---
if os.path.exists("icon.png"):
    image_path = "icon.png"
else:
    # استخدام صورة افتراضية إذا لم تكن موجودة
    image_path = "https://via.placeholder.com/150/00d4ff/ffffff?text=DOSER"
    st.warning("⚠️ ملف icon.png غير موجود! يرجى إضافة الصورة")

# --- الهيدر ---
st.markdown(f"""
    <div class="logo-container">
        <img src="{image_path}" class="logo-img" alt="Doser">
    </div>
    <h1 class="title-text">DOSER</h1>
    <p class="subtitle">منصة تعزيز الخدمات الاجتماعية</p>
""", unsafe_allow_html=True)

# --- الدوال ---
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def send_request(url, link, quantity=None):
    random_ip = generate_random_ip()
    headers = {
        "User-Agent": generate_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://leofame.com",
        "referer": url.split('?')[0],
        "cookie": "token=FAKETOKEN; cf_clearance=FAKECOOKIE",
        "X-Forwarded-For": random_ip,
        "Client-IP": random_ip
    }
    data = {
        "token": "FAKETOKEN",
        "timezone_offset": "Asia/Baghdad",
        "free_link": link
    }
    if quantity:
        data["quantity"] = quantity
    
    try:
        wait_time = random.randint(3, 7)
        st.info(f"⏳ جاري المعالجة... ({wait_time} ثوانٍ)")
        sleep(wait_time)
        
        r = requests.post(url, headers=headers, data=data)
        
        if "Please wait" in r.text or '"error":' in r.text:
            st.error("⚠️ يوجد تأخير، حاول لاحقاً")
        else:
            st.success(f"✅ تم بنجاح! (IP: {random_ip})")
            
    except Exception as e:
        st.error(f"❌ خطأ: {str(e)}")

# --- الواجهة ---
option = st.selectbox(
    "اختر الخدمة",
    ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"]
)

video_url = st.text_input("🔗 الرابط", placeholder="https://...")

if st.button("🚀 تنفيذ"):
    if video_url:
        endpoints = {
            "إعجابات يوتيوب": ("https://leofame.com/free-youtube-likes?api=1", None),
            "إعجابات تيك توك": ("https://leofame.com/free-tiktok-likes?api=1", None),
            "حفظ إنستغرام": ("https://leofame.com/free-instagram-saves?api=1", "30"),
            "مشاهدات تيك توك": ("https://leofame.com/ar/free-tiktok-views?api=1", "200")
        }
        
        url, qty = endpoints[option]
        send_request(url, video_url, qty)
    else:
        st.warning("أدخل الرابط أولاً")

# --- الفوتر المخصص ---
st.markdown("""
    <div class="custom-footer">
        DOSER | Abdelrahman<br>
        <small>تم التطوير بواسطة Doser</small>
    </div>
""", unsafe_allow_html=True)
