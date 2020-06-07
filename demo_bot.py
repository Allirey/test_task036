#!/usr/bin/env python

import configparser
import random
import requests
import json
from faker import Faker

URL = "http://localhost:8000/api/"
fake = Faker()


def create_user():
    username = fake.user_name()
    password = fake.password()
    r = requests.post(URL + 'users/', data={'username': username, 'password': password, 'email': fake.email(), })

    return username, password


def get_token(username, password):
    r = requests.post(URL + 'token/', data={'username': username, 'password': password})
    tokens = json.loads(r.content)

    return tokens['access'], tokens['refresh']


def refresh_access_token(token):
    r = requests.post(URL + 'token/refresh/', data={'refresh': token})

    return json.loads(r.content)['access']


def create_post(access):
    title = fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None)
    content = fake.text(max_nb_chars=200, ext_word_list=None)
    r = requests.post(URL + f'posts/', headers={'Authorization': f'Bearer {access}'},
                      data={'title': title, 'content': content})

    return r.status_code == 201


def like_post(access, post_id):
    r = requests.post(URL + f'posts/{post_id}/like/', headers={'Authorization': f'Bearer {access}'})

    return r.status_code == 201 or json.loads(r.content)['message'] == 'Like already exist'


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    current_posts_number = 0

    max_users = int(config['DEFAULT']['number_of_users'])
    max_posts_per_user = int(config['DEFAULT']['max_posts_per_user'])
    max_likes_per_user = int(config['DEFAULT']['max_likes_per_user'])

    for _ in range(max_users):
        username, password = create_user()
        access, refresh = get_token(username, password)

        for _ in range(max_posts_per_user):
            if create_post(access):
                current_posts_number += 1
            else:
                access = refresh_access_token(refresh)

        for _ in range(max_likes_per_user):
            if not like_post(access, random.randint(1, current_posts_number)):
                access = refresh_access_token(refresh)


if __name__ == '__main__':
    main()
