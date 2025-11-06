# app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="서울 인기 관광지 TOP10 🌏", layout="wide")

st.title("서울 인기 관광지 TOP10 🌏")
st.markdown("""
외국인들이 많이 찾는 **서울의 대표 관광지 10곳**을 지도에 표시했습니다.  
- 마커를 클릭하면 간단한 설명이 나옵니다.  
- 왼쪽 사이드바에서 관광지를 선택하면 해당 위치로 이동합니다.
""")

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]
m = folium.Map(location=seoul_center, zoom_start=12, control_scale=True)

# 관광지 데이터 (이름, 위도, 경도, 설명)
attractions = [
    ("경복궁 Gyeongbokgung Palace", 37.5796, 126.9770, "조선의 대표 궁궐. 수문장 교대식으로 유명합니다."),
    ("창덕궁 Changdeokgung", 37.5794, 126.9910, "유네스코 세계문화유산으로 지정된 궁궐입니다."),
    ("북촌한옥마을 Bukchon Hanok Village", 37.5826, 126.9830, "전통 한옥이 모여 있는 인기 포토존입니다."),
    ("인사동 Insadong", 37.5765, 126.9850, "전통 공예품, 찻집, 기념품 쇼핑 거리입니다."),
    ("명동 Myeongdong", 37.5609, 126.9850, "쇼핑, 화장품, 길거리 음식으로 유명한 거리입니다."),
    ("N서울타워 N Seoul Tower", 37.5512, 126.9882, "서울의 랜드마크 전망대. 야경 명소로도 유명합니다."),
    ("동대문시장 Dongdaemun Market", 37.5700, 127.0079, "패션 도매시장과 야시장으로 유명한 곳입니다."),
    ("홍대 Hongdae", 37.5563, 126.9237, "젊음의 거리, 버스킹과 카페로 유명한 지역입니다."),
    ("코엑스몰 COEX Mall", 37.5110, 127.0595, "대형 쇼핑몰, 별마당 도서관, 아쿠아리움이 있습니다."),
    ("여의도 한강공원 Yeouido Hangang Park", 37.5260, 126.9241, "한강뷰와 피크닉 장소로 인기 많은 공원입니다."),
]

# 지도에 마커 추가
for name, lat, lon, desc in attractions:
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>{name}</b><br>{desc}",
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 출력
st.subheader("🗺️ 관광지도 보기")
st_folium(m, width=1000, height=700)

# 사이드바 이동 기능
st.sidebar.header("📍 빠른 이동")
choice = st.sidebar.selectbox("장소 선택", ["전체 보기"] + [a[0] for a in attractions])

if choice != "전체 보기":
    selected = next(a for a in attractions if a[0] == choice)
    zoom_map = folium.Map(location=[selected[1], selected[2]], zoom_start=16)
    folium.Marker(
        location=[selected[1], selected[2]],
        popup=f"<b>{selected[0]}</b><br>{selected[3]}",
        icon=folium.Icon(color="red", icon="star")
    ).add_to(zoom_map)
    st.subheader(f"📌 {choice} 위치 보기")
    st_folium(zoom_map, width=800, height=500)

st.markdown("---")
st.caption("📊 데이터 출처: TripAdvisor · VisitKorea · Klook (외국인 인기순 기준)")
