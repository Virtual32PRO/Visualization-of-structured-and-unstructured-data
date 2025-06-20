import streamlit as st
from vectordb import init_collection, retrieve, add_pdf
from llm      import generate

init_collection()

uploaded = st.file_uploader("💾 Dodaj PDF-y", type="pdf", accept_multiple_files=True)
if uploaded:
    for pdf in uploaded:
        add_pdf(pdf, pdf.name)
    st.success(f"Zaindeksowano {len(uploaded)} plik(ów).")

st.title(" RAG-Chat działający na RTX 4070")
question = st.text_input("Zadaj pytanie")



if question:
    ctx, hits = retrieve(question)
    for h in hits:
        score  = h.score
        text   = h.payload["text"][:250].replace("\n", " ") + "…"
        bg     = "#dfffdf" if score > 0.8 else "#2d2d2d"   
        st.markdown(
            f"<div style='background:{bg};"
            f"color:#000;padding:4px 6px;border-radius:6px'>"
            f"<b>{score:.2f}</b>&nbsp; {text}"
            f"</div>",
            unsafe_allow_html=True,
    )

    st.markdown("---")
    st.write(generate(question, ctx))