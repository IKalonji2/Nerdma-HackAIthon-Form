# Custom CSS for the header, background image, and form elements
header_html = """
    <style>
        .stApp {
            background-image: url('https://www.nerdma.co.za/assets/images/landing-vr.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px;
            background-color: white;
            border-bottom: 2px solid #ddd;
            position: fixed;
            top: 40px;
            left: 0;
            right: 0;
            width: 100%;
            z-index: 1000;
        }
        .header img {
            height: 50px;
        }
        .header h1 {
            color: #333;
            font-size: 24px;
            margin: 0;
        }
        .stForm, .stTextInput, .stSelectbox, .stCheckbox {
            background-color: white !important;
            opacity: 1 !important;
            border-radius: 5px;
            padding: 10px;
        }
        .sticky-col {
            position: -webkit-sticky; /* Safari */
            position: sticky;
            top: 120px;  /* Adjust this value based on the height of your header */
        }
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            margin: 20px auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            font-size: 20px;
            text-align: center;
        }
    </style>
    <div class="header">
        <img src="https://www.nerdma.co.za/assets/images/nerdma-logo.png" alt="Company Logo">
        <h1>Nerdma Hack-AI-thon Registration</h1>
    </div>
"""


# Custom CSS for centering the thank you message
centered_css = """
    <style>
        .centered-message {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full viewport height to center vertically */
            text-align: center;
            background-color: transparent;
            padding: 20px;
            border-radius: 8px;
            
        }
    </style>
"""