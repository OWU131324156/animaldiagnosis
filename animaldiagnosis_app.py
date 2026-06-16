import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #f5f0e6, #ffffff);
    }
    </style>
    """,
    unsafe_allow_html=True
)
# アプリのタイトル
st.title("あなたを動物に例えると？")
st.write("いくつかの質問に答えるだけで、あなたの性格を動物に例えます！")

# --------------------------------------------------
# リセットボタン（これが重要）
# --------------------------------------------------
if st.button("🔄 診断しなおす"):
    st.session_state.clear()
    st.rerun()

# --------------------------------------------------
# 質問エリア
# --------------------------------------------------
st.header("📋あなたのことについて教えてください")

# 質問1
q1_action = st.selectbox(
    "1. 休日の過ごし方で、一番近いものはどれですか？",
    [
        "家でゴロゴロ、または一人の時間を楽しむ",
        "友達や家族とアクティブに遊びに行く",
        "カフェや本屋で静かに過ごす"
    ],
    help="直感で選んでください"
)

# 質問2
q2_traits = st.multiselect(
    "2. 自分の性格に当てはまるものをすべて選んでください（複数選択可）",
    ["マイペース", "寂しがり屋", "聞き上手", "負けず嫌い", "計画的"],
    default=["マイペース"],
    help="いくつでも選んでね"
)

# 質問3・4
st.write("最後の質問です。あなたの直感を1〜10の数字で教えてください。")

cat_score = st.number_input(
    "3. ぶっちゃけ、集団行動より単独行動が好き？（1:大嫌い 〜 10:大好き）",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

dog_score = st.number_input(
    "4. 人に褒められるとテンション上がる？（1:別に 〜 10:超上がる）",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

# --------------------------------------------------
# 診断ボタン
# --------------------------------------------------
st.header("🔮 診断結果")

if st.button("🔮 診断する"):

    animal_index = dog_score - cat_score + 5

    st.write("あなたの診断結果は……")

    col1, col2, col3 = st.columns(3)

    # 猫タイプ
    if animal_index <= 3:
        with col1:
            st.header("🐱 猫タイプ")
            st.image("https://static.streamlit.io/examples/cat.jpg")
            st.write("➡️ あなたは**【猫タイプ】**です！")
            st.write("周囲に流されない強い芯を持っています。一人の時間をとても大切にし、居心地の良い場所を見つけるのが得意な天才肌です。")

    # 犬タイプ
    elif animal_index <= 7:
        with col2:
            st.header("🐶 犬タイプ")
            st.image("https://static.streamlit.io/examples/dog.jpg")
            st.write("➡️ あなたは**【犬タイプ】**です！")
            st.write("とても人なつっこく、義理堅い性格です。褒められると伸びるタイプで、周囲の人を笑顔にするハッピーなエネルギーを持っています。")

    # フクロウタイプ
    else:
        with col3:
            st.header("🦉 フクロウタイプ")
            st.image("https://static.streamlit.io/examples/owl.jpg")
            st.write("➡️ あなたは**【フクロウタイプ】**です！")
            st.write("聞き上手で、周囲を冷静によく観察している知性派です。一見おとなしそうに見えて、実はもの凄く深いことを考えているミステリアスな魅力があります。")
