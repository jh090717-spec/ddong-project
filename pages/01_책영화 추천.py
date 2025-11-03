import streamlit as st

st.set_page_config(page_title="MBTI 책🎬영화 추천기", page_icon="🌟")

st.title("🌈 MBTI별 책 & 영화 추천기")
st.write("너의 MBTI를 골라봐! 성격에 딱 맞는 책과 영화 추천해줄게 😎")

# MBTI 목록 (15개)
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP", 
    "INFJ", "INFP", "ENFJ", "ENFP", 
    "ISTJ", "ISFJ", "ESTJ", "ESFJ", 
    "ISTP", "ISFP", "ESFP"
]

# MBTI 선택
user_mbti = st.selectbox("👉 나의 MBTI는?", mbti_list)

# MBTI별 책 + 영화 데이터
recommendations = {
    "INTJ": {
        "books": ["📘 『생각의 탄생』 - 루트번스타인 부부", "📗 『사피엔스』 - 유발 하라리"],
        "movies": ["🎬 인터스텔라", "🧠 인셉션"]
    },
    "INTP": {
        "books": ["📘 『총, 균, 쇠』 - 제레드 다이아몬드", "📗 『이기적 유전자』 - 리처드 도킨스"],
        "movies": ["🎬 매트릭스", "🧠 허(her)"]
    },
    "ENTJ": {
        "books": ["📘 『7가지 성공 습관』 - 스티븐 코비", "📗 『팀장님, 리더십이 뭐예요?』 - 김경일"],
        "movies": ["🎬 아이언맨", "💼 월 스트리트"]
    },
    "ENTP": {
        "books": ["📘 『넛지』 - 리처드 탈러", "📗 『창의성의 즐거움』 - 미하이 칙센트미하이"],
        "movies": ["🎬 월-E", "🧠 빅 쇼트"]
    },
    "INFJ": {
        "books": ["📘 『데미안』 - 헤르만 헤세", "📗 『죽은 시인의 사회』 - N.H.클라인바움"],
        "movies": ["🎬 어바웃 타임", "💫 인사이드 아웃"]
    },
    "INFP": {
        "books": ["📘 『연금술사』 - 파울로 코엘료", "📗 『어린 왕자』 - 생텍쥐페리"],
        "movies": ["🎬 월터의 상상은 현실이 된다", "💫 업(UP)"]
    },
    "ENFJ": {
        "books": ["📘 『사람을 얻는 기술』 - 데일 카네기", "📗 『리더는 마지막에 먹는다』 - 사이먼 시넥"],
        "movies": ["🎬 굿 윌 헌팅", "💞 인턴"]
    },
    "ENFP": {
        "books": ["📘 『미움받을 용기』 - 기시미 이치로", "📗 『무라카미 하루키 단편집』"],
        "movies": ["🎬 인사이드 아웃", "💫 라라랜드"]
    },
    "ISTJ": {
        "books": ["📘 『원칙』 - 레이 달리오", "📗 『나는 나를 경영한다』 - 피터 드러커"],
        "movies": ["🎬 셜록 홈즈", "💼 머니볼"]
    },
    "ISFJ": {
        "books": ["📘 『아몬드』 - 손원평", "📗 『작은 아씨들』 - 루이자 메이 올컷"],
        "movies": ["🎬 포레스트 검프", "💞 원더"]
    },
    "ESTJ": {
        "books": ["📘 『그릿』 - 앤절라 더크워스", "📗 『실행이 답이다』 - 래리 보시디"],
        "movies": ["🎬 더 울프 오브 월스트리트", "💼 킹스맨"]
    },
    "ESFJ": {
        "books": ["📘 『트렌드 코리아 2025』", "📗 『감정 수업』 - 윌리엄 제임스"],
        "movies": ["🎬 미션 임파서블", "💞 인턴"]
    },
    "ISTP": {
        "books": ["📘 『나는 나를 믿는다』 - 조승연", "📗 『초격차』 - 권오현"],
        "movies": ["🎬 테넷", "🚗 분노의 질주"]
    },
    "ISFP": {
        "books": ["📘 『걷는 사람, 하정우』", "📗 『나미야 잡화점의 기적』 - 히가시노 게이고"],
        "movies": ["🎬 리틀 포레스트", "🌿 코코"]
    },
    "ESFP": {
        "books": ["📘 『오늘도 내일도, 나는 나답게』", "📗 『나는 내일, 어제의 너와 만난다』"],
        "movies": ["🎬 위대한 쇼맨", "💫 엘라의 모험"]
    },
}

# 결과 출력
if user_mbti:
    st.subheader(f"✨ {user_mbti} 유형에게 추천하는 책 & 영화 ✨")
    st.write("📚 **책 추천**")
    for book in recommendations[user_mbti]["books"]:
        st.write(f"- {book}")
    st.write("🎬 **영화 추천**")
    for movie in recommendations[user_mbti]["movies"]:
        st.write(f"- {movie}")

st.markdown("---")
st.write("💡 MBTI로 보는 나의 취향, 얼마나 맞는지 댓글로 공유해봐! 😆")
