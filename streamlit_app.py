import streamlit as st
import requests
import random
from user_agent import generate_user_agent
from time import sleep

# --- إعدادات الصفحة والتصميم الاحترافي ---
st.set_page_config(
    page_title="Doser | Social Booster",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS احترافي متقدم
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    * { font-family: 'Tajawal', sans-serif; }
    
    .stApp { 
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(2deg); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.5), 0 0 40px rgba(0, 212, 255, 0.3); }
        50% { box-shadow: 0 0 30px rgba(0, 212, 255, 0.8), 0 0 60px rgba(0, 212, 255, 0.5); }
    }
    
    @keyframes pulse-ring {
        0% { transform: scale(0.8); opacity: 0.5; }
        100% { transform: scale(1.3); opacity: 0; }
    }
    
    .logo-container {
        position: relative;
        width: 180px;
        height: 180px;
        margin: 0 auto 30px auto;
    }
    
    .logo-ring {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 200px;
        border: 3px solid #00d4ff;
        border-radius: 50%;
        animation: pulse-ring 2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
    }
    
    .logo-img {
        position: relative;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 4px solid #00d4ff;
        object-fit: cover;
        animation: float 6s ease-in-out infinite, glow 3s ease-in-out infinite;
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.4);
        z-index: 10;
    }
    
    .title-text {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #00d4ff, #7b2cbf, #00d4ff);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 3s ease infinite;
        margin-bottom: 10px;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
        letter-spacing: 2px;
    }
    
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .subtitle {
        text-align: center;
        color: #a0a0a0;
        font-size: 1.2rem;
        margin-bottom: 40px;
        font-weight: 400;
        letter-spacing: 1px;
    }
    
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 15px !important;
        color: white !important;
        backdrop-filter: blur(10px);
    }
    
    .stSelectbox > div > div:hover {
        border-color: #00d4ff !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 15px !important;
        color: white !important;
        padding: 15px !important;
        font-size: 16px !important;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 25px rgba(0, 212, 255, 0.4);
        transform: translateY(-2px);
    }
    
    .stButton > button {
        width: 100%;
        padding: 18px;
        border-radius: 15px;
        background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
        color: white;
        font-weight: 900;
        font-size: 1.3rem;
        border: none;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.5);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .footer {
        text-align: center;
        padding: 30px;
        margin-top: 50px;
        border-top: 1px solid rgba(0, 212, 255, 0.2);
        background: rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 20px 20px 0 0;
    }
    
    .footer-text {
        color: #00d4ff;
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }
    
    .footer-sub {
        color: #666;
        font-size: 0.9rem;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d4ff, transparent);
        margin: 40px 0;
        border: none;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #0f0c29;
    }
    ::-webkit-scrollbar-thumb {
        background: #00d4ff;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الشعار والهيدر الاحترافي ---
st.markdown("""
    <div class="logo-container">
        <div class="logo-ring"></div>
        <img src="icon.png" class="logo-img" alt="Doser Logo">
    </div>
    <h1 class="title-text">DOSER</h1>
    <p class="subtitle">منصة تعزيز الخدمات الاجتماعية الذكية</p>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- دالة توليد IP عشوائي ---
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# --- دالات الإرسال ---
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
        st.info(f"⏳ جاري المعالجة... انتظر {wait_time} ثوانٍ")
        
        with st.spinner(''):
            progress_bar = st.progress(0)
            for i in range(100):
                sleep(wait_time/100)
                progress_bar.progress(i + 1)
        
        r = requests.post(url, headers=headers, data=data)
        
        if "Please wait" in r.text or '"error":' in r.text:
            st.error("⚠️ يوجد تأخير من الخادم، يرجى المحاولة لاحقاً")
        else:
            st.balloons()
            st.success(f"✅ تم التنفيذ بنجاح! (IP: {random_ip})")
            
    except Exception as e:
        st.error(f"❌ خطأ في الاتصال: {str(e)}")

# --- واجهة الاختيار ---
col1, col2 = st.columns([1, 1])

with col1:
    option = st.selectbox(
        "اختر الخدمة",
        ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"],
        index=0
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    
video_url = st.text_input(
    "🔗 رابط المنشور",
    placeholder="https://www.example.com/...",
    help="ألصق الرابط هنا"
)

# --- زر التنفيذ ---
if st.button("🚀 تنفيذ الطلب"):
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
        st.warning("⚠️ يرجى إدخال الرابط أولاً")

# --- الفوتر الاحترافي ---
st.markdown("""
    <div class="footer">
        <div class="footer-text">DOSER | Abdelrahman</div>
        <div class="footer-sub">تم التطوير بواسطة Doser © 2026</div>
    </div>
""", unsafe_allow_html=True)
