import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title='Seoul Top 10 (Folium)', layout='wide')

st.title('서울 인기 관광지 Top 10 — 외국인들이 좋아하는 곳 🌏🇰🇷')
st.markdown('''
아래 지도는 외국인 관광객에게 인기 있는 **서울의 주요 관광지 Top 10**을 표시합니다.
- 마커를 클릭하면 간단한 설명을 볼 수 있고,  
- 사이드바에서 장소를 선택하면 해당 지점으로 확대합니다.
''')

# 서울 중심 좌표
seoul_center = (37.5665, 126.9780)
m = folium.Map(location=seoul_center, zoom_start=12, control_scale=True)

# 외국인들이 좋아하는 서울 관광지 Top 10
attractions = [
    ("Gyeongbokgung Palace", 37.5796, 126.9770, "경복궁 — 조선의 대표 궁궐로 의장 교대식을 볼 수 있습니다."),
    ("Changdeokgung Palace", 37.5794, 126.9910, "창덕궁 — 유네스코 세계문화유산이며 후원이 유명합니다."),
    ("Bukchon Hanok Village", 37.5826, 126.9830, "북촌한옥마을 — 전통 한옥이 모여 있는 예쁜 골목 마을."),
    ("Insadong", 37.5765, 126.9850, "인사동 — 전통 공예품과 찻집, 기념품 쇼핑으로 유명."),
    ("Myeongdong Shopping Street", 37.5609, 126.9850, "명동 — 뷰티/패션 쇼핑과 길거리 음식의 중심지."),
    ("N Seoul Tower (Namsan)", 37.5512, 126.9882, "N서울타워 — 서울 시내를 한눈에 보는 전망대."),
    ("Dongdaemun Market", 37.5700, 127.0079, "동대문 — 패션 도매/쇼핑, 밤에도 활기찬 시장."),
    ("Hongdae (Hongik Univ. area)", 37.5563, 126.9237, "홍대 — 젊음의 거리, 공연과 카페가 많습니다."),
    ("COEX Mall / Starfield", 37.5110, 127.0595, "코엑스몰 — 대형 쇼핑몰과 아쿠아리움, 스타필드."),
    ("Yeouido Hangang Park", 37.5260, 126.9241, "여의도 한강공원 — 한강변 산책과 피크닉 명소.")
]

# 마커 추가
for name, lat, lon, desc in attractions:
    popup_html = f"<b>{name}</b><br>{desc}"
    folium.Marker(
        location=(lat, lon),
        popup=popup_html,
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 표시
st.subheader('지도 보기')
map_data = st_folium(m, width=1000, height=700)

# 사이드바: 특정 관광지로 이동
st.sidebar.title("🎯 빠르게 이동")
choice = st.sidebar.selectbox("장소 선택", ["전체 보기"] + [a[0] for a in attractions])

if choice != "전체 보기":
    sel = next(a for a in attractions if a[0] == choice)
    sel_map = folium.Map(location=(sel[1], sel[2]), zoom_start=16, control_scale=True)
    folium.Marker(
        location=(sel[1], sel[2]),
        popup=f"<b>{sel[0]}</b><br>{sel[3]}",
        tooltip=sel[0],
        icon=folium.Icon(color="red", icon="star")
    ).add_to(sel_map)
    st.subheader(f"📍 {choice} 위치 보기")
    st_folium(sel_map, width=800, height=500)

st.markdown("---")
st.markdown("데이터 출처: TripAdvisor, VisitKorea, Klook 등 외국인 인기 순위 기반 선정.")
