# from moviepy.editor import VideoFileClip, concatenate_videoclips

# def combine_videos(video_paths, output_path):
#     video_clips = []
    
#     # Load each video clip
#     for path in video_paths:
#         clip = VideoFileClip(path)
#         video_clips.append(clip)
    
#     # Concatenate the video clips in the desired order
#     final_clip = concatenate_videoclips(video_clips)
    
#     # Write the final combined video to the output path
#     final_clip.write_videofile(output_path)
    
#     # Close the clips
#     final_clip.close()
#     for clip in video_clips:
#         clip.close()

# # Example usage
# video_paths = ['./sample_videos/video1.mp4', './sample_videos/video2.mp4']  # Replace with your video file paths
# output_path = '/home/my/Desktop/try/combine-videos/combined_video.mp4'  # Replace with the desired output file path

# combine_videos(video_paths, output_path)

# METHOD 2
# sudo apt-get install python3-tk

from tkinter import Tk, filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips

def combine_videos():
    root = Tk()
    root.withdraw()

    # Prompt the user to select video files
    video_paths = filedialog.askopenfilenames(title='Select Video Files', filetypes=[('Video Files', '*.mp4')])
    video_paths = root.tk.splitlist(video_paths)

    if len(video_paths) == 0:
        print("No videos selected.")
        return

    output_path = filedialog.asksaveasfilename(title='Save Combined Video As', defaultextension='.mp4')

    if not output_path:
        print("No output file selected.")
        return

    video_clips = []
    
    # Load each video clip
    for path in video_paths:
        clip = VideoFileClip(path)
        video_clips.append(clip)
    
    # Concatenate the video clips in the desired order
    final_clip = concatenate_videoclips(video_clips)
    
    # Write the final combined video to the output path
    final_clip.write_videofile(output_path)
    
    # Close the clips
    final_clip.close()
    for clip in video_clips:
        clip.close()

    print("Video successfully combined and saved at", output_path)

# Example usage
combine_videos()