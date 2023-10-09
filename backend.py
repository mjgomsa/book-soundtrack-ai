import openai

openai.api_key = 'Please see my email for API key.'




# Get Book Title from User
# ========================

def get_book_title():
    return input("What book are you reading? ")

# Get Book Genre from Book Title
# ==============================

def get_book_genre(book_title):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Based on the book title '{book_title}', determine the genre that the book fits into."}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=messages
    )
    book_genre = response.choices[0].message['content'].strip()
    return book_genre

# Map Book Genre to Music Genre using GPT-4
# =========================================

def map_to_music_genre(book_genre):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Based on the book's genre '{book_genre}', map to a music genre."}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=messages
    )
    music_genre = response.choices[0].message['content'].strip()
    return music_genre

# Generate Sonic Pi Code using GPT-4
# ==================================

def generate_sonic_pi_code(music_genre):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Based on the music genre '{music_genre}', create code for a song within that music genre for Sonic Pi."}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=messages
    )
    sonic_pi_code = response.choices[0].message['content'].strip()
    return sonic_pi_code



# Play Music using Sonic Pi
# =========================

# def play_music(sonic_pi_code):


#    # TODO: MJ pls help me with this


#    print(f"Generated Sonic Pi Code: {sonic_pi_code}")



# Main Function
# =============

def main():
    book_title = get_book_title()
    book_genre = get_book_genre(book_title)
    music_genre = map_to_music_genre(book_genre)
    sonic_pi_code = generate_sonic_pi_code(music_genre)

    # This was just a test
    print(f"Book Title: {book_title}")
    print("=== SONIC PI CODE ===")
    print(sonic_pi_code)

main()
