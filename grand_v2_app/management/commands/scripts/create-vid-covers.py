import os
import cv2

# Define the folder path where the .mp4 files are located (use absolute paths if needed)
folder_path = 'd:/current/code/grand_v2_project/media/03/celeste/t/'
output_folder =  'd:/current/code/grand_v2_project/media/03/celeste/t/'

# Desired aspect ratio for the container (16:9)
target_aspect_ratio = 16 / 9

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all .mp4 files in the folder
mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

# Loop through the .mp4 files
for mp4_file in mp4_files:
    # Full path to the video file
    video_path = os.path.join(folder_path, mp4_file)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was successfully opened
    if not cap.isOpened():
        print(f"Failed to open video file: {mp4_file}")
        continue

    # Set the frame position to 5 seconds (assuming 30 fps, change if different)
    cap.set(cv2.CAP_PROP_POS_MSEC, 5000)  # 5000 ms = 5 seconds

    # Read the frame
    success, frame = cap.read()

    if success:
        # Get the original width and height of the frame
        original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(f"Original dimensions for {mp4_file}: {original_width}x{original_height}")

        # Calculate the aspect ratio of the original frame
        original_aspect_ratio = original_width / original_height

        # Determine if we need to crop the image
        if original_aspect_ratio > target_aspect_ratio:
            # Image is too wide, resize by height and crop width
            target_height = 720  # Set the desired height (for example, 720 pixels)
            target_width = int(target_height * original_aspect_ratio)
            resized_frame = cv2.resize(frame, (target_width, target_height))

            # Crop width to maintain 16:9 aspect ratio
            crop_width = int(target_height * target_aspect_ratio)
            start_x = (target_width - crop_width) // 2
            cropped_frame = resized_frame[:, start_x:start_x + crop_width]

        elif original_aspect_ratio < target_aspect_ratio:
            # Image is too tall, resize by width and crop height
            target_width = 1280  # Set the desired width (for example, 1280 pixels)
            target_height = int(target_width / original_aspect_ratio)
            resized_frame = cv2.resize(frame, (target_width, target_height))

            # Crop height to maintain 16:9 aspect ratio
            crop_height = int(target_width / target_aspect_ratio)
            start_y = (target_height - crop_height) // 2
            cropped_frame = resized_frame[start_y:start_y + crop_height, :]

        else:
            # No need to crop, just resize to the target size
            target_width = 1280
            target_height = 720
            cropped_frame = cv2.resize(frame, (target_width, target_height))

        # Extract the file name without extension
        file_name = os.path.splitext(mp4_file)[0]

        # Construct the output .jpg file path using .format() instead of f-strings
        poster_path = os.path.join(output_folder, '{}.jpg'.format(file_name))

        # Save the cropped frame as a .jpg image
        if cv2.imwrite(poster_path, cropped_frame):
            print(f'Saved poster for {mp4_file} as {file_name}.jpg')
        else:
            print(f"Failed to save poster for {mp4_file}")
    else:
        print(f'Failed to capture frame from {mp4_file}')

    # Release the video capture object
    cap.release()

print("Finished saving posters for all .mp4 files.")
