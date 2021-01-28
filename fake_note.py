from faker import Faker

from app import create_app
from notes.models import Notes

fake = Faker()

my_word_list = [
'danish','cheesecake','sugar',
'Lollipop','wafer','Gummies',
'sesame','Jelly','beans',
'pie','bar','Ice','oat' ]
app = create_app()

def create_fake_notes():
    with app.app_context():
        for i in range(25):
            title = fake.sentence(ext_word_list=my_word_list)
            content = fake.text()
            note = Notes(title=title, body=content)
            note.save()
            return f'saving note {i+1} ...'
    return 'All notes was saved'

if __name__ == '__main__':
    create_fake_notes()
