import sqlite3
import streamlit as st
import pandas as pd

# SQLite veritabanına bağlan
conn = sqlite3.connect(r'C:\Users\ASUS\Desktop\442\spotify.db')
cursor = conn.cursor()

# Kullanıcıdan sadece 1 ile 6 arasındaki periyotlar için Gross Requirement değerlerini al
gross_requirements = {}
num_periods = 6  # Toplam periyot sayısı (örneğin, 6 hafta)

for i in range(1, num_periods + 1):
    gross_requirement = st.number_input(f'Gross Requirement for Period {i}', min_value=0, max_value=None, value=0)
    gross_requirements[i] = gross_requirement

# Gross Requirement değerlerini MRP tablosuna ekleyerek diğer sütunları güncelle
for i, gross_requirement in gross_requirements.items():
    if i != 0:  # Periyot 0'a değer girilmesini engellemek için kontrol
        cursor.execute(f"UPDATE MRP SET GrossRequirements = {gross_requirement} WHERE PartID = 1 AND PeriodID = {i}")
        # Diğer sütunları güncellemek için gerekli sorguları ekleyin

# Veritabanındaki değişiklikleri kaydet
conn.commit()

# MRP tablosundan verileri çek
cursor.execute("SELECT * FROM MRP WHERE PartID = 1")
mrp_data = cursor.fetchall()

# Sütun başlıklarını ekleyerek bir DataFrame oluştur
columns = [description[0] for description in cursor.description]
mrp_df = pd.DataFrame(mrp_data, columns=columns)

# Streamlit'te verileri görselleştir
st.title('MRP Table')
st.dataframe(mrp_df)

# Veritabanı bağlantısını kapat
conn.close()
