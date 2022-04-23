from vapoursynth import core
import vapoursynth as vs
core = vs.core

ruta=r"C:\Users\Ovichan\Desktop\SP1\TVSP1 PID 1011.264"

video = core.lsmas.LWLibavSource(ruta)#


video = core.std.AssumeFPS(video,fpsnum=24000,fpsden=1001)


#show_info
show_info = True

if show_info:
	video = video.text.ClipInfo()

video.set_output()
