#!/usr/bin/env python3
"""수업 관리 대시보드 로컬 서버"""
import http.server
import socketserver
import webbrowser
import os

PORT = 3000
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"수업 관리 대시보드 실행 중: {url}")
    print("종료하려면 Ctrl+C 를 누르세요.")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n서버 종료됨.")
