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

# CSS محسّن
st.markdown("""
    <style>
    .stApp > header, .stAppDeployButton, footer, .st-emotion-cache-1avcm0n, #MainMenu {
        display: none !important;
    }
    
    .stApp {
        margin-top: -80px !important;
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    * { font-family: 'Tajawal', sans-serif; margin: 0; padding: 0; }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.5); }
        50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.8); }
    }
    
    .logo-container { text-align: center; margin-bottom: 20px; }
    
    .logo-img {
        width: 150px; height: 150px; border-radius: 50%; border: 3px solid #00d4ff;
        object-fit: cover; animation: float 4s ease-in-out infinite, glow 3s ease-in-out infinite;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.4);
    }
    
    .title-text {
        text-align: center; font-size: 2.5rem; font-weight: 900;
        background: linear-gradient(45deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 10px 0; letter-spacing: 3px;
    }
    
    .subtitle { text-align: center; color: #888; font-size: 1rem; margin-bottom: 30px; }
    
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 10px !important;
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 10px !important; color: white !important; text-align: center;
    }
    
    .stButton > button {
        width: 100%; padding: 15px; border-radius: 10px;
        background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
        color: white; font-weight: bold; border: none; margin-top: 10px;
        transition: 0.3s;
    }
    
    .stButton > button:hover { transform: translateY(-2px); box-shadow: 0 5px 20px rgba(0, 212, 255, 0.4); }
    
    .custom-footer {
        text-align: center; padding: 20px; margin-top: 30px;
        border-top: 1px solid rgba(0, 212, 255, 0.2);
        color: #00d4ff; font-size: 0.9rem;
    }
    
    .success-box {
        background: rgba(0, 255, 0, 0.1);
        border: 1px solid #00ff00;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
    }
    
    .error-box {
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid #ff0000;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- التحقق من الصورة ---
if os.path.exists("icon.png"):
    image_path = "icon.png"
else:
    image_path = "https://via.placeholder.com/150/00d4ff/ffffff?text=DOSER"
    st.warning("⚠️ أضف ملف icon.png في نفس المجلد")

# --- الهيدر ---
st.markdown(f"""
    <div class="logo-container">
        <img src="{image_path}" class="logo-img" alt="Doser">
    </div>
    <h1 class="title-text">DOSER</h1>
    <p class="subtitle">منصة تعزيز الخدمات الاجتماعية</p>
""", unsafe_allow_html=True)

# --- دالة توليد IP ---
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# --- دالة الإرسال المحسّنة ---
def send_request(service_name, url, link, quantity=None):
    random_ip = generate_random_ip()
    user_agent = generate_user_agent()
    
    # هيدرز محسّنة ومكتملة
    headers = {
        "User-Agent": user_agent,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://leofame.com",
        "Referer": url.replace("?api=1", ""),
        "Connection": "keep-alive",
        "Cookie": f"PHPSESSID={random.randint(1000000000, 9999999999)}; _ga=GA1.1.{random.randint(100000000, 999999999)}.{random.randint(1000000000, 9999999999)}",
        "X-Forwarded-For": random_ip,
        "Client-IP": random_ip,
        "CF-Connecting-IP": random_ip,
        "True-Client-IP": random_ip
    }
    
    # بيانات محسّنة
    data = {
        "token": f"tok_{random.randint(100000, 999999)}",
        "timezone_offset": "Africa/Cairo",
        "free_link": link.strip()
    }
    
    # إضافة quantity للجميع (حتى الإعجابات تحتاج كمية)
    if quantity:
        data["quantity"] = str(quantity)
    else:
        # إذا لم يُحدد quantity، نضع قيمة افتراضية حسب الخدمة
        if "likes" in url.lower():
            data["quantity"] = str(random.randint(10, 20))  # 10-20 إعجاب افتراضي
    
    try:
        # تأخير عشوائي أطول لتجنب الحظر
        wait_time = random.randint(5, 10)
        
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        for i in range(100):
            sleep(wait_time/100)
            progress_bar.progress(i + 1)
            if i % 25 == 0:
                progress_text.text(f"⏳ جاري الإرسال... {i}%")
        
        progress_text.empty()
        
        # إرسال الطلب
        session = requests.Session()
        session.headers.update(headers)
        
        # محاولة أولى
        r = session.post(url, data=data, timeout=30)
        
        # التحقق من الاستجابة
        response_text = r.text.lower()
        
        if r.status_code == 200:
            if "success" in response_text or "completed" in response_text or "order" in response_text:
                st.balloons()
                st.markdown(f"""
                    <div class="success-box">
                        ✅ تم إرسال {service_name} بنجاح!<br>
                        <small>الكمية: {data.get('quantity', 'افتراضية')} | IP: {random_ip}</small>
                    </div>
                """, unsafe_allow_html=True)
                return True
            elif "wait" in response_text or "please" in response_text or "limit" in response_text:
                st.warning("⏳ الموقع يطلب الانتظار (Rate Limit)، حاول بعد دقيقة")
                return False
            else:
                # محاولة ثانية بدون quantity إذا فشلت الأولى
                if "quantity" in data:
                    del data["quantity"]
                    r2 = session.post(url, data=data, timeout=30)
                    if "success" in r2.text.lower():
                        st.balloons()
                        st.success(f"✅ تم الإرسال (محاولة 2)")
                        return True
                
                st.error(f"⚠️ الاستجابة: {r.text[:100]}")
                return False
        else:
            st.error(f"❌ خطأ في الاتصال: {r.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        st.error("❌ انتهى وقت الاتصال، حاول مرة أخرى")
        return False
    except Exception as e:
        st.error(f"❌ خطأ: {str(e)}")
        return False

# --- الواجهة ---
option = st.selectbox(
    "اختر الخدمة",
    ["إعجابات يوتيوب (10-20)", "إعجابات تيك توك (100-60)", "حفظ إنستغرام (30)", "مشاهدات تيك توك (200)"]
)

video_url = st.text_input("🔗 رابط المنشور", placeholder="https://www.youtube.com/watch?v=...")

col1, col2 = st.columns([1, 1])
with col1:
    quantity = st.number_input("الكمية (اختياري)", min_value=1, max_value=100, value=0, help="اتركه 0 للقيمة الافتراضية")

if st.button("🚀 تنفيذ الطلب"):
    if video_url and ("http://" in video_url or "https://" in video_url):
        
        # تحديد الـ endpoint والكمية
        if "يوتيوب" in option:
            url = "https://leofame.com/free-youtube-likes?api=1"
            default_qty = 15 if quantity == 0 else quantity
        elif "تيك توك" in option and "إعجابات" in option:
            url = "https://leofame.com/free-tiktok-likes?api=1"
            default_qty = 15 if quantity == 0 else quantity
        elif "إنستغرام" in option:
            url = "https://leofame.com/free-instagram-saves?api=1"
            default_qty = 30 if quantity == 0 else quantity
        else:  # مشاهدات تيك توك
            url = "https://leofame.com/ar/free-tiktok-views?api=1"
            default_qty = 200 if quantity == 0 else quantity
        
        # تنفيذ
        send_request(option, url, video_url, default_qty)
    else:
        st.warning("⚠️ أدخل رابط صحيح يبدأ بـ http")

# --- الفوتر ---
st.markdown("""
    <div class="custom-footer">
        DOSER | Abdelrahman<br>
        <small>تم التطوير بواسطة Doser © 2024</small>
    </div>
""", unsafe_allow_html=True)
