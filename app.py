from flask import Flask, render_template

# إنشاء تطبيق Flask
app = Flask(__name__)

# تحديد المسار الرئيسي (الصفحة الرئيسية)
@app.route('/')
def home():
    # هنا يتم عرض ملف HTML الخاص بك من مجلد "templates"
    # تأكد أن اسم الملف مطابق تماماً: indexx.html
    return render_template('indexx.html')

# جزء اختياري: يمكنك إضافة مسارات أخرى هنا إذا احتجت إليها مستقبلاً
# @app.route('/about')
# def about():
#     return "هذه صفحة حول"

# تشغيل التطبيق محليًا (لا يعمل على الخادم، فقط للتجربة على جهازك)
if __name__ == '__main__':
    # يعمل على http://127.0.0.1:5000/
    # في حال لم تكن تستخدم ميزات التشفير المتقدمة، يمكنك إزالة الـ host=...
    app.run(debug=True, host='0.0.0.0')
