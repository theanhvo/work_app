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

def crawl_template1(link , page):
    LOGGER.info('Crawl detail page %r', link)
    box_content = page.find("div", {"class" : "detail-content box-content"})
    name_work = box_content.h1.text
    print("="*8)
    print(name_work)

    side_bar = page.find("div", {"class" : "block-sidebar"})
    img = side_bar.img
    link_img = img.get('src')
    # print(link_img)

    off_set = page.find("div" , {"class" : "col-xs-6 p-r-10 offset10"})
    asd = off_set.h3.text
    restaurant_name = asd.strip()
    # print(restaurant_name)

    bass = off_set.span.text
    address_11 = bass.strip().split(':')
    address = address_11[1]
    # print(address)

    push_right = page.find_all("div", {"class" : "col-xs-4 offset20 push-right-20"})
    for ab in push_right:
        li_tong = ab.ul.find_all('li')
    muc_luong = li_tong[0].text
    tmp = muc_luong.split(':')
    muc_luong1 = tmp[1].strip().split()
    muc_luong_result = ' '.join(muc_luong1)
    # print(muc_luong_result)

    kinh_nghiem = li_tong[1].text
    gty = kinh_nghiem.split(':')
    kinh_nghiem1 = gty[1].strip().split()
    kinh_nghiem_result = ' '.join(kinh_nghiem1)
    # print(kinh_nghiem_result)

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
    # print(so_luong)
    gnm = li[1].text
    gnm1 = gnm.split(':')
    gioi_tinh = gnm1[1].strip()
    # print(gioi_tinh)
    iuy = li[2].text
    iuy1 = iuy.split(':')
    tinh_chat = iuy1[1].strip()
    # print(tinh_chat)
    dfg = li[3].text
    dfg1 = dfg.split(':')
    hinh_thuc = dfg1[1].strip()
    # print(hinh_thuc)


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
                job_desc1 = row.p.text.strip()
                job_desc = job_desc1.replace('-' , '\n')
            elif title == 'Yêu cầu':
                job_requirements1 = row.p.text.strip()
                job_requirements = job_requirements1.replace('-' , '\n')
            elif title == 'Quyền lợi':
                benefit1 = row.p.text.strip()
                benefit = benefit1.replace('-' , '\n')

            elif title == 'Hạn nộp':
                deadline = row.find('b', {'class': 'text-danger'}).text.strip()

    if len(tables) >= 2:
        rows = tables[1].find_all('tr')
        for row in rows:
            title = row.b.text

            if title == 'Người liên hệ':
                employer_contact = row.p.text.strip()

            elif title == 'Địa chỉ':
                address = row.p.text.strip()

    char = thanh_pho.lower().split()

    if char[0][0] == "h" and char[1][0]=="c" and char[2][0]=="m":
        thanh_pho = models.Post.SG
        print("Thanh pho HCM: True")

    if char[0][0] == "h" and char[1][0]=="n":
        thanh_pho = models.Post.HN
        print("Ha noi: True")

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

def crawl_template2(link, page):
    LOGGER.info('Crawl detail page %r', link)
    tenviec = page.find("div" , {"class" : "info-left"})
    name_work = tenviec.find('h1').text
    print("="*8)
    print(name_work)

    link_pic = page.find("span" , {"id" : "logo_sv_lg"})
    img = link_pic.img
    link_img = img.get('src')
    # print(link_img)

    company_name = page.find("div" , {"class" : "title-banner"})
    restaurant_name = company_name.h1.text
    print(restaurant_name)

    dia_chi =page.find_all("div" , {"class" : "both-contact"})
    rows = []
    if len(dia_chi) >= 1:
        rows = dia_chi[0].find_all('span')
        dong  = rows[1].text.strip()
        dong_split = dong.split(':')
        address = dong_split[1]
        lien_he =rows[0].text
        lien_he1 = lien_he.split(":")
        employer_contact = lien_he1[1].strip()
    # print(address)
    # print(employer_contact)
    divtag = page.find_all("div" , {"class" : "col-lg-6 col-md-12 col-sm-12 col-xs-12 pl0 pr0"})
    muc_luong1 = divtag[0].text
    muc_luong2 = muc_luong1.split(':')
    muc_luong_result = muc_luong2[1].strip()
    # print(muc_luong_result)

    city1 = divtag[1].text
    city2 = city1.split(':')
    thanh_pho = city2[1].strip()
    print(thanh_pho)

    kinh_nghiem1 = divtag[2].text
    kinh_nghiem2 = kinh_nghiem1.split(':')
    kinh_nghiem_result = kinh_nghiem2[1].strip()
    # print(kinh_nghiem_result)

    trinhdo1 = divtag[3].text
    trinhdo2 = trinhdo1.split(':')
    trinh_do = trinhdo2[1].strip()
    # print(trinh_do)

    hinhthuc1 = divtag[4].text
    hinhthuc2 = hinhthuc1.split(':')
    hinh_thuc = hinhthuc2[1].strip()
    # print(hinh_thuc)

    soluong1 = divtag[5].text
    soluong2 = soluong1.split(':')
    so_luong = soluong2[1].strip()
    # print(so_luong)

    gioitinh1 = divtag[6].text
    gioitinh2 = gioitinh1.split(':')
    gioi_tinh = gioitinh2[1].strip()
    # print(gioi_tinh)

    hannop = page.find("div" , {"class" : "hnhs"})
    hannop1 = hannop.text
    hannop2 = hannop1.split(':')
    deadline = hannop2[1].strip()
    # print(deadline)

    des_info = page.find("div" , {"class" : "des-info-job"})
    des_info_result = des_info.find_all('p')
    for lines in des_info_result:
        job_desc = des_info_result[0].text
        # print(job_desc)
        job_requirements = des_info_result[1].text
        # print(job_requirements)
        benefit1 = des_info_result[2].text
        benefit = benefit1.replace("-", "").strip()
        # print(benefit)

    char = thanh_pho.lower().split()

    if char[0][0] == "h" and char[1][0]=="c" and char[2][0]=="m":
        thanh_pho = models.Post.SG
        print("Thanh pho HCM: True")

    if char[0][0] == "h" and char[1][0]=="n":
        thanh_pho = models.Post.HN
        print("Ha noi: True")
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
        type_job=hinh_thuc,
        job_description=job_desc,
        job_requirements=job_requirements,
        why_love_this_job=benefit,
        deadline=deadline,
    )

    for k in post_params:
        LOGGER.debug('****')
        LOGGER.debug(f'{k}: \n {post_params[k]}')

    if not models.Post.objects.filter( # kiem tra ten nha hang ...neu ko co them moi
        restaurant_namme=restaurant_name,
        job_description=job_desc,
        deadline=deadline,
        ).exists():
        LOGGER.info('Store new restaurant %r', post_params)

        post = models.Post.objects.create(**post_params)
        job, _ = models.Job.objects.get_or_create(name=name_work)
        job.post.add(post)
        job.save()


def crawl_detail(link):
    """
    Request to fetch page from url & store Post & Job
    """
    LOGGER.info('Crawl detail page %r', link)

    resp = requests.get(link)
    page = BeautifulSoup(resp.content, "lxml")
    box_content = page.find("div", {"class" : "detail-content box-content"})
    if box_content == None:
        crawl_template2(link, page)
    else:
        crawl_template1(link, page)

if __name__ == '__main__':
    url = "https://www.timviecnhanh.com/viec-lam-du-lich-nha-hang-khach-san-tai-ho-chi-minh-f23p1.html?page=1"
    # https://www.timviecnhanh.com/viec-lam-du-lich-nha-hang-khach-san-tai-ho-chi-minh-f23p1.html?page=1
    # https://www.timviecnhanh.com/viec-lam-du-lich-nha-hang-khach-san-tai-ha-noi-f23p2.html
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    tdtag = soup.find_all("td", {"class" : "block-item w55"})
    for a in tdtag:
        links = a.find('a' , {"class" : "item"})
        link = links.get('href')
        crawl_detail(link)
