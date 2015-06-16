#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

def extract_content_from_html(html):
    soup = BeautifulSoup(html)
    para_list = []
    for tag in soup.find_all('p'):
        text = tag.get_text().strip()
        if len(text) >= 20:
            neighbour_p_count = len(tag.find_next_siblings('p'))
            if neighbour_p_count >= 3:
                para_list.append(text)
                for ptag in tag.find_next_siblings('p'):
                    para_list.append(ptag.get_text().strip())
                break
    content = '\n'.join( para_list )

    return content

