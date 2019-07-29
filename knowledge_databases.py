from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(link, name, topic, rating):
	article = Knowledge(Link = link, Name = name, Topic = topic, Rating = rating)
	session.add(article)
	session.commit()



# add_article("https://en.wikipedia.org/wiki/Dolphin", "Dolphins", "Learn more  about these gentle aquatic mammals and their living environment. How do they live? How do they communicate?",10)
# add_article("https://en.wikipedia.org/wiki/Ant", "Ants", "Ants are extremely hardworking insects that can carry many times its own body weight. How strong!", 8)


def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

# print(query_all_articles())

def query_article_by_name(name_first):
	name_first = session.query(Knowledge).filter_by(Name = name_first).first()
	return name_first



def delete_article_by_topic(topic):
	topics_deleted = session.query(Knowledge).filter_by(Topic = topic).delete()
	return topics_deleted

def delete_all_articles():
	articles_deleted = session.query(Knowledge).delete()
	return articles_deleted


def edit_article_rating(name, new_rating):
	name = session.query(Knowledge).filter_by(Name=name).first()

	name.Rating = new_rating
	session.commit()

print(query_all_articles())
