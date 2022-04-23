from vapoursynth import core
import vapoursynth as vs
import hysteria as hys
core = vs.core

#core.std.LoadPlugin(r"C:\Users\Isra\AppData\Roaming\VapourSynth\plugins64\fmtconv.dll")

pathfile = r"C:\Users\Isra\Desktop\Res_F\JPN PID 1011.264"

#Loading file using LSmash
#video = core.lsmas.LWLibavSource(pathfile)#, format=vs.YUV420P8")
video = core.ffms2.Source(pathfile, format=vs.YUV420P8)

#Force fps
video = video.std.AssumeFPS(fpsnum=24000,fpsden=1001)
original = video

#Change bitdepth for processing video
video = core.fmtc.bitdepth(video,bits=16)

#Set values for settings of colourimetry. If are present then options are omitted (prefer_props)
video = core.resize.Point(video, matrix_in_s="709", transfer_in_s="709", primaries_in_s="709",range_in_s="limited",prefer_props=True)

#FILTERS
#Sharpen
video = core.asharp.ASharp(video,t=0.5,d=1.6,b=-1)

#Deband
video = core.neo_f3kdb.Deband(video,preset="small")

#Back to 8 bits
video = core.fmtc.bitdepth(video,bits=8)

#video = core.std.SelectEvery(video, cycle=25, offsets=1)
# Select every 10%
#video = video[0::10]

# Select every 5%. cycle = 100 / 5
video = video[0::20]

#Ajust framerate
video = video.std.AssumeFPS(fpsnum=24000,fpsden=1001)
video.set_output()
