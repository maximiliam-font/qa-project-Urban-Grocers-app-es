import sender_stand_request
import data

# Retrieves the name of the kit that was created by the user
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

# Code to retrieve the authentication token of the newly created user
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_user_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_user_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

    # Test_1
def test_create_kit_with_1_character_name():
    new_kit_body = get_kit_body("a")
    positive_assert(new_kit_body)

    # Test_2
def test_create_kit_with_name_max_511_characters():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

    # Test_3
def test_kit_name_empty_should_return_400():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

    # Test_4
def test_kit_name_max_length_512_returns_400():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(new_kit_body)

    # Test_5
def test_kit_name_allows_special_characters_returns_201():
    new_kit_body = get_kit_body("\"№%@\",\"")
    positive_assert(new_kit_body)

    # Test_6
def test_kit_name_allows_leading_trailing_spaces_returns_201():
    new_kit_body = get_kit_body("A Aaa")
    positive_assert(new_kit_body)

    # Test_7
def test_kit_name_allows_numbers_returns_201():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)

    # Test_8
def test_kit_creation_with_empty_body_returns_400():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

    # Test_9
def test_kit_name_as_number_returns_400():
    new_kit_body = get_kit_body(123)
    negative_assert_code_400(new_kit_body)
