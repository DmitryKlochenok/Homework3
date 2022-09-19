import json

POSTS_PATH = 'posts.json'

def load_posts() -> list[dict]:
    with open(POSTS_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(search_word):
    with open("posts.json", "r", encoding="utf-8") as f:
      posts_raw = f.read()
    posts_json = json.loads(posts_raw)
    posts_list = []
    for item in posts_json:
        if search_word in item["content"]:
            posts_list.append(item)
    return posts_list

def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path