import vapoursynth as vs
core = vs.core

ruta=r"C:\Users\Isra\Desktop\Broly\jpn\vpy_Filtrado.avi"

video = core.lsmas.LWLibavSource(ruta)

video = core.std.AssumeFPS(video,fpsnum=24000,fpsden=1001)

video.set_output()
