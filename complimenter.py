import json
import os
import random
from datetime import datetime
from time import sleep

import requests


def read_db():
    with open("data/team.json") as data:
        return json.load(data)


def get_random_team_member():
    team_members = read_db()
    return random.choice(team_members)


def get_random_compliment(team_member):
    return random.choice(team_member["compliments"])


def send(compliment_message):
    slack_token = os.environ.get("SLACK_BOT_TOKEN")
    slack_channel = '#ext-tech'
    slack_icon_emoji = ':see_no_evil:'
    slack_user_name = 'happy-bot'

    requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': compliment_message,
        'icon_emoji': slack_icon_emoji,
        'username': slack_user_name,
        'blocks': None
    })

    print("{} - {}".format(datetime.now().strftime("%H:%M:%S"), compliment_message))


def compliment():
    team_member = get_random_team_member()
    compliment_message = get_random_compliment(team_member)
    send(compliment_message)


def main():
    # Represented in minutes
    compliments_interval = 10
    program_duration = 120

    for i in range(int(program_duration / compliments_interval)):
        compliment()
        sleep(compliments_interval * 60)


if __name__ == "__main__":
    main()
