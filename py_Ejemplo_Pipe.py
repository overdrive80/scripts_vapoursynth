#your script
import subprocess
import vapoursynth as vs
from vapoursynth import core

input=r'C:\path_to_video\video.mkv'
clip = core.ffms2.Source(input)
#clip.set_output()   #this you comment out


#add this to the bottom of your script, adjust whatever you need

output = r'C:\destination\video.264'
x264 = r'C:\path\x264-64bit.exe'

cmd = [x264, '--frames',           f'{len(clip)}',
             '--input-csp',         'i420',
             '--demuxer',           'raw',  
             '--input-depth',       '8',
             '--input-res',        f'{clip.width}x{clip.height}',
             '--fps',              f'{clip.fps_num}/{clip.fps_den}',
             '--crf',               '18',
             '--colorprim',         'bt709',
             '--transfer',          'bt709',
             '--colormatrix',       'bt709',
             '--output',             output,
             '-']
process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
clip.output(process.stdin)
process.communicate()