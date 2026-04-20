class TestUser:
    def test_1_add_user(self, function_fixture, module_fixture, session_fixture, class_fixture):
        print("   Running test_1_add_user")
        assert function_fixture == "function_value"
        assert module_fixture == "module_value"
    def test_2_delete_user(self, function_fixture, module_fixture, session_fixture, class_fixture):
        print("   Running test_2_delete_user")
        assert True
    def test_3_update_user(self, function_fixture, module_fixture, session_fixture, class_fixture):
        print("   Running test_3_update_user")
        assert True



def test_outside_class(function_fixture, module_fixture, session_fixture):
    print("   Running test_outside_class")
    assert True