import glob
import moviepy.editor as mpy

gif_name = 'profiles'
fps = 15
file_list = glob.glob('/senior_design/amination_new/output/done4/*.png')
print(file_list) # Get all the pngs in the current directory
list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)
