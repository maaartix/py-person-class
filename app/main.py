class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = []
    for person in people:
        person_to_add = Person(person["name"], person["age"])
        person_list.append(person_to_add)

    for person in people:
        current_person = Person.people[person.get("name")]

        if person.get("wife") is not None:
            current_person.wife = Person.people[person["wife"]]

        if person.get("husband") is not None:
            current_person.husband = Person.people[person["husband"]]

    return person_list
