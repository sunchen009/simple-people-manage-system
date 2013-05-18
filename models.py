#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sae
import web

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Date
from sqlalchemy.exc import IntegrityError
from settings import mysql_engine

Base = declarative_base()


	
class Student(Base):
	__tablename__ = 'Students'	

	id          	= Column(Integer ,primary_key = True)
	studentid		= Column(String(20))
	name       		= Column(String(50))
	sex				= Column(String(5))
	classid			= Column(String(10))
	dormitory		= Column(String(10))
	birthday		= Column(Date)
	phone			= Column(String(20))
	email			= Column(String(50))
	father			= Column(String(50))
	mother			= Column(String(50))
	fatherjob		= Column(String(50))
	motherjob		= Column(String(50))
	hometown		= Column(String(100))	
	level			= Column(Integer)    #1-6不同人员等级
	prize			= Column(Text)

class HighLevelObject(Base):
	__tablename__ = 'HighLevelObjects'	
		
	id          	= Column(Integer ,primary_key = True)
	studentid		= Column(String(20))
	name       		= Column(String(50))
	sex				= Column(String(5))
	classid			= Column(String(10))
	level 			= Column(Integer)
	belevel5year	= Column(Integer)
	belevel5season	= Column(Integer)
	belevel6year	= Column(Integer)
	belevel6season	= Column(Integer)
	belevel5time	= Column(Date)
	belevel6time	= Column(Date)
	introducer1		= Column(String(50))
	introducer2		= Column(String(50))
	doc1			= Column(Integer)
	doc2			= Column(Integer)
	doc3			= Column(Integer)
	doc4			= Column(Integer)
	doc5			= Column(Integer)
	doc6			= Column(Integer)
	doc7			= Column(Integer)
	doc8			= Column(Integer)
	doc9			= Column(Integer)
	doc10			= Column(Integer)
	doc11			= Column(Integer)
	doc12			= Column(Integer)
	doc13			= Column(Integer)
	doc14			= Column(Integer)
	doc15			= Column(Integer)
	doc16			= Column(Integer)
	doc17			= Column(Integer)
	doc18			= Column(Integer)
	doc19			= Column(Integer)
	doc20			= Column(Integer)
	doc21			= Column(Integer)

class Note(Base):
	__tablename__ = 'Notes'	
		
	id          	= Column(Integer ,primary_key = True)
	title			= Column(String(20))
	poster			= Column(String(20))
	posttime		= Column(DateTime)
	content			= Column(Text)

class Meeting(Base):
	__tablename__ = 'Meetings'	
		
	id          	= Column(Integer ,primary_key = True)
	theme			= Column(String(20))
	poster			= Column(String(20))
	meetingdate		= Column(Date)
	where			= Column(String(20))
	whathappened	= Column(Text)

class Admin(Base):
	__tablename__ ="Admins"
	id          	= Column(Integer ,primary_key = True)
	username		= Column(String(20))
	userpass		= Column(String(50))
	
metadata = Base.metadata
def initDb():
    metadata.create_all(mysql_engine)   

if __name__ == '__main__':
    initDb()
