from vapoursynth import core
import vapoursynth as vs
from vscomparevideos import comparevideos
core = vs.core

#Filenames in root path
pathfile1 = r"Dragon Ball Z - TV Special 2 [1080p] [x264] [GYAO].ts"
pathfile2 = r"00006.m2ts"

#Loading file using LSmash
video1 = core.lsmas.LWLibavSource(pathfile1).std.AssumeFPS(fpsnum=30000,fpsden=1000)
video2 = core.lsmas.LWLibavSource(pathfile2).std.AssumeFPS(fpsnum=24000,fpsden=1001)

#change matrix
video1 = core.fmtc.resample(clip = video1, css="444")
video1 = core.fmtc.matrix(clip = video1, mats = "709", matd = "601", bits = 16)
video1 = core.fmtc.resample(clip = video1, css="420")
video1 = core.fmtc.bitdepth(clip = video1, bits = 8)#, fulls=True, fulld=False)

#video1 = core.fmtc.resample(clip = video1, css="444")
#video1 = core.fmtc.matrix(clip = video1, mat="709", col_fam=vs.RGB)
#video1 = core.fmtc.bitdepth(clip = video1, bits = 8)#, fulls=False, fulld=True)


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
last_frame_v2=video2.num_frames+1

#Initial crop for webdl
video1 = video1[360:]

#Eyecatchs
eyecatch1 = video1[17400:17699]
eyecatch2 = video1[33240:33540]
eyecatch3 = video1[49440:49739]

video2 = video1[0:67] + video2
video2 = video2[0:2760] + video1[2760:2766] + video2[2760:] 
video2 = video2[0:17400] + eyecatch1 + video2[17400]*7 +video2[17400:]
video2 = video2[0:33240] + eyecatch2 + video1[33540:33546]+ video2[33240:]
video2 = video2[0:49440] + eyecatch3 + video2[49440]*4 + video2[49440:]
video2 = video2[0:66676] + video2[66675] + video2[66676:69119]

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