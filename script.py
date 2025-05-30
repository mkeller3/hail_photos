import os

PHOTO_DIR = "photos"

def get_list_of_photos():
    """Returns a list of photo file names in the PHOTO_DIR."""
    if not os.path.exists(PHOTO_DIR):
        return []
    
    return [f for f in os.listdir(PHOTO_DIR) if os.path.isfile(os.path.join(PHOTO_DIR, f))]

for photo in get_list_of_photos():
    print(f"![](./photos/{photo})")