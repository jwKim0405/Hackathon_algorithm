import streamlit as st

# 페이지 제목
st.title("노인을 위한 이야기 플랫폼")

# 개인 정보 입력 섹션
st.header("개인 정보 입력")
gender = st.radio("성별", ["남성", "여성"])
age = st.number_input("나이", min_value=1, max_value=120)
life_graph = st.text_input("당신의 인생 그래프", "")
occupation = st.text_input("직업 여부", "")

if not occupation:
    past_occupation = st.text_input("과거 직업", "")

# 질문지 섹션
st.header("질문지")

# 공통 질문
st.subheader("공통 질문")
memorable_event = st.text_area("당신의 삶에서 가장 기억에 남은 일은 무엇인가요?", "")
regret = st.text_area("당신의 삶에서 가장 후회되는 것이 있다면 무엇인가요?", "")
saddest_moment = st.text_area("당신의 삶에서 가장 슬펐던 것이 있다면 무엇인가요?", "")
greatest_achievement = st.text_area("당신의 삶에서 가장 큰 성취를 말해주세요.", "")

# 연령대별 질문
st.subheader("연령대별 질문")
for decade in ["20", "30", "40", "50", "60"]:
    memorable_event_decade = st.text_area(f"당신의 {decade}대에 있었던 가장 기억에 남는 일을 말해주세요.", "")
    advice_to_younger_self = st.text_area(f"과거로 돌아가 {decade}대의 나에게 해주고 싶은 말이 있다면 무엇인가요?", "")

# 부모님에 대한 질문
st.subheader("부모님에 대한 질문")
parent_story = st.text_area("부모님에 대한 이야기를 들려주세요.", "")
message_to_parents = st.text_area("부모님에게 꼭 하고 싶은 말이 있다면?", "")

# 현재 및 미래 계획
st.subheader("현재 및 미래 계획")
current_goal = st.text_area("올해 목표가 있나요?", "")
future_plans = st.text_area("앞으로의 계획", "")

# 개인화된 질문
st.subheader("개인화된 질문")
if st.checkbox("당신은 누군가에게 엄마/아빠였나요?"):
    good_parent = st.checkbox("당신은 좋은 엄마/아빠였나요?")
    happy_moments = st.text_area("자녀로 인해 행복했던 이야기를 들려주세요.", "")
    challenging_moments = st.text_area("자녀로 인해 힘들었던 이야기를 들려주세요.", "")
    would_be_parent_again = st.checkbox("다시 태어나도 당신의 자녀의 어머니/아버지가 되고 싶으신가요?")
