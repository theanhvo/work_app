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
url1 = "https://www.timviecnhanh.com/tuyen-quan-ly-nha-hang-ho-chi-minh-3793012.html"
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content, "lxml")
side_bar = soup1.find("div", {"class" : "block-sidebar"})
img = side_bar.img
link_img = img.get('src')
print(link_img)
off_set = soup1.find("div" , {"class" : "col-xs-6 p-r-10 offset10"})
restaurant_name = off_set.h3.text
print(restaurant_name)
address = off_set.span.text
print(address)
push_right = soup1.find_all("div", {"class" : "col-xs-4 offset20 push-right-20"})
for ab in push_right:
    muc_luong = ab.text
    print(muc_luong)
push_right1 = soup1.find_all("div", {"class" : "col-xs-4 offset20"})
for ab in push_right1:
    tccv = ab.text
    print(tccv)
#############################
table = soup1.find("table")
table_content = table.text
print(table_content)

# TODO(theanh) extract post logo_restaurant, restaurant_name, .... from table content
post = models.Post.objects.create(
    logo_restaurant,
    restaurant_namme,
    address,
    city,
    wage,
    employer_mail,
    position,
    job_requirements,
    why_love_this_job
)

# TODO(theanh) job name ??
job = models.Job.objects.get_or_create(name)
job.post.add(post)
job.save()
