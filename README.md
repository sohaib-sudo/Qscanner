# Web Network Scanner tool with user friendly GUI

### **Nmap Installation Process in Your App (Simplified Explanation)**  

#### **1. Checking if Requirements is Installed**
- When the app starts, it checks whether **Nmap** is installed on the system.
- If Requirements is found, the app continues as normal.
- If Requirements is missing, a message appears saying **"Nmap is not installed."**
![installing requerment](https://github.com/user-attachments/assets/b78c92dc-a099-469f-ab14-aaa672af412d)

#### **2. Prompting the User to Install the Requirements**
- A **loading animation** runs while the app checks for Requirements.
- If not found, an **"Install" button** appears for the user to start the installation.
![if not installed](https://github.com/user-attachments/assets/be09cb21-60ed-465c-b7cb-aa511fa85495)

#### **3. Installing Requirements**
- When the user clicks the **Install** button, the app attempts to install Requirements automatically.
- It runs an **Requirements installer file** located in the app’s **"dust"** folder.
- If the installation is successful, a message appears saying **"Installation completed. Please restart the application."**
![installing nmap](https://github.com/user-attachments/assets/3224cd91-15d3-4111-812c-e713360ba932)

#### **4. Restarting the App**
- After installation, the app asks the user to **restart** to check if Nmap is now installed.
- When restarted, the app runs the check again.
- If Requirements is now installed, the user can proceed with scanning.
![restart the app](https://github.com/user-attachments/assets/10bb7c53-6717-4724-9402-5a4ae243e941)

#### **5. Handling Errors**
- If **Requirements cannot be found** in the "dust" folder, an error message appears.
- If **the installation fails**, the app displays a warning to the user.
- If **Requirements is installed but not detected**, the user may need to **add it to the system PATH** manually.

#### **Possible Improvements**
- The app could **automatically download** the latest Requirements installer from the internet if it's missing.
- If an **outdated version** of Requirements is found, the app could suggest an update.

#### **1. Login Interface:**
- The app opens with a login screen built using **CustomTkinter**.
- The user must enter an **email** and **password**.
- There are two main options:
  - **Login**: If the user already has an account, they can log in.
  - **Sign Up**: If the user is new, they can register with a username, email, and password. The data is stored in Firebase.
![the app interface](https://github.com/user-attachments/assets/a8abdf93-b0fc-4e21-bbab-078e95387c6c)

#### **2. After Successful Login:**
- The login interface disappears, and the **main application interface** appears.
- The background updates, and the navigation **sidebar** becomes available.
- A **log frame** appears to display system messages.

- 

#### **3. Main Application Interface (Scanning Features):**
- The user sees an input field labeled **"Enter the URL or IP"** to enter a domain or an IP address.
- Two scan types are available:
  - **Normal Scan**
  - **Deep Scan**  
- A **scan button** (with a scan icon) allows the user to start scanning the entered URL or IP.
![the app home screen](https://github.com/user-attachments/assets/c189b102-7a69-4090-ba45-b08eb531ddc5)

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
  - 
![sacn completed successfully](https://github.com/user-attachments/assets/6c65d96d-699a-4efa-a357-52011497ec39)

#### **5. Saving Scan Results to PDF:**
- The scan results are automatically formatted and saved as a **PDF file** on the user's desktop.
- The PDF includes:
  - The scanned IP address
  - A table of scan results with:
    - Port, State, Service, Version, Status, Update Link
- The app also displays a **message box notification** indicating the scan results were saved successfully.
- 
![another scan pdf](https://github.com/user-attachments/assets/a20d9aaf-c5f6-46f4-a84f-54d6b3562ee3)

#### **6. Uploading Scan Results to GitHub (Future Improvement Needed):**
- Currently, the app **saves results to Firebase**.
![b](https://github.com/user-attachments/assets/c64e6031-0db4-4785-840f-2431b81415c6)

- 
- To upload the scan result PDF to GitHub, you need to add a script using the **GitHub API** to push the file to your repository.




## Overview
This project is a graphical user interface (GUI) application for scanning networks . It is built using `customtkinter` and integrates various features, including Firebase authentication, database storage, and email notifications.

## Features
- **Requirements Integration:** Checks if Requirements is installed and installs it if necessary.
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

