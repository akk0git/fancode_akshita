from flask import Flask, jsonify
import requests

app = Flask(__name__)

# API endpoints
API_BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_API = f"{API_BASE_URL}/users"
TODOS_API = f"{API_BASE_URL}/todos"
POSTS_API = f"{API_BASE_URL}/posts"
COMMENTS_API = f"{API_BASE_URL}/comments"
ALBUMS_API = f"{API_BASE_URL}/albums"
PHOTOS_API = f"{API_BASE_URL}/photos"

### Lat and Long boundaries for 'FanCode' city
LAT_MIN, LAT_MAX = -40, 5
LONG_MIN, LONG_MAX = 5, 100


def fetch_data(api_url):
    """Fetch data from the given API URL."""
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


def is_fancode_city(user):
    """Check if the user belongs to the city 'FanCode' based on lat and long."""
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    return LAT_MIN <= lat <= LAT_MAX and LONG_MIN <= lng <= LONG_MAX


def calculate_completed_percentage(todos, user_id):
    """Calculate the percentage of completed tasks for the given user."""
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    total_tasks = len(user_todos)
    completed_tasks = sum(todo['completed'] for todo in user_todos)

    return (completed_tasks / total_tasks * 100) if total_tasks else 0


def count_user_posts(posts, user_id):
    """Count how many posts the user has made."""
    return sum(1 for post in posts if post['userId'] == user_id)


def count_user_comments(comments, posts, user_id):
    """Count how many comments the user has made on their posts."""
    user_post_ids = {post['id'] for post in posts if post['userId'] == user_id}
    return sum(1 for comment in comments if comment['postId'] in user_post_ids)


def count_user_albums(albums, user_id):
    """Count how many albums the user has created."""
    return sum(1 for album in albums if album['userId'] == user_id)


def count_user_photos(photos, albums, user_id):
    """Count how many photos the user has uploaded."""
    user_album_ids = {album['id'] for album in albums if album['userId'] == user_id}
    return sum(1 for photo in photos if photo['albumId'] in user_album_ids)


@app.route('/user_statistics', methods=['GET'])
def user_statistics():
    """Fetch user statistics for those in FanCode city."""
    ###Fetch data from APIs
    users = fetch_data(USERS_API)
    todos = fetch_data(TODOS_API)
    posts = fetch_data(POSTS_API)
    comments = fetch_data(COMMENTS_API)
    albums = fetch_data(ALBUMS_API)
    photos = fetch_data(PHOTOS_API)

    results = []

    # Process each user
    for user in users:
        if is_fancode_city(user):
            completed_percentage = calculate_completed_percentage(todos, user['id'])
            post_count = count_user_posts(posts, user['id'])
            comment_count = count_user_comments(comments, posts, user['id'])
            album_count = count_user_albums(albums, user['id'])
            photo_count = count_user_photos(photos, albums, user['id'])

            user_info = {
                "name": user['name'],
                "id": user['id'],
                "completed_percentage": completed_percentage,
                "post_count": post_count,
                "comment_count": comment_count,
                "album_count": album_count,
                "photo_count": photo_count,
                "status": "PASSED" if completed_percentage > 50 else "FAILED"
            }
            results.append(user_info)

    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=True)