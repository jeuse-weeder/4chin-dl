#!/usr/bin/env python3

import requests
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="The url of the thread")
args = parser.parse_args()

def generate_url(thread):
    thread_id = thread.split("/")[-1]
    board = thread.split("/")[3]
    final_url = "https://a.4cdn.org/{}/thread/{}.json".format(board, thread_id)

    return final_url


def get_json(json_url):
    r = requests.get(json_url)
    json = r.content
    return json


def download_thread(json_data, board):
    c = json.loads(json_data)
    for i in c["posts"]:
        try:
            filename = "{}{}".format(i["tim"], i["ext"])
            file_url = "https://i.4cdn.org/{}/{}".format(board, filename)
            print("Downloading {}".format(file_url))
            w = requests.get(file_url)
            with open(filename, 'wb') as f:
                f.write(w.content)

        except KeyError:
            return ""


if args.url == None or args.url == "":
    print("You need to specify the url")
    exit(-1)

q = args.url
board = q.split("/")[3]
api_url = generate_url(q)
shit = get_json(api_url)
download_thread(shit, board)
