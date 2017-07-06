#!/usr/bin/python3
# -*- coding: utf-8 -*-
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_work.settings")  # noqa
django.setup()
from app import models
import requests
from bs4 import BeautifulSoup
url = "https://www.timviecnhanh.com/viec-lam-du-lich-nha-hang-khach-san-c23.html?page=0"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
divtag = soup.find_all("div", {"class" : "intro col-xs-4 offset20 push-left-10"})
for a in divtag:
    links = a.find('a')
    link = links.get('href')
    print(link)
    print('++++++++++++')
#extract detail page
url1 = "https://www.timviecnhanh.com/tuyen-nhan-vien-booker-ho-chi-minh-3619310.html"
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content, "lxml")
box_content = soup1.find("div", {"class" : "detail-content box-content"})
name_work = box_content.h1.text
print(name_work)
side_bar = soup1.find("div", {"class" : "block-sidebar"})
img = side_bar.img
link_img = img.get('src')
print(link_img)
off_set = soup1.find("div" , {"class" : "col-xs-6 p-r-10 offset10"})
asd = off_set.h3.text
restaurant_name = asd.strip()
print(restaurant_name)
bass = off_set.span.text
address_11 = bass.strip().split(':')
address = address_11[1]

print(address)
push_right = soup1.find_all("div", {"class" : "col-xs-4 offset20 push-right-20"})
for ab in push_right:
    li_tong = ab.ul.find_all('li')
muc_luong = li_tong[0].text
tmp = muc_luong.split(':')
muc_luong1 = tmp[1].strip().split()
muc_luong_result = ' '.join(muc_luong1)
print(muc_luong_result)
kinh_nghiem = li_tong[1].text
gty = kinh_nghiem.split(':')
kinh_nghiem1 = gty[1].strip().split()
kinh_nghiem_result = ' '.join(kinh_nghiem1)
print(kinh_nghiem_result)
ppp = li_tong[3].text
kil = ppp.strip().split('làm')
thanh_pho = kil[1]
print(thanh_pho)
col_xn = soup1.find_all("div" , {"class" : "col-xs-4 offset20"})
for bc in col_xn:
    li = bc.ul.find_all('li')
wer = li[0].text
wer1 = wer.split(':')
so_luong = wer1[1].strip()
print(so_luong)
gnm = li[1].text
gnm1 = gnm.split(':')
gioi_tinh = gnm1[1].strip()
print(gioi_tinh)
iuy = li[2].text
iuy1 = iuy.split(':')
tinh_chat = iuy1[1].strip()
print(tinh_chat)
dfg = li[3].text
dfg1 = dfg.split(':')
hinh_thuc = dfg1[1].strip()
print(hinh_thuc)


#extract table
table = soup1.find('table')
bang = table.find_all('tr')
momo = bang[0].text
momo1 = momo.strip().split('tả')
mo_ta = momo1[1].strip()
mo_ta_result = mo_ta.replace("*" , "").strip()
print(mo_ta_result)
momo2 = bang[1].text
momo3 = momo2.strip().split('cầu')
yeu_cau = momo3[1].strip()
yeu_cau_result = yeu_cau.replace("*" , "").strip()
print(yeu_cau_result)
momo7 = bang[2].text
momo4 = momo7.strip().split('lợi')
love_job = momo4[1].strip()
love_job_result = love_job.replace("-" , "").strip()
print(love_job_result)
momo8 = bang[3].text
momo9 = momo8.strip().split('nộp')
deadline = momo9[1].strip()
print(deadline)
contact_employer = soup1.find("div", {"class" : "block-content"})
abc  = contact_employer.find('tr')
contact_employer1 = abc.text
contact_employer3 = contact_employer1.strip().split('hệ')
result_contact = contact_employer3[1].strip()
print(result_contact)

# TODO(theanh) extract post logo_restaurant, restaurant_name, .... from table content
post = models.Post.objects.create(
    logo_restaurant = link_img,
    restaurant_name = restaurant_name,
    address = address,
    city = thanh_pho,
    wage = muc_luong_result
    employer_mail = employer_mail,
    contact_employer = result_contact,
    experience = kinh_nghiem_result,
    number_recruits = so_luong,
    gender = gioi_tinh,
    job_feature = tinh_chat,
    type_job = hinh_thuc,
    job_description = mo_ta_result,
    job_requirements = yeu_cau_result,
    why_love_this_job = love_job_result,
    deadline = deadline
)

# TODO(theanh) job name ??
job = models.Job.objects.get_or_create(name = name_work)
job.post.add(post)
job.save()
