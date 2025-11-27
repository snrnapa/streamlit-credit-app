import streamlit as st
import requests
import pandas as pd

st.title("Streamlit with Flask API (Sales Data)")

st.write("ボタンを押して、ランダムな売上データフレームを取得します。")

if st.button("APIから売上データを取得"):
    try:
        response = requests.get("http://127.0.0.1:5000/api/sales")
        response.raise_for_status()  # エラーがあれば例外を発生させる
        sales_data = response.json()
        
        if sales_data: # データが空でないことを確認
            df = pd.DataFrame(sales_data)
            st.subheader("取得した売上データ")
            st.dataframe(df)
        else:
            st.info("APIからデータが返されませんでした。")

    except requests.exceptions.RequestException as e:
        st.error(f"APIの呼び出しに失敗しました: {e}")