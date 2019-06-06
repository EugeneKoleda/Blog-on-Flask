from wtforms import Form, StringField, TextAreaField, MultipleFileField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body post')
    main_image = MultipleFileField('Main image')

