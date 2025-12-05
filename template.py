H264TEMPLATES = [
    "uhd60",
    "uhd",
    "hd60",
    "hd",
    "sd",
    "ld",
    "md",
]

H265TEMPLATES = [
    "uhd560",
    "uhd5",
    "hd560",
    "hd5",
    "sd5",
    "ld5",
    "uhd560a",
    "uhd560s",
    "uhd5s",
    "hd5s",
    "hd5c0",
    "hd5c1",
    "hd5c2",
    "hd5c3",
    "hd5d0",
    "hd5d1",
    "hd5d2",
    "hd5d3",
    "hd560a",
    "sd5c",
    "ld5a",
]

def ffmpeg_cmd(template_name: str, index: int):
    if template_name == "uhd60":
        return f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 15 -xcoder-params "out=hw:enableOut1=1:scale1=0x1080" -y  -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -r 60  -c:v h264_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=5000000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/output/out{index}.mp4'
    elif template_name == "uhd":
        return f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 15 -xcoder-params "out=hw:enableOut1=1:scale1=0x1080" -y  -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -r 30  -c:v h264_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=3500000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/output/out{index}.mp4'
    elif template_name == "hd60":
        return f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 15 -xcoder-params "out=hw:enableOut1=1:scale1=0x720" -y  -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -r 60  -c:v h264_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=3000000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/output/out{index}.mp4'
    elif template_name == "hd":
        return f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 15 -xcoder-params "out=hw:enableOut1=1:scale1=0x720" -y  -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -r 30  -c:v h264_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=1800000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/output/out{index}.mp4'
    elif template_name == "sd":
        return f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 15 -xcoder-params "out=hw:enableOut1=1:scale1=0x540" -y  -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -r 25  -c:v h264_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=1200000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/output/out{index}.mp4'
    elif template_name == "ld":
        return f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 15 -xcoder-params "out=hw:enableOut1=1:scale1=0x360" -y  -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -r 20  -c:v h264_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=600000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/output/out{index}.mp4'
    elif template_name == "md":
        return f'/home/test/5.4.0/ffmpeg-n7.1/ffmpeg -y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec 15 -xcoder-params "out=hw:enableOut1=1:scale1=0x240" -y  -i /home/iuz/video/dota_60_1080.mp4 -filter_complex "ni_quadra_merge=filterblit=2" -force_key_frames source -r 15  -c:v h264_ni_quadra_enc -xcoder-params "crfFloat=23.0:RcEnable=0:bitrate=300000:vbvMaxRate=4000000:vbvBufferSize=1000:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=0:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6" /home/iuz/output/out{index}.mp4'
    
    raise ValueError(f"Unknown template: {template_name}")