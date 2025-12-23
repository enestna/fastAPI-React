# FastAPI & React Full Stack Projesi
 ## Projenin Amacı

Bu proje, backend tarafında **FastAPI**'ın asenkron gücünü, frontend tarafında ise **React**'in dinamik yapısını kullanan modern bir Full Stack web uygulamasıdır.
İstemci (client) ve sunucu (server) arasındaki veri akışını ve mimari bütünlüğü **REST API** standartlarına sadık kalarak gösteren proje; 
ayrıştırılmış (decoupled) uygulama yapısını ve modern web geliştirme pratiklerini sergilemektedir.

### Özellikler

* ✅ ** Starlette ve Pydantic sayesinde çok yüksek performans.
* ✅ ** Swagger UI ve ReDoc entegrasyonu.
* ✅ ** JWT ile güvenli kimlik doğrulama
* ✅ ** PostgreSQL veritabanı entegrasyonu

## kullanılan Teknolojiler
### Backend
-Python 
-FastAPI
-SQLite
### Frontend
-React
-JavaScript

## Proje Yapısı
fastAPI_React_full_stack/
│
├── main.py          → FastAPI uygulaması
├── database.py      → Veritabanı bağlantısı
├── models.py        → Veritabanı modelleri
├── my_db.db         → SQLite veritabanı
│
├── App.js           → React ana bileşeni
├── index.js         → React giriş noktası
├── package.json     → Frontend bağımlılıkları
│
└── README.md

## Backend Kurulum 
Backend tarafı FastAPI kullanılarak geliştirilmiştir. Gerekli python paketleri aşağıdaki komut ile yüklenir.

```
pip install fastapi uvicorn
```
## Backend Çalıştırma
FastAPI uygulaması başlatmak için aşağıdaki komut kullanılır.
```
uvicorn main:app --reload
```
API çalıştıktan sonra aşağıdaki adreslerden erişilebilir:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## Frontend Kurlulum 

Frontend tarafı React kullanılarak geliştirilmiştir. Gerekli paketler aşağıdaki komut ile yüklenir.
```
npm install
```
## Frontend Çalıştırma

React uygulamasını başlatmak için aşağıdaki komut kullanılır.
```
npm start
```

## Geliştiriciler

Enes TUNA 
Yusuf İslam EROĞLU

Bu proje, FastAPI ve React teknolojilerini kullanarak
full stack web uygulaması geliştirme pratiği kazanmak
amacıyla hazırlanmıştır. Proje sürecinde backend ve
frontend entegrasyonu temel seviyede uygulanmıştır.

 
 

  
