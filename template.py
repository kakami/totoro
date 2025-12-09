import os
import util

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
]

def ffmpeg_cmd(template_name: str, input: str, index: int):
    binary = "/home/test/5.4.0/ffmpeg-n7.1/ffmpeg"
    global_prefix = f"-y  -hide_banner -hwaccel ni_quadra -force_nidec quadra -dec {util.dev} -xcoder-params out=hw"
    param = "crfFloat=23.0:RcEnable=0:rdoLevel=1:lookAheadDepth=4:EnableRdoQuant=1:gopPresetIdx=5:enable2PassGop=1:minFramesDelay=1:enableVFR=1:repeatHeaders=1:GenHdrs=1:intraPeriod=0:zeroCopyMode=0:crfMaxIframeEnable=6:totalCuTreeDepth=6:cuTreeFactor=6"
    _720p = "ni_quadra_scale=1280x720:filterblit=2"
    _540p = "ni_quadra_scale=960x540:filterblit=2"
    _360p = "ni_quadra_scale=640x360:filterblit=2"
    _240p = "ni_quadra_scale=426x240:filterblit=2"

    output = os.path.join(util.output_dir, f"out{index}.mp4")

    # 264
    if template_name == "uhd60":
        return f'{binary} {global_prefix} -i {input} -force_key_frames source  -c:v h264_ni_quadra_enc -xcoder-params "bitrate=5000000:vbvMaxRate=5000000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "uhd":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=30" -force_key_frames source  -c:v h264_ni_quadra_enc -xcoder-params "bitrate=3500000:vbvMaxRate=3500000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "hd60":
        return f'{binary} {global_prefix} -i {input} -filter_complex "{_720p}" -force_key_frames source  -c:v h264_ni_quadra_enc -xcoder-params "bitrate=3000000:vbvMaxRate=3000000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "hd":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=30,{_720p}" -force_key_frames source  -c:v h264_ni_quadra_enc -xcoder-params "bitrate=1800000:vbvMaxRate=1800000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "sd":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=25,{_540p}" -force_key_frames source -c:v h264_ni_quadra_enc -xcoder-params "bitrate=1200000:vbvMaxRate=1200000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "ld":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=20,{_360p}" -force_key_frames source -c:v h264_ni_quadra_enc -xcoder-params "bitrate=600000:vbvMaxRate=600000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "md":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=15,{_240p}" -force_key_frames source -c:v h264_ni_quadra_enc -xcoder-params "bitrate=300000:vbvMaxRate=300000:vbvBufferSize=1000:{param}" {output}'
    
    # 265
    elif template_name == "uhd560":
        return f'{binary} {global_prefix} -i {input} -force_key_frames source  -c:v h265_ni_quadra_enc -xcoder-params "bitrate=5000000:vbvMaxRate=5000000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "uhd5":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=30" -force_key_frames source  -c:v h265_ni_quadra_enc -xcoder-params "bitrate=3000000:vbvMaxRate=3000000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "hd560":
        return f'{binary} {global_prefix} -i {input} -filter_complex "{_720p}" -force_key_frames source  -c:v h265_ni_quadra_enc -xcoder-params "bitrate=2600000:vbvMaxRate=2600000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "hd5":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=30,{_720p}" -force_key_frames source  -c:v h265_ni_quadra_enc -xcoder-params "bitrate=1600000:vbvMaxRate=1600000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "sd5":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=30,{_540p}" -force_key_frames source -c:v h265_ni_quadra_enc -xcoder-params "bitrate=1200000:vbvMaxRate=1200000:vbvBufferSize=1000:{param}" {output}'
    elif template_name == "ld5":
        return f'{binary} {global_prefix} -i {input} -filter_complex "fps=20,{_360p}" -force_key_frames source -c:v h265_ni_quadra_enc -xcoder-params "bitrate=600000:vbvMaxRate=600000:vbvBufferSize=1000:{param}" {output}'

    raise ValueError(f"Unknown template: {template_name}")