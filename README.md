# 🎯 14. Proje: E-Commerce Customer Segmentation (Müşteri Segmentasyonu)

Bu proje, müşteri demografilerini ve harcama alışkanlıklarını analiz ederek alt kırılımdaki homojen hedef kitleleri ve gizli alışveriş kalıplarını keşfeden bir **Gözetimsiz Öğrenme (Unsupervised Learning)** projesidir.

---

## 📊 Hocanın Dikkatine: Eksikler & Mühendislik Çözümleri

* **1. Eksik (Etiketsiz Veri Çıkmazı):** Orijinal veri setinde "sadık müşteri" veya "riskli müşteri" gibi hiçbir hedef etiket (`y` sütunu) bulunmuyordu.
    * **✔️ Çözüm:** Veri kümesini kendi kendine gruplayabilen **`K-Means Clustering`** mimarisi entegre edilerek anlamsal eksiklik giderildi.
* **2. Eksik (Ölçek ve Varyans Bozukluğu):** Yaş (18-70) ve Yıllık Gelir (15k-140k) sütunları arasındaki devasa sayısal basamak farkı, mesafe tabanlı algoritmaları yanıltıyordu.
    * **✔️ Çözüm:** Tüm sayısal veriler `StandardScaler` ile eşit varyansa getirilerek değişkenlerin birbirini ezmesi engellendi.
* **3. Eksik (Küme Sayısı Belirsizliği):** Verinin kaç gruba ayrılacağı orijinal Kaggle verisinde tanımlı değildi.
    * **✔️ Çözüm:** Rastgele seçim yerine **Dirsek Metodu (The Elbow Method)** kullanılarak verinin en doğal kırılım noktasının **5 Küme (K=5)** olduğu matematiksel olarak kanıtlandı.

---

## 📈 Model Yapılandırması & Metrikler

* **Problem Türü:** Kümeleme (Clustering / Unsupervised Learning)
* **Seçilen Algoritma:** `K-Means++` Optimizasyonu
* **Kritik Metrik:** **Inertia / WCSS** (Within-Cluster Sum of Squares)

---

## 🚀 Canlı Uygulama (Deployment)

Proje, **Hugging Face Spaces** üzerinde **Streamlit** mimarisi kullanılarak canlıya taşınmıştır. Kullanıcıların girdiği yaş, gelir ve harcama skorlarına göre anlık stratejik pazarlama aksiyon planı üreten dinamik simülasyon paneli başarıyla tamamlanmıştır.
