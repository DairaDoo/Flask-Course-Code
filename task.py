import os
import requests
from dotenv import load_dotenv
import jinja2

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)


def send_simple_message(to, subject, body, html):
    domain = os.getenv("MAILGUN_DOMAIN")
    api_key = os.getenv("MAILGUN_API_KEY")

    # Debug prints to trace email sending
    print(f"MAILGUN_DOMAIN: {domain}")
    print(f"MAILGUN_API_KEY: {api_key}")
    print(f"Sending email to: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

    response = None
    try:
        response = requests.post(
            f"https://api.mailgun.net/v3/{domain}/messages",
            auth=("api", api_key),
            data={
                "from": f"Dairan De Jesús Mora <mailgun@{domain}>",
                "to": [to],
                "subject": subject,
                "text": body,
                "html": html
            }
        )
        response.raise_for_status()  # Raise an error for bad status codes
        print(f"Email sent successfully! Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send email: {e}")
    return response


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "succesffully signed up.",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
        render_template("email/action.html", username=username)
        
    )