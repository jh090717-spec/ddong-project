# app.py
import streamlit as st

st.set_page_config(page_title="MBTI → 진로 추천", page_icon="🎯", layout="centered")

st.title("🎯 MBTI로 골라보는 진로 추천기")
st.markdown("친구야~ 너의 MBTI를 골라봐! 해당 유형에 딱 맞는 **진로 2가지**, 어떤 **학과**가 적합한지, 그리고 어떤 **성격**이 그 진로에 잘 맞는지도 알려줄게. 😊")

MBTI_OPTIONS = [
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP",
    "ISFP", "INFP", "INTP", "ESTP", "ESFP",
    "ENFP", "ENTP", "ESTJ", "ESFJ", "ENTJ"
]

data = {
    "ISTJ": [
        {
            "career": "공기업/공무원 🏛️",
            "majors": ["행정학과", "법학과", "경영학과"],
            "personality": "체계적이고 책임감 강함. 규칙과 절차를 잘 따르며 꾸준히 일하는 스타일"
        },
        {
            "career": "회계사/재무 분석가 💼",
            "majors": ["회계학과", "경영학과", "경제학과"],
            "personality": "세부사항을 놓치지 않고 정확성을 중시함. 숫자에 강하고 꼼꼼함"
        }
    ],
    "ISFJ": [
        {
            "career": "간호사/보건의료인 🩺",
            "majors": ["간호학과", "보건학과"],
            "personality": "사려 깊고 타인을 돌보는 성향. 안정적 환경에서 성실히 일함"
        },
        {
            "career": "초등교사/특수교사 ✏️",
            "majors": ["교육학과", "유아교육과"],
            "personality": "인내심 있고 세심함. 학생과의 신뢰를 쌓는 데 강함"
        }
    ],
    "INFJ": [
        {
            "career": "상담심리사/임상심리사 💬",
            "majors": ["심리학과", "사회복지학과"],
            "personality": "공감능력 높고 사람의 내면에 관심 많음. 의미 있는 관계를 중시함"
        },
        {
            "career": "콘텐츠 기획/창작가 ✍️",
            "majors": ["문예창작학과", "미디어학과", "국어국문학과"],
            "personality": "아이디어와 가치에 민감하고 메시지를 잘 전달함"
        }
    ],
    "INTJ": [
        {
            "career": "연구원/데이터 과학자 🔬",
            "majors": ["수학과", "통계학과", "컴퓨터공학과"],
            "personality": "분석적이고 전략적. 복잡한 문제 해결을 즐김"
        },
        {
            "career": "전략기획/컨설턴트 📈",
            "majors": ["경영학과", "경제학과", "산업공학과"],
            "personality": "장기적 플랜을 세우며 구조화된 사고를 좋아함"
        }
    ],
    "ISTP": [
        {
            "career": "기계/전기 기술자 🛠️",
            "majors": ["기계공학과", "전기공학과", "메카트로닉스과"],
            "personality": "실무적이고 손으로 만드는 걸 좋아함. 문제 해결을 직관적으로 함"
        },
        {
            "career": "응급구조대/현장 엔지니어 🚑",
            "majors": ["소방안전학과", "응급구조학과", "공학계열"],
            "personality": "위기 상황에서 침착하고 즉각적으로 대처 가능"
        }
    ],
    "ISFP": [
        {
            "career": "디자이너 (패션/시각) 🎨",
            "majors": ["시각디자인과", "패션디자인과", "공예과"],
            "personality": "미적 감각이 뛰어나고 표현 욕구가 강함. 자유로운 분위기에서 빛남"
        },
        {
            "career": "동물/자연 관련 직업 🐾",
            "majors": ["동물자원학과", "환경학과", "생명과학과"],
            "personality": "따뜻하고 관찰력이 좋음. 자연과 함께 일하는 걸 좋아함"
        }
    ],
    "INFP": [
        {
            "career": "문학/창작가 📚",
            "majors": ["국어국문학과", "문예창작학과", "영문학과"],
            "personality": "이상과 가치를 중시하며 감수성이 풍부함. 자기 표현을 좋아함"
        },
        {
            "career": "NGO/사회복지 활동가 🤝",
            "majors": ["사회복지학과", "국제학과", "사회학과"],
            "personality": "사람과 사회의 의미를 고민함. 도움이 필요한 곳에 헌신적임"
        }
    ],
    "INTP": [
        {
            "career": "소프트웨어 개발자 / 시스템 설계자 💻",
            "majors": ["컴퓨터공학과", "정보통신공학과", "전산학과"],
            "personality": "논리적이고 호기심 많음. 이론을 탐구하고 설계하는 걸 즐김"
        },
        {
            "career": "학술연구/이론물리 등 연구분야 🔭",
            "majors": ["물리학과", "수학과", "전공 심화 연구"],
            "personality": "깊이 있는 사고와 독립적인 탐구 선호"
        }
    ],
    "ESTP": [
        {
            "career": "영업/마케팅 (현장 중심) 🧲",
            "majors": ["경영학과", "광고홍보학과", "무역학과"],
            "personality": "활동적이고 즉흥적인 상황에서 뛰어남. 사람 만나는 걸 좋아함"
        },
        {
            "career": "스포츠/행사 기획 운영 ⚽",
            "majors": ["체육학과", "레저스포츠학과", "경영학과"],
            "personality": "에너지 넘치고 현장 중심적이며 실전 감각이 좋음"
        }
    ],
    "ESFP": [
        {
            "career": "연예/무대 예술가 🎤",
            "majors": ["연극영화과", "무대예술과", "음악과"],
            "personality": "사람들 앞에서 표현하는 걸 즐기고 분위기 메이커"
        },
        {
            "career": "관광/호텔 서비스업 🏨",
            "majors": ["호텔관광학과", "외식조리학과"],
            "personality": "사교적이고 손님 대하는 걸 좋아함. 실무에서 빠르게 적응"
        }
    ],
    "ENFP": [
        {
            "career": "콘텐츠 크리에이터 / PR ✨",
            "majors": ["미디어학과", "광고홍보학과", "커뮤니케이션학과"],
            "personality": "아이디어가 많고 사람 끌어모으는 재주가 있음. 창의력 풍부"
        },
        {
            "career": "창업가 / 스타트업 🔥",
            "majors": ["경영학과", "창업학과", "융합전공"],
            "personality": "새로운 것 도전하는 걸 좋아하고 사람들과 협업 잘함"
        }
    ],
    "ENTP": [
        {
            "career": "제품기획/스타트업 아이디어리더 💡",
            "majors": ["경영학과", "산업공학과", "컴퓨터공학과"],
            "personality": "발상이 기발하고 토론/아이디어 교류를 즐김"
        },
        {
            "career": "변호사/논쟁이 필요한 직업 ⚖️",
            "majors": ["법학과", "정치외교학과"],
            "personality": "논리적이며 설득력 있고 토론에서 강함"
        }
    ],
    "ESTJ": [
        {
            "career": "경영관리자/운영 매니저 🧭",
            "majors": ["경영학과", "산업경영학과"],
            "personality": "조직적이고 리더십 있으며 실행력이 강함"
        },
        {
            "career": "군인/공공행정 관리자 🎖️",
            "majors": ["행정학과", "군사학과"],
            "personality": "규율을 중시하며 책임감으로 팀을 이끔"
        }
    ],
    "ESFJ": [
        {
            "career": "보건/교육 서비스 관리자 🧑‍⚕️👩‍🏫",
            "majors": ["사회복지학과", "교육학과", "간호학과"],
            "personality": "사교적이고 타인을 돌보는 데 기쁨을 느낌. 팀 분위기 조성에 능함"
        },
        {
            "career": "HR/인사 담당자 🤝",
            "majors": ["경영학과", "인사조직전공"],
            "personality": "사람 관리와 조직 문화 형성에 관심 많음"
        }
    ],
    "ENTJ": [
        {
            "career": "CEO/경영 컨설턴트 🏢",
            "majors": ["경영학과", "경제학과", "산업공학과"],
            "personality": "목표 지향적이고 리더십 강함. 큰 그림 보는 데 능함"
        },
        {
            "career": "프로젝트 매니저/전략 담당자 🗺️",
            "majors": ["경영학과", "프로젝트관리학과", "산업공학과"],
            "personality": "조직을 구조화하고 추진하는 능력이 탁월"
        }
    ]
}

st.sidebar.header("시작해볼까?")
selected = st.sidebar.selectbox("너의 MBTI를 골라줘 (15개 중 하나)", MBTI_OPTIONS)

st.markdown("---")
st.subheader(f"🔎 {selected} 유형에게 추천하는 진로")

if selected in data:
    careers = data[selected]
    for i, c in enumerate(careers, 1):
        st.markdown(f"### {i}. {c['career']}")
        st.markdown(f"- **추천 학과:** {', '.join(c['majors'])}")
        st.markdown(f"- **어떤 성격이 잘 맞을까?** {c['personality']}")
        st.markdown("")
    st.info("팁: 위 진로는 타입의 일반적 성향을 바탕으로 한 추천이야. 너만의 경험, 흥미, 가족 상황도 꼭 고려해봐! 💡")
else:
    st.error("아직 해당 유형에 대한 정보가 없어... 😢")

st.markdown("---")
st.markdown("📌 **사용법 팁**: 사이드바에서 MBTI를 바꾸면 바로 다른 추천이 보여. 친구들이랑 비교해보면서 얘기해봐~")
st.markdown("Made with ❤️ — 궁금한 유형 더 추가하거나 설명을 다듬고 싶으면 말해줘!")
