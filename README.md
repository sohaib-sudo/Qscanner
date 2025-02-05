# Web Network Scanner GUI


#### **1. Login Interface:**
- The app opens with a login screen built using **CustomTkinter**.
- The user must enter an **email** and **password**.
- There are two main options:
  - **Login**: If the user already has an account, they can log in.
  - **Sign Up**: If the user is new, they can register with a username, email, and password. The data is stored in Firebase.

#### **2. After Successful Login:**
- The login interface disappears, and the **main application interface** appears.
- The background updates, and the navigation **sidebar** becomes available.
- A **log frame** appears to display system messages.

#### **3. Main Application Interface (Scanning Features):**
- The user sees an input field labeled **"Enter the URL or IP"** to enter a domain or an IP address.
- Two scan types are available:
  - **Normal Scan**
  - **Deep Scan**  
- A **scan button** (with a scan icon) allows the user to start scanning the entered URL or IP.

#### **4. Scanning Process:**
- The app processes the input URL and converts it to an IP address.
- It then runs an **Nmap scan** using different command options based on the scan type.
- The scan results are displayed in a **scrollable results frame**, showing:
  - Open ports
  - Service running on the port
  - Software version
  - Whether the software is outdated (⚠️ Outdated flag)
  - A button to **update** outdated software (redirects to update resources)
  - A button linking to known **vulnerabilities (CVE IDs)** found in security databases.

#### **5. Saving Scan Results to PDF:**
- The scan results are automatically formatted and saved as a **PDF file** on the user's desktop.
- The PDF includes:
  - The scanned IP address
  - A table of scan results with:
    - Port, State, Service, Version, Status, Update Link
- The app also displays a **message box notification** indicating the scan results were saved successfully.

#### **6. Uploading Scan Results to GitHub (Future Improvement Needed):**
- Currently, the app **saves results to Firebase**.
- To upload the scan result PDF to GitHub, you need to add a script using the **GitHub API** to push the file to your repository.




## Overview
This project is a graphical user interface (GUI) application for scanning networks using Nmap. It is built using `customtkinter` and integrates various features, including Firebase authentication, database storage, and email notifications.

## Features
- **Nmap Integration:** Checks if Nmap is installed and installs it if necessary.
- **GUI Interface:** A user-friendly interface using `customtkinter`.
- **Login & Signup System:** User authentication with Firebase.
- **Scan Types:** Supports both normal and deep scans.
- **Vulnerability Check:** Fetches the latest vulnerabilities and updates for detected services.
- **Scan Results Storage:** Saves scan results in Firebase and as a PDF.
- **Email Notifications:** Sends scan reports via email using Postmark.

## Requirements
Make sure you have the following dependencies installed:
- Python 3.x
- `customtkinter`
- `firebase-admin`
- `googlesearch-python`
- `reportlab`
- `pillow`
- `sendgrid`
- `postmarker`

Install dependencies using:
```sh
pip install customtkinter firebase-admin googlesearch-python reportlab pillow sendgrid postmarker
```

## Installation & Usage
1. **Clone the Repository**
```sh
git clone https://github.com/sohaib-sudo/qscanner.git
cd qscanner
```

2. **Run the Application**
```sh
python main_app.py
```

3. **Login/Signup**
- Use your credentials to log in.
- Sign up for a new account if you don't have one.

4. **Start Scanning**
- Enter a URL or IP address.
- Choose scan type (Normal or Deep).
- Click the **Scan** button to analyze the target.

5. **View Results**
- The scan results, including detected services and vulnerabilities, are displayed in the GUI.
- Optionally, export the scan results as a PDF.
- Scan data is stored in Firebase for record-keeping.

6. **Receive Reports via Email**
- The scan report is automatically sent to the configured email address.

## File Structure
```
/your_project_directory
│-- main_app.py                 # Main application script
│-- dust/                   # Contains required assets (fonts, executables, etc.)
│-- sources/                # Stores images and UI elements
│-- README.md               # Documentation file
```

## Firebase Setup
1. Create a Firebase project.
2. Download the service account key (`scann.json`) and place it in the `dust/` folder.
3. Update the `databaseURL` in `main_app.py` to match your Firebase database.

## Contributing
Feel free to contribute to this project! To get started:
1. Fork the repository.
2. Create a new branch (`feature-name`).
3. Commit your changes.
4. Push to your fork and create a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
- **Your Name** - [GitHub Profile](https://github.com/sohaib-sudo/)

