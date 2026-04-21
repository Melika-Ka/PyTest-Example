
def test_user(user_controller, db_connection):
    user_controller.add_user(username="jack_brown", email="jack@email.com")

