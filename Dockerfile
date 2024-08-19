# Resmi Python base image'ını kullan
FROM python:3.10.12

# Uygulamanın dosyalarının kopyalanacağı çalışma dizinini belirle
WORKDIR /content/app

# Gerekli Python kütüphanelerini içeren requirements.txt dosyasını kopyala
COPY requirements.txt .

# Kütüphaneleri kur
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamanın geri kalan dosyalarını kopyala
COPY . .

# Flask'ın varsayılan portunu aç
EXPOSE 5000

# Uygulamayı çalıştırma komutu
CMD ["flask", "run", "--host=0.0.0.0"]
