from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BookDB(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    pages = Column(Integer, nullable=False)


class LibraryDB(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    books = relationship("BookDB", backref="library")



engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


new_library = LibraryDB(name="Моя бібліотека")
new_book1 = BookDB(title="Великий роман", pages=300)
new_book2 = BookDB(title="Маленька книга", pages=150)

new_library.books.append(new_book1)
new_library.books.append(new_book2)

session.add(new_library)
session.commit()
session.close()