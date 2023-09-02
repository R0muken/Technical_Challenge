from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

Base = declarative_base()


class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    activity_name = Column(String)
    type = Column(String)
    participants = Column(Integer)
    price = Column(Float)
    link = Column(String)
    key = Column(String)
    accessibility = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"activity_name = {self.activity_name}\n" \
               f"type = {self.type}\n" \
               f"participants = {self.participants}\n" \
               f"price = {self.price}\n" \
               f"link = {self.link}\n" \
               f"key = {self.key}\n" \
               f"accessibility = {self.accessibility}\n"


class ActivityDatabase:
    def __init__(
            self,
            db_url
    ):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_activity(
            self,
            activity_name,
            type,
            participants,
            price,
            link,
            key,
            accessibility
    ):
        session = self.Session()

        activity = Activity(
            activity_name=activity_name,
            type=type,
            participants=participants,
            price=price,
            link=link,
            key=key,
            accessibility=accessibility
        )

        try:
            session.add(activity)
            session.commit()
            session.close()
        except SQLAlchemyError as e:
            print(f"Database operation error: {e}")

    def get_latest_activities(
            self,
            limit=10
    ):
        try:
            session = self.Session()
            activities = session.query(Activity).order_by(Activity.timestamp.desc()).limit(limit).all()
            session.close()
            return activities
        except SQLAlchemyError as e:
            print(f"Database operation error: {e}")
