from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

def add_text_to_video(video_path, text, output_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Split the text into chunks
    text_chunks = text.split('.') # Adjust the chunk size as needed

    # Create a list to hold TextClips for each chunk
    text_clips = []

    # Create a TextClip for each chunk with appropriate duration and position
    total_duration = 0
    for i, chunk in enumerate(text_chunks):
        text_clip = TextClip(chunk, fontsize=50, color='black', bg_color='white')
        text_clip = text_clip.set_duration(5)  # Adjust the duration as needed
        text_clip = text_clip.set_position(("center", 0.1),relative=True)
        text_clip = text_clip.set_start(total_duration)  # Set the start time for each chunk
        total_duration += 5  # Adjust the delay between chunks
        text_clips.append(text_clip)

    # Overlay the text clips on the video clip
    video_with_text = CompositeVideoClip([video_clip] + text_clips)

    # Write the result to an output file
    video_with_text.write_videofile(output_path, codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    video_path = "input_video.mp4"
    text_to_overlay = """This is line 1. This is line 2. This is line 3. Adjust the duration and delay as needed"""
    output_path = "output_video.mp4"

    add_text_to_video(video_path, text_to_overlay, output_path)
