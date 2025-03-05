import streamlit as st
import base64
import os
from pyairtable import Api

def display_image(file_path):
    st.image(file_path, caption="QR-code voor betaling, €5 per team")

#https://airtable.com/appFQrfgHHc7pQ3Bd/tblnLJ33Eo5q73Cot/viwaUw0FiUO9lpqHh?blocks=hide
def add_submission_to_airtable(name, tournament_type, email, phone, bankrekeningsnummer):
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
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "email_address": email,
            "phone_number": phone,
            "IBAN": bankrekeningsnummer

    }
    table.create(data)

def main():
    st.logo("streamlit-web-app/src/vva71-logo.png")
    st.title("Aanmeldformulier dart-toernooi VVA Achterberg 11 april 2025")
    st.text("Welkom op het aanmeldformulier voor het dart-toernooi van VVA Achterberg op 11 april 2025.")
    st.text("Het toernooi gaat plaatsvinden op vrijdag 11 april 2025 van 18:30 (inloop) en 19:00 (start wedstrijden) bij VVA Achterberg op de Zuidelijke Meentsteeg 33 in Achterberg. U kunt zich aanmelden voor het singlestoernooi, dubbels toernooi, of beide. Kosten voor deelname zijn 5€ per persoon. Vul onderstaande gegevens in om je aan te melden voor het toernooi en betaal het betaalverzoek hieronder.")
    
    # User input for name
    name = st.text_input("Voornaam, achternaam, en dartnaam:")
    tournament_type = st.selectbox("Kies het type toernooi:", ["Singles", "Dubbels", "Singles en dubbels"])
    email = st.text_input("E-mailadres:")
    phone = st.text_input("Telefoonnummer:")
    bankrekeningsnummer = st.text_input("Bankrekeningsnummer (IBAN):")
    
    # Tournament type selection
    

    st.text("QR-code om te betalen, €5 euro per persoon:")
    display_image("streamlit-web-app/src/betalen.png")
    #display_image("betalen.png")
    if st.button("Aanmelden"):
        try:
            add_submission_to_airtable(name, tournament_type, email, phone, bankrekeningsnummer)
            st.success("Aanmelding succesvol ontvangen! Tot 11 april 2025!")
        except Exception as e:
            st.error(f"{e}")

if __name__ == "__main__":
    main()