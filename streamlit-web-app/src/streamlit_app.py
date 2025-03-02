import streamlit as st
import base64
import streamlit.components.v1 as components

def display_image(file_path):
    st.image(file_path, caption="QR-code voor betaling, €5 per team")


def add_submission_to_sharepoint(name, tournament_type):
    from office365.sharepoint.client_context import ClientContext
    from office365.runtime.auth.user_credential import UserCredential

    site_url = st.secrets["sharepoint"]["site_url"]
    username = st.secrets["sharepoint"]["username"]
    password = st.secrets["sharepoint"]["password"]
    list_name = st.secrets["sharepoint"]["list_name"]

    ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
    sp_list = ctx.web.lists.get_by_title(list_name)
    item_properties = {
        "Title": "aanmelding",
        "Name": name,
        "Toernooi_type": tournament_type
    }
    sp_list.add_item(item_properties)
    ctx.execute_query()
    return True

def main():
    st.title("Dart-toernooi VVA Achterberg 11 april 2025 aanmeldformulier")
    st.text("Welkom bij het aanmeldformulier voor het dart-toernooi van VVA Achterberg op 11 april 2025.")
    st.text("Het toernooi gaat plaatsvinden op vrijdag 11 april 2025 van ... tot ... . U kunt zich aanmelden voor het singlestoernooi en het dubbels toernooi. Kosten voor deelnames zijn ... Vul onderstaande gegevens in om je aan te melden voor het toernooi.")
    
    # User input for name
    name = st.text_input("Voer je naam in:")
    
    # Tournament type selection
    tournament_type = st.selectbox("Kies het type toernooi:", ["Singles", "Doubles"])

    st.write("List name from secrets:", st.secrets["sharepoint"]["list_name"])
    st.text("QR-code voor betaling, €5 euro per team")
    display_image("streamlit-web-app/src/betalen.png")
    
    if st.button("Verzend aanmelding"):
        try:
            add_submission_to_sharepoint(name, tournament_type)
            st.success("Aanmelding succesvol verzonden!")
        except Exception as e:
            st.error(f"Aanmelding opgeslagen maar mislukt om naar SharePoint te uploaden: {e}")
    else:
        st.error("Vul alstublieft alle velden in.")

if __name__ == "__main__":
    main()