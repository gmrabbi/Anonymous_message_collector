# WhisperBox — Anonymous Flask Message Website

A small Flask website where anyone can submit an anonymous message and only the administrator can view stored messages.

## Features

- Anonymous public message form
- No sender name, email, IP address, or user-agent is stored by the application
- Admin-only dashboard
- Password-protected admin login
- Excel `.xlsx` export of all messages
- Spreadsheet formula-injection protection for exported anonymous text
- Delete individual messages
- SQLite database
- CSRF protection
- Hidden honeypot field for simple bot protection
- Responsive custom UI
- 5,000-character message limit

## 1. Create a virtual environment

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install packages

```bash
pip install -r requirements.txt
```

## 3. Create `.env`

Copy `.env.example` to `.env`.

Windows:

```powershell
Copy-Item .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Generate the admin password hash:

```bash
python generate_password_hash.py
```

Paste the generated value into:

```env
ADMIN_PASSWORD_HASH=your-generated-hash
```

Also replace `SECRET_KEY` with a long random secret.

For example, you can generate one with Python:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## 4. Run

```bash
python app.py
```

Open:

- Public form: `http://127.0.0.1:5000`
- Admin login: `http://127.0.0.1:5000/admin/login`

## Make it accessible on your LAN

Change this in `.env`:

```env
FLASK_HOST=0.0.0.0
```

Then run again and access the computer's LAN IP, for example:

```text
http://192.168.0.50:5000
```

## Internet deployment

For a public deployment, do not use Flask's development server directly. Put the app behind a production WSGI server/reverse proxy and HTTPS.

Important production settings:

```env
FLASK_DEBUG=false
SESSION_COOKIE_SECURE=true
```

Use a strong `SECRET_KEY`, protect the server itself, and use HTTPS.

## Privacy note

The application database stores:

- internal message ID
- message body
- received timestamp

It does **not** intentionally store sender name, email, IP address, or browser/user-agent.

However, a reverse proxy, hosting platform, CDN, firewall, or web server may independently create access logs containing IP addresses. If strict anonymity is required, configure those systems accordingly.
