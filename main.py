from moviepy.editor import VideoFileClip, concatenate_videoclips

def combine_videos(video_paths, output_path):
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

# Example usage
video_paths = ['./sample_videos/video1.mp4', './sample_videos/video2.mp4', './sample_videos/video3.mp4']  # Replace with your video file paths
output_path = '/home/my/Desktop/try/combine-videos/combined_video.mp4'  # Replace with the desired output file path

combine_videos(video_paths, output_path)