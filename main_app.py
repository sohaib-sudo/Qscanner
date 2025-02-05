import customtkinter as ctk
import subprocess
import random
from googlesearch import search
import socket
import firebase_admin
from firebase_admin import credentials, db, auth
import webbrowser
import threading
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from tkinter import font as tkfont
import os
from tkinter import messagebox
import time
from pathlib import Path
import sys
import platform
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64
from postmarker.core import PostmarkClient









if getattr(sys, 'frozen', False):
    # If running as a bundled executable
    base_path = Path(sys._MEIPASS)
else:
    # If running as a script
    base_path = Path(__file__).resolve().parent

dust_folder = base_path / "dust"
sources_folder = base_path / "sources"
bundled_nmap_path = base_path / "nmap.exe"


font_path = dust_folder/"arialroundedmtbold.ttf"
pdfmetrics.registerFont(TTFont("ArialRoundedMTBold", font_path))




# Check if Nmap is installed on the system
sss = None
def check_nmap_installed():
    """Check if Nmap is installed on the system."""
    try:
        # Get the parent directory of the current working directory
        parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
        
        # Run the 'nmap --version' command in the parent directory
        result = subprocess.run(["nmap", "--version"], capture_output=True, text=True, check=True, cwd=parent_dir)
        
        # Check if the output contains "Nmap version"
        if "Nmap version" in result.stdout:
            sss = 1  # Nmap is installed
        else:
            sss = 0  # Nmap is not installed

    except (subprocess.CalledProcessError, FileNotFoundError):
        sss = 0  # If Nmap isn't found or an error occurs

    return sss

# Example of usage
print(check_nmap_installed())




def install_nmap():
    """Install Nmap by running the nmap.exe file in the dust folder."""
    try:
        nmap_exe_path = dust_folder / "nmap.exe"
        if nmap_exe_path.exists():
            subprocess.run([str(nmap_exe_path)], check=True)
            messagebox.showinfo("Installation", "Nmap installation completed. Please restart the application.")
            restart_app()
        else:
            messagebox.showerror("Installation Error", "nmap.exe not found in the dust folder.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Installation Error", f"An error occurred during installation: {e}")




        
def restart_app():
    """Restart the application to recheck installation."""
    root.destroy()
    main()

def main_app_logic():
    """The main logic of the application once Nmap is confirmed installed."""
    messagebox.showinfo("Success", "Nmap is installed. Application will now run normally.")
    # Add your main app logic here

def center_window(window, width, height):
    """Centers a Tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def main():
    global root
    root = tk.Tk()

    # Set initial window dimensions (important for centering)
    width = 500
    height = 300
    root.geometry(f"{width}x{height}")

    # Center the window after setting its size
    center_window(root, width, height)

    root.title("Nmap Installer Check")
    
    

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    font_path = dust_folder / "arialroundedmtbold.ttf"

# Ensure the font file is registered
    font_name = "Arial Rounded MT Bold"  # Set the font name to use
    if font_path.exists():
        tkfont.nametofont("TkDefaultFont").configure(family=font_name)
    else:
        print(f"Font not found at: {font_path}")

# Main frameqqqqqq
    main_frame = ctk.CTkFrame(master=root)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Labels
    label = ctk.CTkLabel(
        master=main_frame,
        text="Installing Requirements...",
        font=(font_name, 20, "bold")
    )
    label.pack(pady=20)

    spinner_label = ctk.CTkLabel(
        master=main_frame,
        text="",
        font=(font_name, 20, "bold")
    )
    spinner_label.pack()

    spinner_frames = ["|", "/", "-", "\\"]  # Spinner frames

    def animate():
        for frame in spinner_frames * 10:  # 10 iterations (4 seconds total)
            spinner_label.configure(text=frame)
            root.update()
            time.sleep(0.1)

    # Check if Nmap is installed
        if check_nmap_installed():
        # Remove spinner and loading text
            spinner_label.destroy()
            label.destroy()

        # Success message
            success_label = ctk.CTkLabel(
                master=main_frame,
                text="All The Requirements Are Installed!",
                font=("Arial Rounded MT Bold", 20, "bold")  # Correct font family name
            )
            success_label.pack(pady=20)


        # Load and display the "check" image
            check_path = sources_folder / "gg.png"
            check_image = Image.open(check_path)
            check_image = check_image.resize((30, 30))  # Resize the image if necessary
            check_image = ImageTk.PhotoImage(check_image)

        # Display continue button
            continue_button = ctk.CTkButton(
                master=main_frame,
                corner_radius=12,
                fg_color="transparent",
                hover_color="#C850C0",
                border_color="#FFCC70",
                border_width=2,
                image=check_image,
                font=("Arial Rounded MT Bold", 20, "bold"),
                text=" Continue ",
                compound="right",  # Put the image on the right side of the text
                command=root.destroy,
                width=300
            )
            continue_button.pack(pady=10)
        else:
        # Update loading text to indicate failure
            label.configure(text="Nmap is not installed.")
            spinner_label.destroy()

        # Display install button only if Nmap is not installed
            install_button = ctk.CTkButton(
                master=main_frame,
                corner_radius=12,
                fg_color="transparent",
                hover_color="#C850C0",
                border_color="#FFCC70",
                font=("Arial Rounded MT Bold", 20, "bold"),  
                border_width=2,
                text="Install",
                command=install_nmap,  # The install_nmap function is linked to the button click
                width=300
            )
            install_button.pack(pady=10)


    root.after(100, animate)
    root.mainloop()

if __name__ == "__main__":
    main()







# Firebase setup
cred = credentials.Certificate(dust_folder/"scann.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://testscan-f28dc-default-rtdb.firebaseio.com/'})

# Initialize main app window
def center_window(window, width, height):
    """
    Centers the given window on the screen, accounting for window decorations.
    """
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the top-left corner coordinates
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Adjust `y` to compensate for window decorations (like title bars)
    y = max(0, y - 10)  # Adjust by 10 pixels; tweak this if necessary

    # Set the geometry of the window
    window.geometry(f"{width}x{height}+{x}+{y}")

# Create the CTk app
app = ctk.CTk()

# Set the dimensions of the app
width = 1200
height = 660

# Center the app on the screen
center_window(app, width, height)

# Set the title of the app
app.title("My Tester")
# ... rest of your code

# Load and set the background image
bg_image = Image.open(dust_folder/"background.png")  # Replace with your image file path
bg_image = bg_image.resize((width, height))  # Resize the image to match the window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the image as background
bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
bg_label.place(relwidth=1, relheight=1)






main_frame = ctk.CTkFrame(app, width=200, height=200)  # 200x200 for pixel-based sizing

# Configure the grid for 20x20 (units can depend on the pixel size)
main_frame.grid(row=0, column=1, padx=(50, 30), pady=(30, 30), sticky="nsew")

# Set grid column and row weight so that the frame expands properly
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)



# Load icons
email_icon_path =sources_folder/"person.png"
person_icon_path = sources_folder/"email.png"  # Replace with the actual path to the person icon
lock_icon_path = sources_folder/"lock.png"  # Replace with the actual path to the lock icon

person_icon = ImageTk.PhotoImage(Image.open(person_icon_path).resize((20, 20)))
lock_icon = ImageTk.PhotoImage(Image.open(lock_icon_path).resize((20, 20)))
email_icon = ImageTk.PhotoImage(Image.open(email_icon_path).resize((20, 20)))



# Log frame to display messages within the app
# Create the log frame and text box
log_frame = ctk.CTkFrame(app, width=700, height=100)
log_frame.grid(row=1, column=1, padx=(30, 30), pady=(10, 10), sticky="nsew")

log_text = ctk.CTkTextbox(log_frame, width=600, height=80)
log_text.pack(padx=10, pady=10)

# Hide the log frame initially
log_frame.grid_remove()

# Function to add a log message
def add_log(message):
    log_text.insert("end", message + "\n")
    log_text.yview("end")  # Auto-scroll to the bottom

# Example code to show the log frame later


    
    



# Load the image for the app logo or any other image
logo_path = sources_folder/"374970.png"  # Replace with the actual path to the logo image
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((90, 90))  # Resize the image if necessary
logo_image = ImageTk.PhotoImage(logo_image)


# Add the logo image to the main frame, centered above the input fields
logo_label = ctk.CTkLabel(master=main_frame, image=logo_image, text="")  # Set text to empty string
logo_label.grid(row=0, column=0, columnspan=2, padx=(100, 10), pady=(20, 10), sticky="n")
logo_label.place(x=280, y=130)

# Load the image for the app logo or any other image
se_path = sources_folder/"se.png"  # Replace with the actual path to the logo image
se_image = Image.open(se_path)
se_image = se_image.resize((500, 500))  # Resize the image if necessary
se_image = ImageTk.PhotoImage(se_image)


# Add the logo image to the main frame, centered above the input fields
se_label = ctk.CTkLabel(master=main_frame, image=se_image, text="")  # Set text to empty string
se_label.grid(row=0, column=0, columnspan=2, padx=(100, 10), pady=(20, 10), sticky="n")
se_label.place(x=560, y=90)





# Adjusting the layout of the input fields and labels to make them larger
email_label = ctk.CTkLabel(
    master=main_frame,
    image=person_icon,
    compound="left",
    text="  Email:",
    font=("Arial Rounded MT Bold", 18, "bold")
)
email_label.grid(row=1, column=0, padx=(140, 10), pady=(10, 0), sticky="w")
email_label.place(x=150, y=250)

email_entry = ctk.CTkEntry(
    master=main_frame,
    width=350,
    font=("Arial Rounded MT Bold", 13, "bold"),
    border_color="lightblue"
)
email_entry.grid(row=2, column=0, padx=(140, 10), pady=(0, 10))
email_entry.place(x=150, y=280)

global email
email = email_entry.get()

password_label = ctk.CTkLabel(
    master=main_frame,
    image=lock_icon,
    compound="left",
    text="  Password:",
    font=("Arial Rounded MT Bold", 18, "bold")
)
password_label.grid(row=3, column=0, padx=(140, 10), pady=(10, 0), sticky="w")
password_label.place(x=150, y=330)

password_entry = ctk.CTkEntry(
    master=main_frame,
    width=350,
    show="*",
    font=("Arial Rounded MT Bold", 13, "bold"),
    border_color="lightblue"
)
password_entry.grid(row=4, column=0, padx=(140, 10), pady=(0, 10))
password_entry.place(x=150, y=360)

# Username entry (hidden initially) - adjusting size
username_label = ctk.CTkLabel(
    master=main_frame,
    image=email_icon,
    compound="left",
    text="Username:",
    font=("Arial Rounded MT Bold", 18, "bold")
)

username_entry = ctk.CTkEntry(
    master=main_frame,
    width=350,
    font=("Arial Rounded MT Bold", 13, "bold"),
    border_color="lightblue"
)

def show_username_field():
    username_label.grid(row=5, column=0, padx=(140, 10), pady=(10, 0), sticky="w")
    username_entry.grid(row=6, column=0, padx=(140, 10), pady=(0, 10))
    username_label.place(x=150, y=410)
    username_entry.place(x=150, y=440)
    login_button.place(x=170, y=500)
    signup_button.place(x=170, y=550)

    






# Signup function
def signup():
    show_username_field()  # Show username field when signup button is clicked
    
    def complete_signup():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        if not email or not password or not username:
            messagebox.showerror("Signup Error", "Please fill in all fields.")
            return

        try:
            # Create user in Firebase Auth
            user = auth.create_user(email=email, password=password, display_name=username)
            
            # Add user to Realtime Database
            db.reference("accounts").push({
                "username" : username,
                "email": email,
                "password": password
            })

            add_log(f"User created successfully: {user.uid}")
            messagebox.showinfo("Signup Successful", f"Account created for {username} ({email})")
        except Exception as e:
            add_log(f"Signup failed: {e}")
            messagebox.showerror("Signup Error", f"Error: {e}")

    # Change the button to complete the signup process
    signup_button.configure(text="Complete Signup", command=complete_signup)

# Login function
def login():
    global email
    
    email = email_entry.get()  # Retrieve email from the login form
    password = password_entry.get()  # Retrieve password from the login form

    if not email or not password:
        messagebox.showerror("Login Error", "Please enter both email and password.")
        return

    try:
        # Authenticate user with Firebase
        email = auth.get_user_by_email(email)
        
        messagebox.showinfo("Welcome", f"You're logged in ^_^")
        
        bg_label.destroy()

        # Sidebar setup (do this BEFORE resizing)
        sidebar_frame = ctk.CTkFrame(app, width=140, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsw")

        switch_var = ctk.StringVar(value="dark")
        switch = ctk.CTkSwitch(
            master=sidebar_frame,
            text="Dark Mode",
            variable=switch_var,
            onvalue="dark",
            offvalue="light",
            font=("Arial Rounded MT Bold", 13, "bold"),
            command=lambda: ctk.set_appearance_mode(switch_var.get())
        )
        switch.grid(row=4, column=0, padx=20, pady=10)
        
        def show_log():
            log_frame.grid()  # Re-add the frame to the grid
            
        

# Simulate showing the log frame after some operation
        app.after(0, show_log)  # Show the log frame after 2 seconds



        main_interface()  # Proceed to main interface
    except Exception as e:
        add_log(f"Login failed: {e}")
        messagebox.showerror("Login Error", f"Authentication failed: {e}")




# Load Google icon image (ensure you have 'google_icon.png' in the same directory or specify the path)
google_icon = Image.open(sources_folder/"google_icon.png")
google_icon = google_icon.resize((25, 25))  # Resize the icon to fit the button
google_icon = ImageTk.PhotoImage(google_icon)

# Create the 'Sign up with Google' button
signup_button = ctk.CTkButton(
    master=main_frame, 
    corner_radius=12,
    font=("Arial Rounded MT Bold", 17, "bold"),
    fg_color="transparent",
    hover_color="#C850C0",
    border_color="#FFCC70",
    border_width=2,
    text=" Sign up with ", 
    image=google_icon, 
    compound="right",  # Put the image on the left side of the text
    command=signup, 
    width=300
)
signup_button.grid(row=7, column=0, columnspan=2, padx=(140, 10), pady=(5, 10), sticky="n")
signup_button.place(x=170, y=470)

# Create the 'Log in' button
login_button = ctk.CTkButton(
    master=main_frame, 
    corner_radius=12,
    fg_color="transparent",
    font=("Arial Rounded MT Bold", 17, "bold"),
    hover_color="#C850C0",
    border_color="#FFCC70",
    border_width=2,
    text="Log in", 
    command=login, 
    width=300
)
login_button.grid(row=8, column=0, columnspan=2, padx=(140, 10), pady=(5, 10), sticky="n")
login_button.place(x=170, y=415)



# Define main application interface after login
def main_interface():
    
    
    
    # Clear the main_frame for the scanning interface after login
    for widget in main_frame.winfo_children():
        widget.destroy()

    url_label = ctk.CTkLabel(master=main_frame, text="Enter the URL or IP:",font=("Arial Rounded MT Bold", 13, "bold"))
    url_label.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="w")
    url_entry = ctk.CTkEntry(master=main_frame, width=300)
    
    url_entry.grid(row=1, column=1, padx=(10, 20), pady=(10, 10))
    
    
    messagebox.showinfo("credit", f"Sohaib Check my GitHub Repository The Link In The PDF ;)")

    scan_type_var = ctk.StringVar(value="normal")  # Default to normal scan

    # Radio buttons for scan type selection
    normal_radio = ctk.CTkRadioButton(master=main_frame, text="Normal Scan", variable=scan_type_var, value="normal",font=("Arial Rounded MT Bold", 13, "bold"))
    normal_radio.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="w")
    deep_radio = ctk.CTkRadioButton(master=main_frame, text="Deep Scan", variable=scan_type_var, value="deep",font=("Arial Rounded MT Bold", 13, "bold"))
    deep_radio.grid(row=2, column=1, padx=(10, 20), pady=(10, 10), sticky="w")

    result_frame = ctk.CTkScrollableFrame(master=main_frame, width=900, height=300)
    result_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(10, 20), sticky="nsew")

    # Function to process the URL input: remove "https://" and anything after the first "/"
    def process_url(input_url):
        # Remove "https://" or "http://" if present
        if input_url.startswith("https://"):
            input_url = input_url[8:]
        elif input_url.startswith("http://"):
            input_url = input_url[7:]

        # Keep only the domain part before the first "/"
        domain = input_url.split("/")[0]
        return domain

    # Function to resolve a URL to an IP address
    def resolve_to_ip(input_url):
        try:
            return socket.gethostbyname(input_url)
        except socket.gaierror as e:
            add_log(f"Error resolving URL: {e}")
            return None

    # Function to simulate and display the latest version
    def simulate_latest_version(service):
        latest_version = f"{service} {random.randint(1, 5)}.{random.randint(0, 9)}"
        search_query = f"nvd {service}"
        search_results = search(search_query, num_results=1)
        update_url = next(search_results, "https://google.com")
        return latest_version, update_url

    # Function to run the scan
    def run_scan(ip_or_url):
        domain = process_url(ip_or_url)  # Process the URL to get the domain
        ip = resolve_to_ip(domain) if not domain.replace('.', '').isdigit() else domain
        if not ip:
            add_log("Invalid IP or URL.")
            return

        command = ["nmap", "-sV", "-T4", "-O", "-F", "--version-light", ip]
        if scan_type_var.get() == "deep":
            command.append("-A")  # Add deep scan option

        if command:
            def scan_task():
                try:
                    add_log(f"Scanning IP: {ip}...")
                    creationflags = subprocess.CREATE_NO_WINDOW if platform.system() == "Windows" else 0
                    result = subprocess.run(command, capture_output=True, text=True, check=True,creationflags=creationflags)
                    output = result.stdout
                    display_results(output, ip)
                except subprocess.CalledProcessError as e:
                    output = f"An error occurred: {e.stderr}"
                    display_results(output, ip)
                    add_log(f"Scan error: {e.stderr}")

            threading.Thread(target=scan_task).start()

    # Function to display scan results and save to database
    def display_results(output, ip):
        for widget in result_frame.winfo_children():
            widget.destroy()

        # Headers for the columns
        headers = ["PORT", "STATE", "SERVICE", "VERSION", "STATUS", "UPDATE", "VULNERABILITY"]
        scan_data = {"IP": ip, "Results": []}

# Create the header row
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(result_frame, text=header, font=("Arial Rounded MT Bold", 13, "bold"))
            header_label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

# Parse and display each line
        row = 1
        lines = output.splitlines()
        for line in lines:
            if "/tcp" in line:
                parts = line.split()
                if len(parts) >= 3:
                    port = parts[0]
                    state = parts[1]
                    service = parts[2]
                    version = " ".join(parts[3:]) if len(parts) > 3 else ""
                    latest_version, update_url = simulate_latest_version(service)
                    flag = "⚠️ Outdated" if version and latest_version and version != latest_version else ""

                    ctk.CTkLabel(result_frame, text=port).grid(row=row, column=0, padx=10, pady=2, sticky="w")
                    ctk.CTkLabel(result_frame, text=state).grid(row=row, column=1, padx=10, pady=2, sticky="w")
                    ctk.CTkLabel(result_frame, text=service).grid(row=row, column=2, padx=10, pady=2, sticky="w")
                    ctk.CTkLabel(result_frame, text=version).grid(row=row, column=3, padx=10, pady=2, sticky="w")
                    

                    if flag:  # If outdated
                        flag_label = ctk.CTkButton(
                            result_frame,
                            text=flag,
                            fg_color="lightcoral",  # Background color
                            text_color="white",     # Text color
                            corner_radius=12,       # Rounded corners
                            hover=False             # Disable hover effect
                        )
                        flag_label.grid(row=row, column=4, padx=10, pady=2, sticky="w")
                    else:
                        ctk.CTkLabel(result_frame, text="").grid(row=row, column=4, padx=10, pady=2, sticky="w")

                    


                    if flag:
                        update_query = f"how to update {version}"
                        update_results = search(update_query, num_results=1)
                        update_url = next(update_results, "https://google.com")
                        
                        
                        i=1
                        
                        vulnerability_query = f"nvd {version}"
                        vulnerability_results = search(vulnerability_query, num_results=1)
                        vulnerability_url = next(vulnerability_results, "https://google.com")
                        cve_id = vulnerability_url.rsplit("/", 1)[-1]
                        if cve_id != r"^CVE-\d{4}-\d{4,}$" :
                            for i in range (1,6):
                                vulnerability_results =search(vulnerability_query, num_results=i)
                                vulnerability_url = next(vulnerability_results, "https://google.com")
                        else:
                            cve_id == "coul't find the cve_id"
                                
                        
                       
                        
                        

                        if flag:  # Check if the flag is not empty
                            update_label = ctk.CTkButton(
                                result_frame,
                                text="Update",
                                fg_color="limegreen",
                                text_color="white",
                                corner_radius=12,  # Set corner radius to 12px
                                cursor="hand2",
                                command=lambda: open_update_link(update_url)
                            )
                            update_label.grid(row=row, column=5, padx=1, pady=2, sticky="w")

                            vulnerability_label = ctk.CTkButton(
                                result_frame,
                                text=cve_id,
                                fg_color="limegreen",
                                text_color="white",
                                corner_radius=12,  # Set corner radius to 12px
                                cursor="hand2",
                                command=lambda: open_update_link(vulnerability_url)
                            )
                            vulnerability_label.grid(row=row, column=6, padx=1, pady=2, sticky="w")
                        else:
                            ctk.CTkLabel(result_frame, text="").grid(row=row, column=5, padx=10, pady=2, sticky="w")
                            ctk.CTkLabel(result_frame, text="").grid(row=row, column=6, padx=10, pady=2, sticky="w")


                    scan_data["Results"].append({
                        "Port": port,
                        "State": state,
                        "Service": service,
                        "Version": version,
                        "Status": flag,
                        "Update URL": update_url if flag else "",
                        "Vulnerability URL": vulnerability_url if flag else "",
                    })
                    row += 1






                    
                    def save_results_as_pdf(scan_data, filename="scan_results.pdf"):
                        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                        file_path = os.path.join(desktop_path, filename)
                        
                        doc = SimpleDocTemplate(file_path, pagesize=letter)
                        elements = []

                        styles = getSampleStyleSheet()
                        styleN = styles['Normal']
                        styleLink = styles['Normal']
                        styleLink.textColor = colors.blue

    # Title
                        title = ["Scan Results"]
                        elements.append(Table([title], colWidths=[500]))


    # Adding a header with IP information
                        ip_info = [[f"IP: {scan_data['IP']}"]]
                        elements.append(Table(ip_info, colWidths=[500]))

    # Table header and data
                        header = ["PORT", "STATE", "SERVICE", "VERSION", "STATUS", "CHECK"]
                        data = [header]

                        for result in scan_data["Results"]:
                            update_url = result["Update URL"]
                            if update_url:
                                update_url = Paragraph(
                                f'<a href="{update_url}" color="blue">Update</a>',
                                styleLink
                                )
                            else:
                                update_url = ""
                                
                            row = [
                                result["Port"],
                                result["State"],
                                result["Service"],
                                result["Version"],
                                result["Status"],
                                update_url  # Ensure this goes under the correct column
                            ]
                            data.append(row)
                            
                        font_path = dust_folder/"arialroundedmtbold.ttf"
                        pdfmetrics.registerFont(TTFont("ArialRoundedMTBold", font_path))
                        
                        pdfmetrics.registerFont(TTFont("ArialRoundedMTBold", str(font_path)))



                        table = Table(data, colWidths=[80, 50, 50, 170, 100, 50])
                        table.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'ArialRoundedMTBold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ]))
                        elements.append(table)

                        doc.build(elements)
                        messagebox.showinfo("Scan Condition", "Scan Completed Successfully.")
                        add_log("Scan completed successfully.")
                        messagebox.showinfo("PDF Saved", f"Scan results saved as PDF on Desktop.")
                        add_log("Scan results saved as PDF on Desktop.")
                        
                        # Call the send email function
                        
                        recipient_email = "spotifygoy@gmail.com"
                        send_pdf_via_postmark(file_path, recipient_email)

                        
                        
                        
                        # Function to send the PDF via email
                        
                    def send_pdf_via_postmark(pdf_path, recipient_email):
    # Replace this with your Postmark Server Token
                        from postmarker.core import PostmarkClient
                        import os
                        server_token = "56bf7540-cc25-4a7a-b95c-9badd3418a87"
                        sender_email = "colabddsdf@gmail.com"  # Ensure this email is verified in Postmark

    # Read PDF data
                        with open(pdf_path, "rb") as pdf_file:
                            pdf_data = pdf_file.read()
                            
                            
                        encoded_pdf_data = base64.b64encode(pdf_data).decode("utf-8")

    # Create a Postmark client
                        postmark = PostmarkClient(server_token=server_token)

    # Send the email with attachment
                        try:
                            postmark.emails.send(
                                From=sender_email,
                                To=recipient_email,
                                Subject="Scan Results PDF",
                                TextBody="Please find attached the scan results PDF.",
                                Attachments=[
                                    {
                                        "Name": os.path.basename(pdf_path),
                                        "Content": encoded_pdf_data,
                                        "ContentType": "application/pdf",
                                    }
                                ],
                            )
                            print("Email sent successfully!")
                            messagebox.showinfo("Email Sent", "Email sent successfully.")
                        except Exception as e:
                            messagebox.showerror("Email Error", f"Failed to send email: {e}")
                            print(f"Failed to send email: {e}")
                        
                    
                    
                    
        # Save scan data to Firebase
        
        
        db.reference("scan_results/last_scan").set(scan_data)
        
        # Save scan data as PDF
        save_results_as_pdf(scan_data)


    # Function to open update link in browser
    def open_update_link(url):
        webbrowser.open(url)


    

    # adding the scan image
    scan_icon = Image.open(sources_folder/"257-2572350_search-icon-search-icon-png-orange-fotor-bg-remover-20241224111032-fotor-bg-remover-20241224111612.png")
    scan_icon = scan_icon.resize((29, 25))  # Resize the icon to fit the button
    scan_icon = ImageTk.PhotoImage(scan_icon)
    # Scan button
    scan_button = ctk.CTkButton(master=main_frame, text="Scan", corner_radius=12,
    fg_color="transparent",
    hover_color="#C850C0",
    border_color="#FFCC70",
    border_width=2,
    image=scan_icon, 
    compound="right",
    font=("Arial Rounded MT Bold", 13, "bold"),
    command=lambda: run_scan(url_entry.get()))
    scan_button.grid(row=3, column=1, padx=(10, 20), pady=(10, 20), sticky="w")
    
    
    # Start listening for changes in the "/new_scan" path
    def listener(event):
        if event.data:
            ip_or_url = event.data
            last_scan_ref = db.reference("scan_results/last_scan/IP").get()

            domain = process_url(ip_or_url)  # Process the URL
            ip = resolve_to_ip(domain) if not domain.replace('.', '').isdigit() else domain
            if not ip:
                add_log(f"Failed to resolve URL: {ip_or_url}")
                return

            if 1==1:
                add_log("welcome to me scaner")
            if 1==1:
                answer = messagebox.askyesno("New Scan Request", f"Do you want to run the scan for {ip_or_url} (IP: {ip})?")
                if answer:
                    add_log(f"New scan request for IP: {ip}")
                    run_scan(ip)
                else:
                    add_log("User declined the new scan request.")
        else:
            add_log("No valid URL found for scanning.")

    db.reference("new_scan").listen(listener)

app.mainloop()