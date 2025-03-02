# Streamlit Dart Toernooi Aanmeldpagina

This project is a Streamlit web application designed for Dutch users to register for singles or doubles dart tournaments. The application allows users to enter their names, generates a QR code for payment of the entrance fee, and includes a submit button to save the data.

## Project Structure

```
streamlit-web-app
├── src
│   ├── streamlit_app.py        # Main entry point of the Streamlit application
│   ├── components
│   │   └── qr_code.py          # Functions to generate QR codes for payments
│   └── utils
│       └── database.py         # Functions to save user data securely
├── requirements.txt            # Project dependencies
├── Procfile                    # Deployment configuration
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd streamlit-web-app
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can run the Streamlit application locally with:
   ```
   streamlit run src/streamlit_app.py
   ```

## Usage

- Open the application in your web browser.
- Enter your name and select the tournament type (singles or doubles).
- A QR code will be generated for the payment of the entrance fee.
- Click the submit button to save your registration.

## Deployment

To deploy the application to the cloud, ensure that the `Procfile` is correctly configured, and follow the deployment instructions for your chosen cloud platform.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.