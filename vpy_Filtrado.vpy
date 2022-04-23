from vapoursynth import core
import vapoursynth as vs
import hysteria as hys
core = vs.core

#core.std.LoadPlugin(r"C:\Users\Isra\AppData\Roaming\VapourSynth\plugins64\fmtconv.dll")

pathfile = r"C:\Users\Isra\Desktop\Kami2Kami\Extendida\VE_Japan PID 1011.264"

#Loading file using LSmash
video = core.lsmas.LWLibavSource(pathfile)#, format="YUV420P8")
original = video

#Force fps
video = video.std.AssumeFPS(fpsnum=24000,fpsden=1001)

#Change bitdepth for processing video
video = core.fmtc.bitdepth(video,bits=16)

#Set values for settings of colourimetry. If are present then options are omitted (prefer_props)
video = core.resize.Point(video, matrix_in_s="709", transfer_in_s="709", primaries_in_s="709",range_in_s="limited",prefer_props=True)

#Show info video
showinfo = False
if showinfo:
	video = video.text.ClipInfo()

#FILTERS
#Sharpen
video = core.asharp.ASharp(video,t=1.1,d=2.0,b=-1)

#Deband
video = core.neo_f3kdb.Deband(video,preset="small")

#Back to 8 bits
video = core.fmtc.bitdepth(video,bits=8)

#Output
showStack = False
if showStack:
	original = core.sub.Subtitle(original, "Original")
	video = core.sub.Subtitle(video, "Editado")
	stacked = core.std.Interleave([original,video])
	stacked.set_output()
else:
	video.set_output()
