#Copyright 2021 Dhuls-Scratch
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
from scratchclient import ScratchSession
from getpass import getpass
print("Username?")
session = ScratchSession(input(), getpass(prompt='Password: '))
print("Crawl who's followers?")
s_target = input()
count = 0
usersids = {}
while count < len(session.get_user(s_target).get_followers(all=True)):
    usersids[session.get_user(session.get_user(s_target).get_followers(limit=1, offset=count)).username] = session.get_user(session.get_user(s_target).get_followers(limit=1, offset=count)).id
    count = count + 1
    print(usersids)
