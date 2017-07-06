#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_work.settings")  # noqa
django.setup()

from bs4 import BeautifulSoup
import requests

from app import models

LOGGER = logging.getLogger(__name__)


def crawl_detail(link):
    """
    Request to fetch page from url & store Post & Job
    """
    LOGGER.info('Crawl detail page %r', link)
    resp = requests.get(link)
    page = BeautifulSoup(resp.content, "lxml")

    box_content = page.find("div", {"class" : "detail-content box-content"})
    name_work = box_content.h1.text
    print(name_work)

    side_bar = page.find("div", {"class" : "block-sidebar"})
    img = side_bar.img
    link_img = img.get('src')
    print(link_img)

    off_set = page.find("div" , {"class" : "col-xs-6 p-r-10 offset10"})
    asd = off_set.h3.text
    restaurant_name = asd.strip()
    print(restaurant_name)

    bass = off_set.span.text
    address_11 = bass.strip().split(':')
    address = address_11[1]
    print(address)

    push_right = page.find_all("div", {"class" : "col-xs-4 offset20 push-right-20"})
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

    col_xn = page.find_all("div" , {"class" : "col-xs-4 offset20"})
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
    tables = page.find_all('table')
    job_desc = None
    job_requirements = None
    benefit = None
    deadline = None
    employer_contact = None

    rows = []
    if len(tables) >= 1:
        rows = tables[0].find_all('tr')
        for row in rows:
            title = row.b.text
            if title == 'Mô tả':
                job_desc = row.p.text.strip()

            elif title == 'Yêu cầu':
                job_requirements = row.p.text.strip()

            elif title == 'Quyền lợi':
                benefit = row.p.text.strip()

            elif title == 'Hạn nộp':
                deadline = row.find('b', {'class': 'text-danger'}).text.strip()

    if len(tables) >= 2:
        rows = tables[1].find_all('tr')
        for row in rows:
            title = row.b.text
            if title == 'Mô tả':
                job_desc = row.p.text.strip()

            elif title == 'Người liên hệ':
                employer_contact = row.p.text.strip()

            elif title == 'Địa chỉ':
                address = row.p.text.strip()

    post_params = dict(
        logo_restaurant=link_img,
        restaurant_namme=restaurant_name,
        address=address,
        city=thanh_pho,
        wage=muc_luong_result,
        contact_employer=employer_contact,
        experience=kinh_nghiem_result,
        number_recruits=so_luong,
        gender=gioi_tinh,
        job_feature=tinh_chat,
        type_job=hinh_thuc,
        job_description=job_desc,
        job_requirements=job_requirements,
        why_love_this_job=benefit,
        deadline=deadline,
    )

    for k in post_params:
        LOGGER.debug('****')
        LOGGER.debug(f'{k}: \n {post_params[k]}')

    if not models.Post.objects.filter(
        restaurant_namme=restaurant_name,
        job_description=job_desc,
        deadline=deadline,
        ).exists():
        LOGGER.info('Store new restaurant %r', post_params)

        post = models.Post.objects.create(**post_params)
        job, _ = models.Job.objects.get_or_create(name=name_work)
        job.post.add(post)
        job.save()


if __name__ == '__main__':
    url = "https://www.timviecnhanh.com/viec-lam-du-lich-nha-hang-khach-san-c23.html?page=0"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    divtag = soup.find_all("div", {"class" : "intro col-xs-4 offset20 push-left-10"})
    for a in divtag:
        links = a.find('a')
        link = links.get('href')
        crawl_detail(link)
