def validate_post_data(data,post_id,user_id):
    
    assert "id" in data , "id key missing in response"
    assert isinstance(data['id'], int)
    assert data['id'] == post_id ,  f"Expected id {post_id}, but got {data['id']}"

    assert "title" in data, "title key missing in response"
    assert isinstance(data['title'], str)
    assert len(data['title']) > 10,  f"Expected title length > 10, but got '{data['title']}'"

    assert "userId" in data, "userId key missing in response"
    assert isinstance(data['userId'], int)
    assert data['userId'] == user_id ,  f"Expected user_id {user_id}, but got {data['userId']}"