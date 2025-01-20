

"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
            "id":0,
            "first_name": "John",
            "last_name": last_name,
            "age":33,
            "lucky_numbers": [7,13,22]},
            {
            "id":1,
            "first_name": "Jane",
            "last_name": last_name,
            "age":35,
            "lucky_numbers": [10,14,3]},
            {
            "id":2,
            "first_name": "Jimmy",
            "last_name": last_name,
            "age":5,
            "lucky_numbers": [1]},
            ]
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        
        new_member={**member,
            "id":self._generateId(),
            "last_name":self.last_name,
          }
        self._members.append(new_member)
        

    def delete_member(self, id):
        for item in self._members:
            if item["id"]==id:
                self._members.remove(item)

    def get_member(self, id):
        for item in self._members:
            if item["id"]==id:
                return item
        
        
    def get_all_members(self):
        return self._members

