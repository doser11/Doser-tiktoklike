
import streamlit as st
import requests
import random
import base64
from user_agent import generate_user_agent
from time import sleep

# --- وظيفة لتحويل الصورة المحلية إلى Base64 لعرضها ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# --- إعدادات الصفحة المتقدمة ---
st.set_page_config(
    page_title="Doser || TikTok",
    page_icon="⚔️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تحويل الصورة icon.png
img_base64 = get_base64_image("icon.png")
avatar_html = f'data:image/png;base64,{img_base64}' if img_base64 else ""

# --- CSS هندسي متطور (Custom UI/UX) ---
st.markdown(f"""
    <style>
    /* إعدادات الخلفية العامة */
    .stApp {{
        background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    /* تصميم الحاوية الرئيسية */
    .main-container {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        text-align: center;
    }}

    /* تصميم الصورة الشخصية المتحرك */
    .user-avatar {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 3px solid #FFD700;
        padding: 5px;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        transition: 0.5s;
        object-fit: cover;
    }}
    .user-avatar:hover {{
        transform: rotate(360s);
        transition: 0.5s;
    }}

    /* العناوين */
    .main-title {{
        color: #FFD700;
        font-size: 2.5rem;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-top: 15px;
    }}

    /* تحسين شكل الحقول */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
        background-color: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid #444 !important;
        color: #FFD700 !important;
        border-radius: 10px !important;
        transition: 0.3s;
    }}
    .stTextInput input:focus {{
        border-color: #FFD700 !important;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.2) !important;
    }}

    /* زر التشغيل الخرافي */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #FFD700, #DAA520);
        color: #000 !important;
        border: none;
        padding: 15px;
        font-weight: bold;
        font-size: 1.1rem;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .stButton>button:hover {{
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
        background: #FFD700;
    }}

    /* الميتا تاجز المخفية للتنسيق */
    .description {{
        color: #aaa;
        font-size: 0.9rem;
        margin-bottom: 25px;
    }}
    
    hr {{ border: 0.5px solid rgba(255,215,0,0.2); }}
    </style>
    
    <meta name="description" content="Doser Professional Social Services Dashboard">
    """, unsafe_allow_html=True)

# --- محتوى الواجهة ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# عرض الأفاتار (icon.png)
if img_base64:
    st.markdown(f'<img src="{avatar_html}" class="user-avatar">', unsafe_allow_html=True)
else:
    st.markdown('<div style="color:red">يرجى التأكد من وجود ملف icon.png في المجلد</div>', unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Doser || Abdelrahman</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">المنصة الأقوى لتعزيز الحسابات الاجتماعية بهندسة برمجية متطورة</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- منطق البرمجة (Backend Logic) ---
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def send_request(url, link, quantity=None):
    random_ip = generate_random_ip()
    headers = {
        "User-Agent": generate_user_agent(),
        "X-Forwarded-For": random_ip,
        "Client-IP": random_ip
    }
    data = {
        "token": "FAKETOKEN", 
        "timezone_offset": "Asia/Baghdad",
        "free_link": link
    }
    if quantity: data["quantity"] = quantity
    
    try:
        wait_time = random.randint(3, 6)
        progress_bar = st.progress(0)
        for i in range(100):
            sleep(wait_time/100)
            progress_bar.progress(i + 1)
        
        r = requests.post(url, headers=headers, data=data, timeout=10)
        
        if r.status_code == 200:
            st.balloons()
            st.success(f"⚡ تم التنفيذ بنجاح! IP: {random_ip}")
        else:
            st.error("❌ فشل الطلب، الموقع قد يكون تحت الصيانة.")
    except Exception as e:
        st.error(f"⚠️ خطأ تقني: {e}")

# --- واجهة الإدخال المتجاوبة ---
col1, col2 = st.columns([1, 1])

with col1:
    option = st.selectbox(
        "نوع الخدمة",
        ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"],
        index=0
    )

with col2:
    video_url = st.text_input("رابط المحتوى", placeholder="https://www.example.com/...")

st.write("") # مسافة جمالية

if st.button("🚀 إطلاق العملية"):
    if video_url:
        if option == "إعجابات يوتيوب":
            send_request("https://leofame.com/free-youtube-likes?api=1", video_url)
        elif option == "إعجابات تيك توك":
            send_request("https://leofame.com/free-tiktok-likes?api=1", video_url)
        elif option == "حفظ إنستغرام":
            send_request("https://leofame.com/free-instagram-saves?api=1", video_url, "30")
        elif option == "مشاهدات تيك توك":
            send_request("https://leofame.com/ar/free-tiktok-views?api=1", video_url, "200")
    else:
        st.warning("⚠️ لا يمكن البدء بدون إدخال الرابط!")

# --- التذييل (Footer) ---
st.write("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-family: monospace;">
        &copy; 2026 Doser Engineering System | Designed by Abdelrahman <br>
        <span style="color: #FFD700;">Logic & Aesthetic Fusion</span>
    </div>
    """, unsafe_allow_html=True)
