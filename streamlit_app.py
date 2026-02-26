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
st.set_page_config(page_title="Doser || Abdelrahman", page_icon="⚔️", layout="centered", initial_sidebar_state="collapsed")

img_base = get_base64_image("icon.png")

# --- CSS: تصميم iOS 26 Liquid Glass & Neumorphism ---
st.markdown(f'''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600;700&family=Cairo:wght@400;700&display=swap');
    
    /* خلفية iOS 26 - Liquid Glass Effect */
    .stApp {{
        background: linear-gradient(135deg, #f5f5f7 0%, #e8e8ed 50%, #f0f0f5 100%);
        background-attachment: fixed;
        font-family: 'SF Pro Display', 'Cairo', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    /* إخفاء كل عناصر Streamlit الافتراضية */
    #MainMenu, footer, header, .stDeployButton, .stAppToolbar, .stActionButton,
    .st-emotion-cache-1dp5vir, .st-emotion-cache-15ecox0, .st-emotion-cache-1wbqy5l,
    .st-emotion-cache-1avcm0n, .st-emotion-cache-18ni7ap, .st-emotion-cache-1y4p8pa,
    .st-emotion-cache-1cypcdb, .st-emotion-cache-1wrcr25, .st-emotion-cache-16txtl3,
    .st-emotion-cache-1jicfl2, .st-emotion-cache-10trblm, .st-emotion-cache-16idsys {{
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        position: absolute !important;
        top: -9999px !important;
        pointer-events: none !important;
    }}
    
    /* إخفاء الشريط العلوي والأزرار */
    .stApp header, .stToolbar, .stAppToolbar {{
        display: none !important;
    }}
    
    /* إزالة المساحات الفارغة */
    .main > div {{
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }}
    
    .block-container {{
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 600px !important;
    }}
    
    /* تنسيق الصورة الشخصية - iOS 26 Style */
    .profile-container {{
        display: flex;
        justify-content: center;
        margin: 30px 0 25px 0;
    }}
    
    .hero-img {{
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.15),
            0 0 0 8px rgba(255, 255, 255, 0.8),
            0 0 0 12px rgba(0, 122, 255, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    
    .hero-img:hover {{
        transform: scale(1.02);
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.2),
            0 0 0 8px rgba(255, 255, 255, 0.9),
            0 0 0 12px rgba(0, 122, 255, 0.2);
    }}

    /* العنوان الرئيسي - iOS 26 Blue */
    .main-title {{
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #007AFF 0%, #5856D6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
        letter-spacing: -0.5px;
        text-align: center;
    }}
    
    /* الحاوية الزجاجية - Liquid Glass Effect */
    .glass-quote-container {{
        background: rgba(255, 255, 255, 0.72);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 24px;
        padding: 20px 25px;
        text-align: center;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.6);
        margin: 25px auto 35px auto;
        width: 90%;
        max-width: 500px;
    }}
    
    /* تنسيق الجملة - Dark Gray iOS */
    .quote-text {{
        color: #1c1c1e;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0;
        line-height: 1.4;
        letter-spacing: -0.2px;
    }}

    /* تحسين شكل المدخلات - iOS Style */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {{
        background: rgba(255, 255, 255, 0.8) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(0, 0, 0, 0.08) !important;
        color: #1c1c1e !important;
        height: 52px !important;
        direction: rtl !important;
        text-align: right !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
        padding: 0 18px !important;
        box-shadow: 
            inset 0 1px 2px rgba(0, 0, 0, 0.05),
            0 2px 4px rgba(0, 0, 0, 0.02) !important;
        transition: all 0.2s ease !important;
    }}
    
    .stTextInput input:focus, .stSelectbox [data-baseweb="select"]:focus {{
        border-color: #007AFF !important;
        box-shadow: 
            0 0 0 4px rgba(0, 122, 255, 0.15),
            inset 0 1px 2px rgba(0, 0, 0, 0.05) !important;
        background: rgba(255, 255, 255, 0.95) !important;
    }}
    
    .stTextInput input::placeholder {{
        color: #8e8e93 !important;
    }}
    
    /* تنسيق الـ select box */
    .stSelectbox [data-baseweb="select"] > div {{
        background: transparent !important;
        color: #1c1c1e !important;
    }}
    
    /* تنسيق القائمة المنسدلة */
    .stSelectbox [data-baseweb="popover"] {{
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 0, 0, 0.08) !important;
        border-radius: 16px !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15) !important;
    }}
    
    .stSelectbox [data-baseweb="popover"] li {{
        color: #1c1c1e !important;
        background: transparent !important;
        font-size: 0.95rem !important;
        padding: 12px 16px !important;
        border-radius: 8px !important;
        margin: 4px 8px !important;
    }}
    
    .stSelectbox [data-baseweb="popover"] li:hover {{
        background: rgba(0, 122, 255, 0.1) !important;
        color: #007AFF !important;
    }}

    /* زر التشغيل - iOS 26 Style */
    .stButton>button {{
        background: linear-gradient(135deg, #007AFF 0%, #5856D6 100%) !important;
        color: white !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        height: 56px !important;
        width: 100% !important;
        border: none !important;
        margin-top: 20px !important;
        box-shadow: 
            0 4px 15px rgba(0, 122, 255, 0.3),
            0 1px 2px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        letter-spacing: -0.3px !important;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 
            0 8px 25px rgba(0, 122, 255, 0.4),
            0 2px 4px rgba(0, 0, 0, 0.1) !important;
        background: linear-gradient(135deg, #007AFF 0%, #6b69e0 100%) !important;
    }}
    
    .stButton>button:active {{
        transform: translateY(0px) scale(0.98);
    }}
    
    /* تنسيق رسائل النجاح والخطأ - iOS Style */
    .stAlert {{
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(0, 0, 0, 0.08) !important;
        border-radius: 16px !important;
        color: #1c1c1e !important;
        font-weight: 500 !important;
        text-align: center !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
    }}
    
    .stSuccess {{
        background: rgba(52, 199, 89, 0.15) !important;
        border-color: rgba(52, 199, 89, 0.4) !important;
        color: #34c759 !important;
    }}
    
    .stError {{
        background: rgba(255, 59, 48, 0.15) !important;
        border-color: rgba(255, 59, 48, 0.4) !important;
        color: #ff3b30 !important;
    }}
    
    .stWarning {{
        background: rgba(255, 204, 0, 0.15) !important;
        border-color: rgba(255, 204, 0, 0.4) !important;
        color: #ffcc00 !important;
    }}
    
    .stInfo {{
        background: rgba(0, 122, 255, 0.15) !important;
        border-color: rgba(0, 122, 255, 0.4) !important;
        color: #007AFF !important;
    }}
    
    /* تنسيق الـ spinner */
    .stSpinner > div {{
        border-color: #007AFF transparent transparent transparent !important;
    }}
    
    /* تنسيق الفوتر - iOS Gray */
    .footer-text {{
        text-align: center;
        color: #8e8e93;
        font-size: 0.9rem;
        margin-top: 40px;
        font-weight: 400;
        letter-spacing: 0.5px;
    }}
    
    /* تنسيق العلامات */
    .service-tag {{
        display: inline-block;
        background: rgba(0, 122, 255, 0.1);
        color: #007AFF;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 15px;
    }}
    
    /* Divider iOS Style */
    .ios-divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0,0,0,0.1), transparent);
        margin: 30px 0;
    }}
    
    /* تنسيق حالة الاتصال */
    .status-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 10px;
    }}
    
    .status-online {{
        background: rgba(52, 199, 89, 0.15);
        color: #34c759;
    }}
    
    .status-offline {{
        background: rgba(255, 59, 48, 0.15);
        color: #ff3b30;
    }}
    
    .status-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: currentColor;
    }}
    </style>
    ''', unsafe_allow_html=True)

# --- الهيكل البصري ---

# 1. الصورة في المنتصف
if img_base:
    st.markdown(f'<div class="profile-container"><img src="data:image/png;base64,{img_base}" class="hero-img"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="profile-container"><div class="hero-img" style="background:linear-gradient(135deg, #007AFF, #5856D6);"></div></div>', unsafe_allow_html=True)

# 2. العنوان الرئيسي
st.markdown('<h1 class="main-title">Doser || Abdelrahman</h1>', unsafe_allow_html=True)

# 3. الحاوية الزجاجية للجملة
st.markdown('''
    <div class="glass-quote-container">
        <div class="quote-text">الهندسة الذكية لخدمات الرشق المتطورة</div>
    </div>
''', unsafe_allow_html=True)

st.markdown('<div class="ios-divider"></div>', unsafe_allow_html=True)

# --- دالة لتوليد IP عشوائي ---
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# --- دالة إرسال الطلب إلى leofame ---
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
        # إضافة تأخير عشوائي بين 3 إلى 7 ثوانٍ
        wait_time = random.randint(3, 7)
        st.info(f"⏳ جاري الانتظار {wait_time} ثوانٍ لتجنب الحظر...")
        sleep(wait_time)
        
        r = requests.post(url, headers=headers, data=data, timeout=30)
        
        # التحقق من الاستجابة
        if "Please wait" in r.text or '"error":' in r.text:
            st.error("⚠️ الموقع يطلب الانتظار. جرب لاحقاً أو غير الرابط.")
            return False
        elif r.status_code == 200:
            st.success(f"✅ تم الإرسال بنجاح بـ IP وهمي: {random_ip}")
            st.balloons()
            return True
        else:
            st.error(f"❌ فشل الاتصال. كود الحالة: {r.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        st.error("⏱️ انتهى وقت الانتظار. الموقع بطيء أو غير متاح حالياً.")
        return False
    except requests.exceptions.ConnectionError:
        st.error("🔌 خطأ في الاتصال. تأكد من اتصالك بالإنترنت.")
        return False
    except Exception as e:
        st.error(f"❌ حدث خطأ غير متوقع: {str(e)}")
        return False

# 4. الحقول والزر
col_input = st.columns([0.05, 0.9, 0.05])[1]
with col_input:
    st.markdown('<div class="service-tag">اختر الخدمة</div>', unsafe_allow_html=True)
    
    # خيارات الخدمة مع الروابط المقابلة
    services = {
        "✨ إعجابات يوتيوب": ("https://leofame.com/free-youtube-likes?api=1", None),
        "✨ إعجابات تيك توك": ("https://leofame.com/free-tiktok-likes?api=1", None),
        "✨ حفظ إنستغرام": ("https://leofame.com/free-instagram-saves?api=1", "30"),
        "✨ مشاهدات تيك توك": ("https://leofame.com/ar/free-tiktok-views?api=1", "200")
    }
    
    service_name = st.selectbox("", list(services.keys()), label_visibility="collapsed")
    
    st.markdown('<div style="height: 15px;"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="service-tag" style="background: rgba(88, 86, 214, 0.1); color: #5856D6;">الرابط</div>', unsafe_allow_html=True)
    video_url = st.text_input("", placeholder="https://...", label_visibility="collapsed")
    
    # 5. زر التنفيذ
    execute_btn = st.button("⚡ تفعيل الخدمة", type="primary")

st.markdown('<div class="ios-divider"></div>', unsafe_allow_html=True)

# --- معالجة الضغط على الزر ---
if execute_btn:
    if not video_url:
        st.error("❌ يرجى إدخال الرابط أولاً!")
    else:
        with st.spinner('🔄 جاري الاتصال بخوادم leofame...'):
            # الحصول على URL والكمية للخدمة المختارة
            service_url, quantity = services[service_name]
            
            # إرسال الطلب
            success = send_request(service_url, video_url, quantity)
            
            if success:
                st.markdown(f'''
                    <div style="text-align: center; margin-top: 20px;">
                        <div class="status-badge status-online">
                            <div class="status-dot"></div>
                            <span>الخدمة تعمل بنجاح</span>
                        </div>
                    </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown(f'''
                    <div style="text-align: center; margin-top: 20px;">
                        <div class="status-badge status-offline">
                            <div class="status-dot"></div>
                            <span>الخدمة متوقفة</span>
                        </div>
                    </div>
                ''', unsafe_allow_html=True)

# --- Footer ---
st.markdown('<p class="footer-text">Doser || Abdelrahman © 2026</p>', unsafe_allow_html=True)
