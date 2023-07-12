from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.models.models import User
from src.schemas.user import CreateUserSchema
import random, config, smtplib


def create_user(session: Session, user: CreateUserSchema):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, phone: str):
    return session.query(User).filter(User.phone == phone).one()

def send_password_reset_link(email: str, session: Session):
    def rand():
        rnd = (random.randint(100000, 999999))
        return rnd

    msg = MIMEMultipart()
    msg['Subject'] = "Password Recovery"
    msg['From'] = config.login
    msg.attach(MIMEText(f"Hello, enter this code in the password recovery field {rand()}", "plain"))

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(config.login, config.password)
    s.sendmail(email, email, msg.as_string())
    return rand()