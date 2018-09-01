# coding=utf-8
"""
-------------------------------------------------
   File Name ：     crawler.py
   Description :
   Author :         skhe
   Date :           2018/8/24T19:49
-------------------------------------------------
"""
import requests
from requests_html import HTMLSession
from . import datas

session = HTMLSession()


def get_professions() -> list:
    resp = session.get(datas.url_get_profession)
    page = resp.html

    names = [ele.text for ele in page.find('h2')]
    images = [item.attrs.get('src') for item in
              page.xpath('//*[@id="wiki-body"]/div[1]/table/tbody/tr[1]/td[1]/img')]
    remarks = [ele.text for ele in page.xpath('//*[@id="wiki-body"]/div[1]/p')]
    remark_index = [[3, 4], [5], [6], [7], [8], [9, 10], [11], [12]]

    result = [
        {
            "name": name,
            "image": image,
            "start_skills": [ele.text for ele in page.xpath(
                '//*[@id="wiki-body"]/div[1]/table[{}]/tbody/tr[1]/td'.format(i))[2:]],
            "start_attributes": adjust_start_attributes([ele.text for ele in page.xpath(
                '//*[@id="wiki-body"]/div[1]/table[{}]/tbody/tr[position()<4]/td'.format(i)) if ele.text]),
            "start_equipments": [item.attrs.get('src') for item in page.xpath(
                '//*[@id="wiki-body"]/div[1]/table[{}]/tbody/tr[5]/td/img'.format(i))],
            "remarks": [remarks[x] for x in remark_index[i-1]]
        }
        for name, image, i in zip(names, images, range(1, 9))
    ]

    return result


def adjust_start_attributes(items: list) -> dict:
    border = items.index('起始属性')
    result = {k: v for k, v in zip(items[border:][1::2], items[border:][2::2])}
    return result


def main():
    professions = get_professions()
    for profession in professions:
        resp = requests.post(datas.url_post_profession, json=profession)
        print(resp.status_code)


if __name__ == '__main__':
    main()
