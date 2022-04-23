from vapoursynth import core
import vapoursynth as vs
core = vs.core

pathfile1 = r"C:\Users\Isra\Downloads\DBZ Movie 15 - Resurrection F\[Pendekar] Dragon Ball Z - Movie 15 - Resurrection F [3D] [HalfSBS] [Dual Audio].mkv"
pathfile2 = r"C:\Users\Isra\Desktop\[EvoShare] Dragon Ball Z Movie 15.mkv"

#Loading file using LSmash
video1 = core.lsmas.LWLibavSource(pathfile1)#, format="YUV420P8")
video2 = core.lsmas.LWLibavSource(pathfile2)

#Force fps
video1 = video1.std.AssumeFPS(fpsnum=24000,fpsden=1001)
video2 = video2[0]*24+video2.std.AssumeFPS(fpsnum=24000,fpsden=1001) #video2[0]*47+

#Output
video1 = core.sub.Subtitle(video1, "Pendekar")
video2 = core.sub.Subtitle(video2, "EvoShare")
stacked = core.std.Interleave([video1,video2])
stacked.set_output()

