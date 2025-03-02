import streamlit as st
import base64

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def save_to_database(name, tournament_type, entrance_fee):
    with open("submissions.txt", "a", encoding="utf-8") as f:
        f.write(f"{name},{tournament_type},{entrance_fee}\n")
    return True

def main():
    st.title("Dart-toernooi VVA Achterberg 11 april 2025 aanmeldformulier")
    st.text("Welkom bij het aanmeldformulier voor het dart-toernooi van VVA Achterberg op 11 april 2025.")
    st.text("Het toernooi gaat plaatsvinden op vrijdag 11 april 2025 van ... tot ... . U kunt zich aanmelden voor het singlestoernooi en het dubbels toernooi. Kosten voor deelnames zijn ... Vul onderstaande gegevens in om je aan te melden voor het toernooi.")
    # User input for name
    name = st.text_input("Voer je naam in:")
    
    # Tournament type selection
    tournament_type = st.selectbox("Kies het type toernooi:", ["Singles", "Doubles"])

    # Entrance fee (for display and saving)
    entrance_fee = 5

    st.text("QR-code voor betaling, €5 euro per team")
    display_pdf("QR_Rabobank_Test_2025-03-02.pdf")
    
    if st.button("Verzend aanmelding"):
        if name and tournament_type:
            save_to_database(name, tournament_type, entrance_fee)
            st.success("Aanmelding succesvol verzonden!")
        else:
            st.error("Vul alstublieft alle velden in.")

if __name__ == "__main__":
    main()