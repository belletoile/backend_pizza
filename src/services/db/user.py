import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from sqlalchemy.orm import Session

from src.config import LOGIN, PASSWORD
from src.models.models import User
from src.schemas.user import CreateUserSchema


def create_user(session: Session, user: CreateUserSchema):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, phone: str):
    return session.query(User).filter(User.phone == phone).one()


def send_password_reset_link(email: str):
    def rand():
        rnd = (random.randint(100000, 999999))
        return rnd

    msg = MIMEMultipart()
    msg['Subject'] = "Password Recovery"
    msg['From'] = LOGIN
    msg.attach(MIMEText(f"Hello, enter this code in the password recovery field {rand()}", "plain"))

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(LOGIN, PASSWORD)
    s.sendmail(email, email, msg.as_string())
    return rand()
