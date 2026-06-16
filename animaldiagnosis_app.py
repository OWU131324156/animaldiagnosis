import streamlit as st

# アプリのタイトル
st.title("あなたを動物に例えると？")
st.write("いくつかの質問に答えるだけで、あなたの性格を動物に例えます！")


# ------------------------------------------------------------------
# 質問エリア
# ------------------------------------------------------------------

st.header("📋あなたのことについて教えてください")

# ボタンが押されたら、画面を強制的にリバース（再起動）させる

if st.button("診断しなおす"):
    st.rerun()

# if st.button("最初からやり直す"):
#     for key in [
#         "q1",
#         "q2",
#         "cat",
#         "dog",
#         "agreement"
#     ]:
#         if key in st.session_state:
#             del st.session_state[key]
#     st.rerun()
    
# 削除　agreement = st.checkbox("結果を見る")

# 質問1：セレクトボックス
q1_action = st.selectbox(
    label="1. 休日の過ごし方で、一番近いものはどれですか？",
    options=["家でゴロゴロ、または一人の時間を楽しむ", "友達や家族とアクティブに遊びに行く", "カフェや本屋で静かに過ごす"],
    help="直感で選んでください",
    key="q1"
)

# 質問2：マルチセレクト
q2_traits = st.multiselect(
    label="2. 自分の性格に当てはまるものをすべて選んでください（複数選択可）",
    options=["マイペース", "寂しがり屋", "聞き上手", "負けず嫌い", "計画的"],
    default=["マイペース"],
    help="いくつでも選んでね",
    key="q2"
)


# 質問3＆4：テキスト入力
st.write("最後の質問です。あなたの直感を1〜10の数字で教えてください。")
cat_score = st.number_input(
    "3. ぶっちゃけ、集団行動より単独行動が好き？（1:大嫌い 〜 10:大好き）",
    min_value=1,
    max_value=10,
    value=5,
    step=1,
    key="cat"
)

dog_score = st.number_input(
    "4. 人に褒められると、めちゃくちゃテンションが上がる？（1:別に 〜 10:超上がる）",
    min_value=1,
    max_value=10,
    value=5,
    step=1,
    key="dog"
)

agreement = st.checkbox("結果を見る", key="agreement")

# ------------------------------------------------------------------
# 診断結果エリア
# ------------------------------------------------------------------

st.header("🔮 診断結果")

# チェックボックスがONで、かつ入力欄が空っぽじゃないときだけ診断
if agreement and cat_score and dog_score:
   
    # c_val = float(cat_score)
    # d_val = float(dog_score)

    c_val = cat_score
    d_val = dog_score
    

    # # もし0以下の数字が入った場合の安全対策
    # if c_val <= 0:
    #     c_val = 1.0
    
    # 足し引きの点数計算
    animal_index = d_val - c_val + 5
    
    st.write("すべての質問が出揃いました。あなたの診断結果は……")
    
    col1, col2, col3 = st.columns(3)
    
    # パターン1：猫タイプ
    if animal_index <= 3.0:
        with col1:
            st.header("🐱 マイペースな猫タイプ")
            st.image("https://static.streamlit.io/examples/cat.jpg", caption="自由を愛する猫")
        st.write("➡️ あなたは**【猫タイプ】**です！")
        st.write("周囲に流されない強い芯を持っています。一人の時間をとても大切にし、居心地の良い場所を見つけるのが得意な天才肌です。")
        
    # パターン2：犬タイプ
    elif 3.0 < animal_index <= 7.0:
        with col2:
            st.header("🐶 素直でフレンドリーな犬タイプ")
            st.image("https://static.streamlit.io/examples/dog.jpg", caption="愛され上手な犬")
        st.write("➡️ あなたは**【犬タイプ】**です！")
        st.write("とても人なつっこく、義理堅い性格です。褒められると伸びるタイプで、周囲の人を笑顔にするハッピーなエネルギーを持っています。")
        
    # パターン3：フクロウタイプ）
    else:
        with col3:
            st.header("🦉 知的なフクロウタイプ")
            st.image("https://static.streamlit.io/examples/owl.jpg", caption="冷静に見つめるフクロウ")
        st.write("➡️ あなたは**【フクロウタイプ】**です！")
        st.write("聞き上手で、周囲を冷静によく観察している知性派です。一見おとなしそうに見えて、実はもの凄く深いことを考えているミステリアスな魅力があります。")
else:
    st.write("👆 上にある「結果を見る」にチェックを入れると、ここに診断結果が表示されます！")
