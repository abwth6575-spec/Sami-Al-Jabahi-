
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from faker import Faker

app = Flask(__name__)
fake = Faker()

# ترحيب بالبورد عند تشغيل السيرفر
@app.route("/", methods=["GET"])
def home():
    return "بوت أرقام واتساب المجاني يعمل بنجاح الآن على سيرفر GitHub!"

# استقبال رسائل الواتساب والرد عليها تلقائياً
@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    # استقبال الرسالة القادمة من المستخدم
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    # نظام الأوامر والرد التلقائي للبوت
    if incoming_msg in ['مرحبا', 'مرحبًا', 'hello', 'hi', 'البوت', 'تفعيل']:
        reply = (
            "🤖 أهلاً بك في بوت أرقام واتساب المجاني!\n\n"
            "للحصول على رقم وهمي مجاني لتفعيل الحسابات، أرسل كلمة:\n"
            "👉 *رقم*"
        )
        msg.body(reply)
        
    elif incoming_msg in ['رقم', 'رقم مجاني', 'number', 'num']:
        # توليد رقم هاتف افتراضي عشوائي مجاني مجاناً للمستخدم
        generated_number = fake.phone_number()
        reply = (
            "✅ تم توليد رقمك الافتراضي المجاني بنجاح:\n\n"
            f"📱 الرقم: `{generated_number}`\n\n"
            "ℹ️ يمكنك استخدام هذا الرقم لتفعيل الحسابات التجريبية. "
            "يرجى العلم أن الأرقام افتراضية للأغراض التعليمية والتجريبية فقط."
        )
        msg.body(reply)
        
    else:
        reply = "❌ عذراً، لم أفهم الأمر. أرسل كلمة *رقم* للحصول على رقم افتراضي مجاني فوراً."
        msg.body(reply)

    return str(resp)

if __name__ == "__main__":
    # تشغيل البوت على السيرفر المحلي
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
