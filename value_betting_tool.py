import streamlit as st

st.set_page_config(page_title="Value Betting Tool", layout="centered")
st.title("🎯 Value Betting Einsatzrechner")

st.markdown("""
Gib unten deine Daten ein, um den Value und den optimalen Einsatz zu berechnen.
Die Kelly Light Methode (50 %) wird zur Risikoreduzierung genutzt.
""")

quote = st.number_input("📈 Buchmacherquote", min_value=1.01, step=0.01, format="%.2f")
wk_percent = st.slider("🔍 Deine Einschätzung der Gewinnwahrscheinlichkeit (%)", min_value=1, max_value=100, value=60)
bankroll = st.number_input("💰 Aktuelle Bankroll (€)", min_value=1.0, value=1000.0, step=10.0, format="%.2f")

if st.button("🔎 Berechnen"):
    wk = wk_percent / 100
    value = (quote * wk) - 1

    if value <= 0:
        st.error("Diese Wette hat keinen positiven Erwartungswert (kein Value). Setze lieber nicht.")
    else:
        kelly = bankroll * ((quote * wk - 1) / (quote - 1))
        kelly_light = kelly * 0.5

        st.success("✅ Positive Value-Wette erkannt!")
        st.markdown(f"**Value:** {value:.2%}")
        st.markdown(f"**Optimaler Kelly-Einsatz:** {kelly:.2f} €")
        st.markdown(f"**Kelly Light (50%) Einsatz:** {kelly_light:.2f} €")

        st.markdown("---")
        st.info("Setze idealerweise nicht mehr als den Kelly-Light-Einsatz, um langfristig stabil zu bleiben.")
