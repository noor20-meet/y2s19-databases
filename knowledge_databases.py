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


add_article("url","Name","Topic",7)
dolphins = add_article(link = "https://en.wikipedia.org/wiki/Dolphin", name = "Dolphins", 
						topic = "Learn more",
						# rating = 8)
# ants = add_article(link = "https://en.wikipedia.org/wiki/Ant", name = "Ants", 
					# topic = "Ants ", rating = 7)

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

print(query_all_articles())

def query_article_by_topic(topic):
	topics = session.query(Knowledge).filter_by(Topic = topic).first()
	return topics

def delete_article_by_topic():
	topics_deleted = session.query(Knowledge).filter_by(Topic = topic).delete()
	return topics_deleted

def delete_all_articles():
	articles_deleted = session.query(Knowledge).delete()
	return articles_deleted

def edit_article_rating(name, new_rating):
	name.Rating(new_rating)

