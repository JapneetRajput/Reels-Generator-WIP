from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings

change_settings(
    {"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})


def add_text_to_video(video_path, text_data, output_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Split the text into title, body, options, and answer
    title, body, option1, option2, option3, answer = text_data.split('\t')

    # Create TextClips for each part of the text
    title_clip = TextClip(title, fontsize=50, color='black', bg_color='white')
    body_clip = TextClip(body, fontsize=40, color='black', bg_color='white')
    option1_clip = TextClip(option1, fontsize=30,
                            color='black', bg_color='white')
    option2_clip = TextClip(option2, fontsize=30,
                            color='black', bg_color='white')
    option3_clip = TextClip(option3, fontsize=30,
                            color='black', bg_color='white')
    answer_clip = TextClip(answer, fontsize=40,
                           color='black', bg_color='white')

    # Set the duration for each text clip
    title_clip = title_clip.set_duration(15)
    body_clip = body_clip.set_duration(15)
    option1_clip = option1_clip.set_duration(15)
    option2_clip = option2_clip.set_duration(15)
    option3_clip = option3_clip.set_duration(15)
    answer_clip = answer_clip.set_start(15).set_duration(5)

    # Set the position for each text clip
    title_clip = title_clip.set_position(("center", 0.1), relative=True).set_position(("center", 0.1), relative=True).set_position(("center", 0.1), relative=True)
    body_clip = body_clip.set_position(("center", 0.3), relative=True).set_position(("center", 0.3), relative=True)
    option1_clip = option1_clip.set_position((0.35, 0.5), relative=True).set_position((0.35, 0.5), relative=True)
    option2_clip = option2_clip.set_position((0.35, 0.6), relative=True).set_position((0.35, 0.6), relative=True)
    option3_clip = option3_clip.set_position((0.35, 0.7), relative=True).set_position((0.35, 0.7), relative=True)
    answer_clip = answer_clip.set_position(("center", 0.5), relative=True)

    # Concatenate all the text clips
    text_clips = [title_clip, body_clip,
                  option1_clip, option2_clip, option3_clip, answer_clip]
    video_with_text = CompositeVideoClip([video_clip] + text_clips)

    # Write the result to an output file
    video_with_text.write_videofile(
        output_path, codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    video_path = "stock\\coding-bg-1.mp4"
    text_to_overlay = "Exception Expedition	Which Java keyword is used to handle exceptions in a try-catch block?	a) throw	b) exception	c) catch	c) catch"
    output_path = "output_video.mp4"

    add_text_to_video(video_path, text_to_overlay, output_path)
