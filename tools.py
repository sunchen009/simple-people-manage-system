#!/usr/bin/env python
#-*- coding: utf-8 -*-

#分页函数
def Pager(lists,page=1):
	count = len(lists)
	page_count = count / 40
	if count == 0:
		return lists,0,0
	if count % 40 != 0:
			page_count = page_count + 1		
	if page < page_count:
		return lists[40*(page-1):40*page],page_count,count
	elif page == page_count:
		if count >40:
			return lists[40*(page-1):],page_count,count
		else:
			return lists[:],page_count,count






		