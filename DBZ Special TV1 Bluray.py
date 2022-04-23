from vapoursynth import core
import vapoursynth as vs
core = vs.core

def change_matrix(clip, mats, matd):
	video = clip

	video = core.fmtc.resample(clip = video , css="444")
	video = core.fmtc.matrix(clip = video , mats = mats, matd = matd, bits = 16)
	video = core.fmtc.resample(clip = video , css="420")
	video = core.fmtc.bitdepth(clip = video , bits = 8)
	
	return video

#Filenames in root path
pathfile1 = r"Dragon Ball Z - TV Special 1 [1080p] [x264] [GYAO].ts"
pathfile2 = r"00016.m2ts"

#Loading file using LSmash
video1 = core.lsmas.LWLibavSource(pathfile1).std.AssumeFPS(fpsnum=30000,fpsden=1000)
video2 = core.lsmas.LWLibavSource(pathfile2).std.AssumeFPS(fpsnum=24000,fpsden=1001)

#IVTC/Deinterlace
video1 = core.tivtc.TDecimate(video1,mode=7,rate=23.976,dupThresh=0.9, display=False,maxndl=5)
video1 = core.grain.Add(video1,var=6.9, uvar=0.0, constant=True)

#Force fps
video1 = video1.std.AssumeFPS(fpsnum=24000,fpsden=1001)
video2 = video2.std.AssumeFPS(fpsnum=24000,fpsden=1001) #video2[0]*47+  video2[0]*24+

#Crooping
video1 = video1.std.Crop(left=240,right=240)
video2 = video2.std.Crop(left=240,right=240)

#Metrics adjustment
 #Initial crop for webdl
video1 = video1[360:]

 #Eyecatchs
eyecatch1 = video1[17807:18149]
eyecatch2 = video1[33240:33582]
eyecatch3 = video1[49751:50093]

video2 = video2[0:17807] + eyecatch1 + video2[17807] + video2[17807:]
video2 = video2[0:33095] + video2[33095-5:33095] + video1[33100:33240] + eyecatch2 + video2[33095:]
video2 = video2[0:49751] + eyecatch3 + video2[49752:]
video2 = video2[0:69069] 

resto = video2[68879:]

#change matrix
resto = change_matrix(clip=resto, mats="709", matd="601")

video2 = video2[0:68879] + resto

subtitles = False

if subtitles:
    video1= core.sub.Subtitle(video1,"WEBDL")
    video2= core.sub.Subtitle(video2,"BD")

stack = False

if stack:
    video = core.std.StackHorizontal([video1, video2])

    video.set_output()
    
    exit()

video2.set_output()