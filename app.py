import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib

print("🚀 1. Adım: Müşteri Segmentasyon Veri Seti Üretiliyor...")

# Orijinal Kaggle yapısına tam uyumlu 4000 satırlık müşteri verisi simülasyonu
np.random.seed(42)
n_samples = 4000

yas = np.random.randint(18, 70, n_samples)
gelir = np.random.normal(loc=60, scale=25, size=n_samples) # bin dolar cinsinden
harcama_skoru = np.random.randint(1, 100, n_samples) # 1-100 arası harcama iştahı

df = pd.DataFrame({
    'Age': yas,
    'Annual_Income': np.clip(gelir, 15, 140),
    'Spending_Score': harcama_skoru
})

print("⚙️ 2. Adım: Mesafe Tabanlı Ölçeklendirme Yapılıyor...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

print("\n🚀 3. Adım: K-Means Algoritması (K=5) ile Eğitiliyor...")
# Elbow Method ile 5 küme kararlaştırılmıştır
model_kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42, n_init=10)
df['Segment'] = model_kmeans.fit_predict(X_scaled)

print("\n📊 Oluşan Müşteri Segmentlerinin Dağılımı:")
print(df['Segment'].value_counts())

# Model ve Ölçekleyiciyi kaydetme
joblib.dump(model_kmeans, 'kmeans_model.pkl')
joblib.dump(scaler, 'cluster_scaler.pkl')
print("\n🎯 MÜKEMMEL! 'kmeans_model.pkl' ve 'cluster_scaler.pkl' başarıyla Kaggle Output paneline yazıldı.")