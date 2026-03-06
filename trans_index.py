import os
import re

def translate_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        "Özellikler": "Features",
        "Fiyatlandırma": "Pricing",
        "SSS": "FAQ",
        "Gizlilik Politikası": "Privacy Policy",
        "Kullanım Koşulları": "Terms of Use",
        "App Store'da İndir": "Download on the App Store",
        "Herhangi Bir Dosyayı Anında Dönüştür": "Convert Any File Instantly",
        "Görselleri, PDF'leri ve belgeleri tek dokunuşla dönüştür. Hızlı, güvenli ve güçlü.": "Convert images, PDFs, and documents with a single tap. Fast, secure, and powerful.",
        "Daha Fazla Bilgi": "Learn More",
        "iPhone Ekran Görüntüsü": "iPhone Screenshot",
        "Güçlü Özellikler": "Powerful Features",
        "Convertify+ ile dosya dönüştürme hiç bu kadar kolay olmamıştı": "File conversion has never been easier with Convertify+",
        "Tüm Format Desteği": "All Format Support",
        "PDF, DOCX, JPG, PNG, HEIC, WEBP, MP4 ve daha fazlası.": "PDF, DOCX, JPG, PNG, HEIC, WEBP, MP4 & more.",
        "Yıldırım Hızı": "Lightning Fast",
        "Dosyaları saniyeler içinde dönüştür, cihazda işleme ile.": "Convert files in seconds using on-device processing.",
        "%100 Gizli": "100% Private",
        "Tüm dönüştürmeler yerel olarak gerçekleşir. Sunuculara dosya yüklenmez.": "All conversions happen locally. No files uploaded to servers.",
        "OCR Metin Tanıma": "OCR Text Recognition",
        "Görseller ve taranmış belgelerden metin çıkart.": "Extract text from images and scanned documents.",
        "PDF Araçları": "PDF Tools",
        "PDF'leri birleştir, böl, sıkıştır ve dönüştür.": "Merge, split, compress, and convert PDFs.",
        "Toplu İşlem": "Batch Processing",
        "Pro ile birden fazla dosyayı aynı anda dönüştür.": "Convert multiple files at once with Pro.",
        "Nasıl Çalışır?": "How It Works",
        "3 basit adımda dosyalarını dönüştür": "Convert your files in 3 simple steps",
        "Dosyanı Seç": "Select Your File",
        "Fotoğraflardan, Dosyalardan veya herhangi bir uygulamadan seç.": "Choose from Photos, Files, or any app.",
        "Çıkış Formatını Seç": "Choose Output Format",
        "20+ desteklenen format arasından seç.": "Select from 20+ supported formats.",
        "Dönüştür & Paylaş": "Convert & Share",
        "Dosyanı anında al. Kaydet veya herhangi yere paylaş.": "Get your file instantly. Save or share anywhere.",
        "Basit Fiyatlandırma": "Simple Pricing",
        "Tüm planlar sınırsız dönüştürme içerir": "All plans include unlimited conversions",
        "Haftalık": "Weekly",
        "₺29<span>.99/hafta</span>": "$2<span>.99/week</span>",
        "Sınırsız Dönüştürme": "Unlimited Conversions",
        "Tüm Formatlar": "All Formats",
        "Dosya Boyutu Sınırı Yok": "No File Size Limit",
        "Öncelikli Destek": "Priority Support",
        ">Başla<": ">Start<",
        "Aylık": "Monthly",
        "₺79<span>.99/ay</span>": "$7<span>.99/month</span>",
        "EN POPÜLER": "MOST POPULAR",
        "Yıllık": "Yearly",
        "₺349<span>.99/yıl</span>": "$34<span>.99/year</span>",
        "2 ücretsiz dönüştürme dahil. Kredi kartı gerekmez.": "2 free conversions included. No credit card required.",
        "Sık Sorulan Sorular": "Frequently Asked Questions",
        "Convertify+ ücretsiz mi?": "Is Convertify+ free?",
        "2 ücretsiz dönüştürme alırsınız. Bundan sonra sınırsız erişim için abone olun.": "You get 2 free conversions. After that, subscribe for unlimited access.",
        "Dosyalarım güvenli mi?": "Are my files safe?",
        "Evet. Tüm işlemler cihazınızda gerçekleşir. Dosyalarınızı hiçbir zaman sunuculara yüklemeyiz.": "Yes. All processing happens on your device. We never upload files to our servers.",
        "İptal edebilir miyim?": "Can I cancel?",
        "Kesinlikle. Apple ID ayarlarından istediğiniz zaman iptal edebilirsiniz.": "Absolutely. You can cancel anytime from your Apple ID settings.",
        "Hangi formatlar destekleniyor?": "What formats are supported?",
        "Görseller (JPG, PNG, HEIC, WEBP, BMP, TIFF), Belgeler (PDF, DOCX, TXT, RTF) ve daha fazlası.": "Images (JPG, PNG, HEIC, WEBP, BMP, TIFF), Documents (PDF, DOCX, TXT, RTF) & more.",
        "Satın almamı nasıl geri yüklerim?": "How do I restore my purchase?",
        "Uygulamadaki Ayarlar'a gidin ve 'Satın Almayı Geri Yükle'ye dokunun veya ödeme ekranındaki Geri Yükle düğmesini kullanın.": "Go to Settings in the app and tap 'Restore Purchase', or use the Restore button on the paywall.",
        "Hizmet Şartları": "Terms of Service",
        "Tüm Hakları Saklıdır.": "All Rights Reserved."
    }

    for tr, en in replacements.items():
        content = content.replace(tr, en)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

translate_html('index.html')
print("Done.")
