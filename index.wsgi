#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import datetime

import sae
import web
from sae.mail import send_mail

import md5
import re
from urls import urls       
from settings import global_render 
from settings import load_sqla ,store
from web import form
from models	import Student, initDb,HighLevelObject,Meeting,Note,Admin
from tools import Pager



def check_login():
	try:
		if session.login != True:
			raise web.seeother('/login')
	except AttributeError:
			raise web.seeother('/login')
###########
#控制器
###########
class Index(object):	
	def GET(self):
		check_login()			
		return global_render.index()

class GetAClassStudent(object):
	def GET(self,classid):
		check_login()
		studentlist = web.ctx.orm.query(Student).filter_by(classid=classid).order_by(Student.studentid.desc()).all()
		return global_render.classstudent(student_list=studentlist)

class GetStudentList(object):
	def GET(self,level,pageid):
		check_login()
		pageid = int(pageid)
		level  = int(level)
		if level == 0:
			studentlist = web.ctx.orm.query(Student).order_by(Student.classid.desc()).all()
		elif level in range(1,7):
			studentlist = web.ctx.orm.query(Student).filter_by(level=level).order_by(Student.classid.desc()).all()
		studentlist, pagecount,count = Pager(studentlist,pageid)
		return global_render.studentlist(student_list=studentlist,page_count=pagecount,page=pageid,level=level,count=count)

class DeleteStudent(object):
	def GET(self,studentid):
		check_login()
		student = web.ctx.orm.query(Student).filter_by(studentid=studentid).first()
		web.ctx.orm.delete(student)
		referer = web.ctx.env.get('HTTP_REFERER', 'a url you want')
		raise web.seeother(referer)

class GetStudentInfo(object):
	def GET(self,studentid):
		check_login()
		student = web.ctx.orm.query(Student).filter_by(studentid=studentid).first()
		return global_render.studentinfo(student=student)

class GetHighLevelInfo(object):
	def GET(self,studentid):
		check_login()
		student = web.ctx.orm.query(HighLevelObject).filter_by(studentid=studentid).first()
		return global_render.highlevelinfo(student=student)

class EditStudentInfo(object):
	def GET(self,studentid):
		check_login()
		student = web.ctx.orm.query(Student).filter_by(studentid=studentid).first()
		return global_render.editstudentinfo(student=student)

class AddStudent(object):
	def GET(self):
		check_login()
		student = Student()
		return global_render.addstudent(student=student)

class AddMeeting(object):
	def GET(self):
		check_login()
		meeting = Meeting()
		return global_render.addmeeting(meeting=meeting)
class SaveMeeting(object):
	def POST(self):
		check_login()
		i = web.input()
		meeting = Meeting()
		meeting.theme = i.theme
		meeting.where = i.where
		meeting.meetingdate = i.meetingdate
		meeting.whathappened = i.whathappened
		web.ctx.orm.add(meeting)
		raise web.seeother('/meetinglist')

class GetMeetingList(object):
	def GET(self):
		check_login()
		meetinglist = web.ctx.orm.query(Meeting).order_by(Meeting.meetingdate.desc()).all()
		count = len(meetinglist)
		return global_render.meetinglist(meetinglist=meetinglist,count=count)

class AddNote(object):
	def GET(self):
		check_login()
		note = Note()
		return global_render.addnote(note=note)

class SaveNote(object):
	def POST(self):
		check_login()
		i = web.input()
		note = Note()
		note.title = i.title
		note.content = i.content
		note.posttime =  datetime.datetime.now()
		web.ctx.orm.add(note)
		raise web.seeother('/notelist')

class GetNoteList(object):
	def GET(self):
		check_login()
		notelist = web.ctx.orm.query(Note).order_by(Note.posttime.desc()).all()
		count = len(notelist)
		return global_render.notelist(notelist=notelist,count=count)

class SaveStudent(object):
	def POST(self):
		check_login()
		i = web.input()
		student = Student()
		student.studentid = i.studentid
		student.name = i.name
		student.sex  = i.sex
		student.dormitory	= i.dormitory
		student.birthday	= i.birthday
		student.classid		= i.classid
		student.father		= i.father
		student.mother		= i.mother
		student.fatherjob	= i.fatherjob
		student.mother		= i.motherjob
		student.hometown	= i.hometown
		student.phone		= i.phone
		student.email		= i.email
		student.prize		= i.prize
		student.level		= i.level
		web.ctx.orm.add(student)
		raise web.seeother("/studentinfo/"+str(i.studentid))

class SaveStudentInfo(object):
	def POST(self):
		check_login()
		i = web.input()
		studentid = i.studentid
		student = web.ctx.orm.query(Student).filter_by(studentid=studentid).first()
		student.name = i.name
		student.sex  = i.sex
		student.dormitory	= i.dormitory
		student.birthday	= i.birthday
		student.classid		= i.classid
		student.father		= i.father
		student.mother		= i.mother
		student.fatherjob	= i.fatherjob
		student.mother		= i.motherjob
		student.hometown	= i.hometown
		student.phone		= i.phone
		student.email		= i.email
		student.prize		= i.prize
		student.level		= i.level
		web.ctx.orm.commit()
		raise web.seeother("/studentinfo/"+str(studentid))

class Search(object):
	def POST(self):
		check_login()
		i = web.input()
		querystr = i.querystr
		querystr = querystr.strip()
		r1 = re.compile(r'^\d{9}$')
		r2 = re.compile(r'^\d{6}[A-Z]$')

		if r1.match(querystr):
			raise web.seeother("/studentinfo/"+querystr)
		elif r2.match(querystr):
			raise web.seeother("/class/"+querystr)
		else :
			studentlist = web.ctx.orm.query(Student).filter(Student.name.like(querystr)).all()
			if len(studentlist) ==1 :
				raise web.seeother("/studentinfo/"+str(studentlist[0].studentid))
			else:
				return global_render.classstudent(student_list=studentlist)
 
class NewEmail(object):
	 def GET(self,studentid):
	 	check_login()
	 	student = web.ctx.orm.query(Student).filter_by(studentid=studentid).first()
	 	email =student.email
	 	return global_render.editmail(address=email)
class SendEmail(object):
	 def POST(self):
	 	check_login()
	 	i = web.input()
	 	to = i.address
	 	subject = i.theme
	 	body = i.content
	 	send_mail(to, subject, body,
        ('smtp.xxxx.com', port, "xxxx@xxx.com", "thepassword", False))
	 	return "<script>alert(\"发送成功\")</script>"

class Login(object):
	 def GET(self):

	 	return global_render.login()

	 def POST(self):
	 	i=web.input()
	 	userpass = i.userpass.strip()
	 	username = i.username.strip()
	 	admin = web.ctx.orm.query(Admin).filter_by(username=username).first()
	 	if admin==None:
	 		raise web.seeother("/login")
	 	if md5.new(userpass).hexdigest() == admin.userpass:
	 		session.login = True
			session.username = username
			raise web.seeother("/")
		else:
			raise web.seeother("/login")

class Logout(object):
	 def GET(self):
	 	session.kill()
	 	raise web.seeother("/login")





def notfound():
    return  web.notfound(global_render.page404())

def internalerror():
    return web.internalerror(global_render.page500())


app = web.application(urls, globals())
app.add_processor(load_sqla)
#app.notfound = notfound
#app.internalerror = internalerror


#use session in debug modal
if web.config.get('_session') is None:
    session = web.session.Session(app, store)
    web.config._session = session
else:
    session = web.config._session

application = sae.create_wsgi_app(app.wsgifunc())

initDb()
web.config.debug = True





