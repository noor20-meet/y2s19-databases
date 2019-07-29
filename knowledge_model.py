from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = 'knowledge'
	Link = Column(String, primary_key=True)
	Name = Column(String)
	Topic = Column(String)
	Rating = Column(Integer)


	def __repr__(self):
		return("Link : {}\n"
			"Name: {}\n"
			"Topic: {}\n"
			"Rating: {}").format(self.Link, self.Name, self.Topic, self.Rating)

