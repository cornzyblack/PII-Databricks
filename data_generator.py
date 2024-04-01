import json
from datetime import datetime
from uuid import uuid4

import click
from mimesis import Person
from mimesis.locales import Locale

person = Person(Locale.EN, seed=100)


@click.command()
@click.option("--rows", default=10, help="Number of greetings.")
def generate_person_details(rows):
    person_data = []
    for _ in range(rows):
        person_info = {
            "customer_id": uuid4(),
            "first_name": person.first_name(),
            "last_name": person.last_name(),
            "email": person.email(),
            "updated_at": datetime.now(),
        }
        person_data.append(person_info)
    with open("sample.json", "w") as f:
        f.write(json.dumps(person_data, default=str))

    click.echo(f"Generated {rows} rows of data")


if __name__ == "__main__":
    generate_person_details()
