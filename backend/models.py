class User:

    def __init__(
        self,
        username,
        email,
        password
    ):

        self.username=username
        self.email=email
        self.password=password




class Post:

    def __init__(
        self,
        title,
        content
    ):

        self.title=title
        self.content=content




class Comment:

    def __init__(
        self,
        comment
    ):

        self.comment=comment
