#!/usr/bin/env python
#-*- coding: utf-8 -*-

urls = (
    '/' 						,	'Index',
    '/studentlist/(.+)/(.+)'	,	'GetStudentList',
    '/class/(.+)'				,	'GetAClassStudent',
    '/deletestudent/(.+)'		,	'DeleteStudent',
    '/studentinfo/(.+)'			,	'GetStudentInfo',
    '/highlevelinfo/(.+)'       ,   'GetHighLevelInfo',
    '/editstudentinfo/(.+)'		,	'EditStudentInfo',
    '/savestudentinfo'			,	'SaveStudentInfo',
    '/addstudent'				,	'AddStudent',
    '/savestudent'				,	'SaveStudent',
    '/search'					,	'Search',
    '/addmeeting'               ,   'AddMeeting',
    '/savemeeting'              ,   'SaveMeeting',
    '/meetinglist'              ,   'GetMeetingList',
    '/addnote'                  ,   'AddNote',
    '/savenote'                 ,   'SaveNote',
    '/notelist'                 ,   'GetNoteList',
    '/sendmailto/(.+)'          ,   'NewEmail'  ,
    '/sendmail'                 ,   'SendEmail',
    '/login'                    ,   'Login',
    '/logout'                   ,   'Logout'

    

   
)	