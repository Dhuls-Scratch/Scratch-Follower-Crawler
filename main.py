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
import requests
import json
print("Username?")
s_user = input()
print("Password?")
s_pass = input()
session = ScratchSession(s_user, s_pass)
print("Crawl who's followers?")
s_target = input()
s_targetdb = requests.get("https://scratchdb.lefty.one/v3/user/info/%s" % s_target)
print(s_targetdb)