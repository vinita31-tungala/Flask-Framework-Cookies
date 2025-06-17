📂 Project Structure
markdown
Copy
Edit
cookie-flask-app/
│
├── app.py
└── templates/
    ├── setcookie.html
    └── readcookie.html
📄 app.py
This is the main Flask application file. It:

Displays a form (/)

Accepts a POST request to set a cookie (/setcookie)

Reads and displays the cookie (/getcookie)
🚀 How to Run
Clone the repo or copy the files

Open terminal and navigate to project folder.

(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
Install Flask:

bash
Copy
Edit
pip install flask
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to:

arduino
Copy
Edit
http://localhost:5000/
🧪 Sample Output
Visit the homepage and enter your name:

csharp
Copy
Edit
Enter userID: Vinita
[Login]
After submitting, you'll see:

pgsql
Copy
Edit
Click here to read cookie
Clicking the link shows:

nginx
Copy
Edit
Welcome Vinita
🛠 Built With
Python 3.x

Flask

