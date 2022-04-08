from user import User
from post import Post

app_user_one = User("aa@nn.com", "fl", "pwd", "it-guy")
app_user_one.get_user_info()

app_user_two = User("bb@nn.com", "Ul", "pwd", "it-girl")
app_user_two.get_user_info()

app_user_one.change_job_title("Mopped")
app_user_one.get_user_info()


new_post = Post("on a secret mopped mission today", "James Bond")
new_post.get_post_info()

"""def add_new_skill():
    #asd """

