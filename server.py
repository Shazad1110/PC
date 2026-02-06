#!/usr/bin/env python3
"""
Simple HTTP Server for App Landing Page
بۆ کارپێکردنی ئەم سێرڤەرە، ئەم فەرمانە بنووسە:
python server.py
"""

import http.server
import socketserver
import json
import os
from pathlib import Path

# تێبینی: دەتوانیت پۆرتەکە بگۆڕیت
PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP Request Handler بۆ خزمەتکردنی فایلەکان
    """
    
    def end_headers(self):
        # زیادکردنی CORS headers بۆ لەبارکردنی فایلەکان
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Log کردنی داواکارییەکان
        print(f"📥 داواکاری بۆ: {self.path}")
        return super().do_GET()


def update_app_config(config_data):
    """
    نوێکردنەوەی فایلی JSON بە زانیاریی نوێ
    
    Args:
        config_data (dict): زانیاریی نوێ بۆ ئەپڵیکەیشن
    """
    config_file = Path('app-data.json')
    
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=2)
        print("✅ فایلی JSON بە سەرکەوتوویی نوێکرایەوە")
        return True
    except Exception as e:
        print(f"❌ هەڵە لە نوێکردنەوەی فایل: {e}")
        return False


def read_app_config():
    """
    خوێندنەوەی ڕێکخستنی ئێستای ئەپڵیکەیشن
    
    Returns:
        dict: زانیاریی ئەپڵیکەیشن
    """
    config_file = Path('app-data.json')
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ هەڵە لە خوێندنەوەی فایل: {e}")
        return None


def start_server():
    """
    دەستپێکردنی HTTP Server
    """
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print("=" * 60)
            print(f"🚀 سێرڤەر دەستی پێکرد لەسەر پۆرت {PORT}")
            print(f"🌐 سەردانی ئەم لینکە بکە: http://localhost:{PORT}")
            print(f"⏹️  بۆ ڕاگرتن، Ctrl+C دابگرە")
            print("=" * 60)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 سێرڤەر ڕاگیرا")
    except Exception as e:
        print(f"❌ هەڵە لە دەستپێکردنی سێرڤەر: {e}")


def main():
    """
    فەنکشنی سەرەکی
    """
    print("🔧 سێرڤەری شابڵۆد")
    print("-" * 60)
    
    # پشکنینی بوونی فایلە پێویستەکان
    required_files = ['index.html', 'style.css', 'script.js', 'app-data.json']
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if missing_files:
        print(f"⚠️  ئاگاداری: ئەم فایلانە نییە: {', '.join(missing_files)}")
        print("تکایە دڵنیابە لە بوونی هەموو فایلەکان\n")
    
    # خوێندنەوەی ڕێکخستنی ئێستا
    config = read_app_config()
    if config:
        print("📱 زانیاریی ئێستای ئەپڵیکەیشن:")
        print(f"   ناو: {config.get('appName', 'نادیار')}")
        print(f"   لینکی دابەزاندن: {config.get('downloadLink', 'نادیار')}")
        print()
    
    # دەستپێکردنی سێرڤەر
    start_server()


# نموونەی فەنکشنەکان بۆ کارکردن لەگەڵ config
def example_update_config():
    """
    نموونە بۆ چۆنیەتیی نوێکردنەوەی فایلی config
    """
    new_config = {
        "appName": "شابڵۆد پڕۆ",
        "appIcon": "https://example.com/new-icon.png",
        "appDescription": "وەسفێکی نوێ بۆ ئەپڵیکەیشنەکە",
        "downloadLink": "https://apps.apple.com/app/new-id",
        "tutorialLink": "https://youtube.com/new-tutorial"
    }
    
    update_app_config(new_config)


if __name__ == "__main__":
    main()