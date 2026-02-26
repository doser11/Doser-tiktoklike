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

# --- إعدادات الميتا والصفحة ---
st.set_page_config(
    page_title="Doser || TikTok",
    page_icon="⚔️",
    layout="wide" # جعل الصفحة عريضة للتحكم الأفضل في التنسيق
)

img_base = get_base64_image("icon.png")

# --- CSS هندسي احترافي (التركيز على الشكل والاستجابة) ---
st.markdown(f"""
    <style>
    /* إعدادات الخلفية والخطوط */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    .stApp {{
        background: #050505;
        font-family: 'Cairo', sans-serif;
        color: white;
    }}

    /* حاوية التوسط الرئيسية (لجعل كل شيء في السنتر) */
    .main-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        margin-top: 2rem;
    }}

    /* تنسيق الصورة (كبيرة، دائرية، وفي المنتصف) */
    .hero-img {{
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 4px solid #FFD700;
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.3);
        object-fit: cover;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }}
    .hero-img:hover {{ transform: scale(1.05); }}

    /* العنوان الرئيسي */
    .title-text {{
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(to right, #FFD700, #FFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
        text-align: center;
    }}

    /* كارت الخدمة (Glassmorphism) */
    .service-card {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 215, 0, 0.1);
        border-radius: 25px;
        padding: 40px;
        width: 100%;
        max-width: 600px;
        margin: 20px auto;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    }}

    /* تحسين الأزرار البرمجية */
    .stButton>button {{
        background: linear-gradient(45deg, #FFD700, #DAA520) !important;
        color: black !important;
        border: none !important;
        border-radius: 15px !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        box-shadow: 0 5px 15px rgba(218, 165, 32, 0.3) !important;
        transition: 0.4s !important;
    }}
    .stButton>button:hover {{
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 25px rgba(218, 165, 32, 0.5) !important;
    }}

    /* إخفاء عناصر Streamlit الزائدة لتنظيف الواجهة */
    #MainMenu, footer, header {{visibility: hidden;}}
    
    /* جعل الحقول متناسقة مع التصميم */
    .stTextInput input, .stSelectbox select {{
        background-color: #111 !important;
        color: #FFD700 !important;
        border: 1px solid #333 !important;
        text-align: center !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- بناء الهيكل البصري ---
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

# عرض الصورة المركزية
if img_base:
    st.markdown(f'<div style="text-align: center;"><img src="data:image/png;base64,{img_base}" class="hero-img"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="text-align: center;"><div class="hero-img" style="background:#222; display:flex; align-items:center; justify-content:center;">No Icon</div></div>', unsafe_allow_html=True)

st.markdown('<h1 class="title-text">Doser || Abdelrahman</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#888; font-size:1.1rem;">الهندسة الذكية لخدمات الرشق المتطورة</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # نهاية wrapper العناوين

# --- منطقة العمليات (داخل الكارت الزجاجي) ---
st.markdown('<div class="service-card">', unsafe_allow_html=True)

col_mid = st.columns([0.1, 0.8, 0.1])[1] # لضمان توسيط العناصر الداخلية

with col_mid:
    option = st.selectbox("🎯 اختر الخدمة البرمجية:", 
                          ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ إنستغرام", "مشاهدات تيك توك"])
    
    video_url = st.text_input("🔗 ضع الرابط هنا", placeholder="https://...")
    
    st.write("") # مساحة
    
    btn_trigger = st.button("تفعيل الرشق الآن")

st.markdown('</div>', unsafe_allow_html=True) # نهاية الكارت

# --- منطق البرمجة (الباك إند) ---
def send_request(url, link, quantity=None):
    random_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    headers = {"User-Agent": generate_user_agent(), "X-Forwarded-For": random_ip}
    data = {"token": "FAKETOKEN", "timezone_offset": "Asia/Baghdad", "free_link": link}
    if quantity: data["quantity"] = quantity
    
    try:
        with st.status("🛠️ جاري الاتصال بالخوادم...", expanded=True) as status:
            sleep(random.randint(2, 4))
            r = requests.post(url, headers=headers, data=data, timeout=10)
            if r.status_code == 200:
                status.update(label="✅ تم الإرسال بنجاح!", state="complete")
                st.balloons()
                st.success(f"تم التنفيذ عبر IP: {random_ip}")
            else:
                status.update(label="❌ فشل في الوصول للموقع", state="error")
    except Exception as e:
        st.error(f"خطأ تقني: {e}")

if btn_trigger:
    if video_url:
        if "يوتيوب" in option: send_request("https://leofame.com/free-youtube-likes?api=1", video_url)
        elif "تيك توك" in option and "إعجابات" in option: send_request("https://leofame.com/free-tiktok-likes?api=1", video_url)
        elif "إنستغرام" in option: send_request("https://leofame.com/free-instagram-saves?api=1", video_url, "30")
        elif "مشاهدات" in option: send_request("https://leofame.com/ar/free-tiktok-views?api=1", video_url, "200")
    else:
        st.warning("يرجى وضع رابط صحيح أولاً!")

# --- التذييل (Footer) ---
st.markdown("""
    <div style="margin-top: 50px; text-align: center; border-top: 1px solid #222; padding-top: 20px;">
        <p style="color: #444; font-size: 0.8rem;">
            DEVELOPED BY: <b>Doser Engine</b><br>
            Metatags: Social-Panel, Doser-Logic, Responsive-UI
        </p>
    </div>
    """, unsafe_allow_html=True)
