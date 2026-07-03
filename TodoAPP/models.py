# from database import Base
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

# class Todos(Base):
#     __tablename__ = 'todos'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     priority = Column(Integer)
#     complete = Column(Boolean, default=False)
#     #owner_id = Column(Integer, ForeignKey("users.id"))

#======================================================================

# Base import kar rahe hain database.py se
# Base wahi declarative_base() hai — isse inherit karna matlab "ye ek DB table hai"
from database import Base

# Column     → table ka ek column define karne ke liye
# Integer    → number type (1, 2, 3...)
# String     → text type
# Boolean    → True/False type
# ForeignKey → doosri table se relation banana ke liye
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

# Base se inherit kar rahe hain → SQLAlchemy samajh jaata hai ye ek DB table hai
# Jab models.Base.metadata.create_all(bind=engine) chalega
# toh ye class ek actual table ban jaayegi DB mein
class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    #owner_id = Column(Integer, ForeignKey("users.id"))