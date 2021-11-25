from time import sleep
import json
import random


def read_db():
    with open("data/team.json") as data:
        return json.load(data)


def get_random_team_member():
    teams_members = read_db()
    return random.choice(teams_members)


def get_random_compliment(team_member):
    compliment_message = ""
    # TODO: Somehow get random message (maybe in correlation to team member profile data?)
    return compliment_message


def send(compliment_message):
    # TODO: Connect to Slack bot and send message
    pass


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


if __name__ is "__main__":
    main()
