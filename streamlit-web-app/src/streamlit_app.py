import streamlit as st
import base64
import os
from pyairtable import Api

def display_image(file_path):
    st.image(file_path, caption="QR-code voor betaling, €5 per team")

#https://airtable.com/appFQrfgHHc7pQ3Bd/tblnLJ33Eo5q73Cot/viwaUw0FiUO9lpqHh?blocks=hide
def add_submission_to_airtable(name, tournament_type):
    import requests
    from datetime import datetime
    # Generate uuid
    import uuid
    uuid = uuid.uuid4().hex
    # Airtable API credentials (add to .streamlit/secrets.toml)
    base_id = st.secrets["airtable"]["base_id"]
    table_id = st.secrets["airtable"]["table_id"]
    api = Api(st.secrets["airtable"]["api_key"])
    table = api.table(base_id, table_id)
    data = {

            "Name": uuid,
            "Deelnemer": name,
            "Tournament Type": tournament_type,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    table.create(data)

def main():
    st.title("Dart-toernooi VVA Achterberg 11 april 2025 aanmeldformulier")
    st.text("Welkom bij het aanmeldformulier voor het dart-toernooi van VVA Achterberg op 11 april 2025.")
    st.text("Het toernooi gaat plaatsvinden op vrijdag 11 april 2025 van ... tot ... . U kunt zich aanmelden voor het singlestoernooi en het dubbels toernooi. Kosten voor deelnames zijn ... Vul onderstaande gegevens in om je aan te melden voor het toernooi.")
    
    # User input for name
    name = st.text_input("Voer je naam in:")
    
    # Tournament type selection
    tournament_type = st.selectbox("Kies het type toernooi:", ["Singles", "Doubles"])

    st.text("QR-code voor betaling, €5 euro per team")
    display_image("streamlit-web-app/src/betalen.png")
    #display_image("betalen.png")
    if st.button("Verzend aanmelding"):
        try:
            add_submission_to_airtable(name, tournament_type)
            st.success("Aanmelding succesvol verzonden!")
        except Exception as e:
            st.error(f"{e}")

if __name__ == "__main__":
    main()