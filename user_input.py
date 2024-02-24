# Copyright 2024 Steve Nginyo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Ask for user's name
name = input("What is your name? ")

# Ask for user's age
age = input("How old are you? ")

# Ask for user's location
location = input("Where do you live?")

# Print personalized message
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))