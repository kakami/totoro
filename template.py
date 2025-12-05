# template.py

H264_TEMPLATES = {
    "_uhd60",
    "_uhd",
    "_hd60",
    "_hd",
    "_sd",
    "_ld",
}

H265_TEMPLATES = {
    "_uhd560",
    "_uhd5",
    "_hd560",
    "_hd5",
    "_sd5",
    "_ld5",
    "_uhd560a",
    "_uhd560s",
    "_uhd5s",
    "_hd5s",
    "_hd5c0",
    "_hd5c1",
    "_hd5c2",
    "_hd5c3",
    "_hd5d0",
    "_hd5d1",
    "_hd5d2",
    "_hd5d3",
    "_hd560a",
    "_sd5c",
    "_ld5a",
}

H264_PARAMS = {
    "_uhd60": {
        "gear": "Ultra high definition 60fps",
        "resolution": "1080P",
        "fps": "60fps",
        "video_codec": "h264",
        "video_bitrate": "5M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "high",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "b_frame": 3,
    },
    "_uhd": {
        "gear": "Ultra high definition",
        "resolution": "1080P",
        "fps": "30fps",
        "video_codec": "h264",
        "video_bitrate": "3.5M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "high",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "b_frame": 3,
    },
    "_hd60": {
        "gear": "High definition 60fps",
        "resolution": "720P",
        "fps": "60fps",
        "video_codec": "h264",
        "video_bitrate": "3M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "high",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "b_frame": 3,
    },
    "_hd": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "h264",
        "video_bitrate": "1.8M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "high",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "b_frame": 3,
    },
    "_sd": {
        "gear": "Standard Definition",
        "resolution": "540P",
        "fps": "25fps",
        "video_codec": "h264",
        "video_bitrate": "1.2M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "high",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "b_frame": 3,
    },
    "_ld": {
        "gear": "Low Definition",
        "resolution": "360P",
        "fps": "20fps",
        "video_codec": "h264",
        "video_bitrate": "600K",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "high",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "b_frame": 3,
    },
    "_md": {
        "gear": "Review",
        "resolution": "240P",
        "fps": "15fps",
        "video_codec": "h264",
        "video_bitrate": "300K",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "high",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "b_frame": 3,
    },
}

# template.py

H265_PARAMS = {
    "_uhd560": {
        "gear": "Ultra high definition 60fps",
        "resolution": "1080P",
        "fps": "60fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=22.5maxrate=4000vbvbuffer=4000",
        "b_frame": 3,
        "ipratio": 0.5,
        "scale": "bicubic",
        "opengop": 0,
    },
    "_uhd5": {
        "gear": "Ultra high definition",
        "resolution": "1080P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "3M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "params": None,
        "b_frame": None,
        "ipratio": None,
        "scale": None,
        "opengop": None,
    },
    "_hd560": {
        "gear": "High definition 60fps",
        "resolution": "720P",
        "fps": "60fps",
        "video_codec": "hevc",
        "video_bitrate": "2.6M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "params": None,
        "b_frame": None,
        "ipratio": None,
        "scale": None,
        "opengop": None,
    },
    "_hd5": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.6M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "params": None,
        "b_frame": None,
        "ipratio": None,
        "scale": None,
        "opengop": None,
    },
    "_sd5": {
        "gear": "Standard Definition",
        "resolution": "540P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=22.5maxrate=1150kvbvbuffer=1300k",
        "b_frame": 3,
        "ipratio": 0.5,
        "scale": "bicubic",
        "opengop": 0,
    },
    "_ld5": {
        "gear": "Low Definition",
        "resolution": "360P",
        "fps": "20fps",
        "video_codec": "hevc",
        "video_bitrate": "600K",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "params": None,
        "b_frame": None,
        "ipratio": None,
        "scale": None,
        "opengop": None,
    },

    "_uhd560a": {
        "gear": "Ultra high definition 60fps",
        "resolution": "1080P",
        "fps": "60fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=22.5maxrate=4000vbvbuffer=4000",
        "b_frame": 3,
        "ipratio": 0.5,
        "scale": "bicubic",
        "opengop": 0,
    },

    "_uhd560s": {
        "gear": "Ultra high definition 60fps",
        "resolution": "1080P",
        "fps": "60fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf21.5，maxrate=3800，vbvbuffer=3800",
        "b_frame": 3,
        "ipratio": 0.5,
        "scale": "bicubic",
        "opengop": 0,
    },

    "_uhd5s": {
        "gear": "Ultra high definition",
        "resolution": "1080P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf21.5，maxrate=3600，vbvbuffer=3800",
        "b_frame": None,
        "ipratio": None,
        "scale": None,
        "opengop": None,
    },

    "_hd5s": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf21.5，maxrate=2000，vbvbuffer=2200",
        "b_frame": None,
        "ipratio": None,
        "scale": None,
        "opengop": None,
    },

    "_hd5c0": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.4M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=26maxrate=vbvbuf=1.4m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd5c1": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.4M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=25maxrate=vbvbuf=1.5m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd5c2": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.6M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=24maxrate=vbvbuf=1.65m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd5c3": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.6M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=24maxrate=vbvbuf=1.75m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd5d0": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.4M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=26maxrate=vbvbuf=1.4m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd5d1": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.4M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=25maxrate=vbvbuf=1.5m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd5d2": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.6M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=24maxrate=vbvbuf=1.65m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd5d3": {
        "gear": "High definition",
        "resolution": "720P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": "1.6M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=24maxrate=vbvbuf=1.75m",
        "b_frame": 3,
        "ipratio": 0.3,
        "scale": None,
        "opengop": None,
    },

    "_hd560a": {
        "gear": "High definition 60fps",
        "resolution": "720P",
        "fps": "60fps",
        "video_codec": "hevc",
        "video_bitrate": "2.6M",
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "ABR",
        "params": None,
        "b_frame": None,
        "ipratio": None,
        "scale": None,
        "opengop": None,
    },

    "_sd5c": {
        "gear": "Standard Definition",
        "resolution": "540P",
        "fps": "30fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=22.5maxrate=1150kvbvbuffer=1300k",
        "b_frame": 3,
        "ipratio": 0.5,
        "scale": "bicubic",
        "opengop": 0,
    },

    "_ld5a": {
        "gear": "Low Definition",
        "resolution": "360P",
        "fps": "20fps",
        "video_codec": "hevc",
        "video_bitrate": None,
        "audio_codec": "aac",
        "audio_bitrate": "copy",
        "limit_small_to_large": "Yes",
        "adapt_vertical_size": "Yes",
        "vpreset": "medium",
        "profile": "main",
        "me_method": "dia",
        "rc_lookahead": 4,
        "qmin": 15,
        "gop": "copy",
        "video_ratecontrol": "CRF",
        "params": "crf=24maxrate=600vbvbuffer=600",
        "b_frame": 3,
        "ipratio": 0.5,
        "scale": None,
        "opengop": None,
    },
}

def get_template_params(name: str):
    """返回 (codec_type, params)"""
    if name in H264_TEMPLATES:
        return "h264", H264_PARAMS.get(name)

    if name in H265_TEMPLATES:
        return "h265", H265_PARAMS.get(name)

    return None, None

# template.py (省略你的模板定义部分)

def build_ffmpeg_cmd(template_name: str, input_file: str, output_file: str):
    codec, params = get_template_params(template_name)
    if params is None:
        raise ValueError(f"Unknown template: {template_name}")

    if codec == "h264":
        return _build_h264_cmd(params, input_file, output_file)
    else:
        return _build_h265_cmd(params, input_file, output_file)


def _build_h264_cmd(p: dict, inp: str, out: str):
    cmd = ["/home/test/5.4.0/ffmpeg-n7.1/ffmpeg", "-y", "-i", inp]

    # 视频编码器
    cmd += ["-c:v", "h264_ni_quadra_enc"]

    # FPS
    fps_raw = p.get("fps")
    if fps_raw and fps_raw not in ("copy", ""):
    # 去掉大小写混合的 "fps"
        clean = str(fps_raw).lower().replace("fps", "").strip()
        # 例如 "60fps" -> "60" ； "30" -> "30"
        try:
            fps_val = str(float(clean)).rstrip("0").rstrip(".")
            cmd += ["-r", fps_val]
        except:
            pass

    # 分辨率映射（示例）
    if "resolution" in p and p["resolution"]:
        mapping = {"1080P": "1920:1080", "720P": "1280:720", "540P": "960:540", "360P": "640:360"}
        res = p["resolution"].upper()
        if res in mapping:
            cmd += ["-vf", f"scale={mapping[res]}"]

    # preset/profile
    # if p.get("vpreset"):
        # cmd += ["-preset", p["vpreset"]]
    if p.get("profile"):
        cmd += ["-profile:v", p["profile"]]

    # Rate control: ABR or others
    ratecontrol = p.get("ratecontrol") or p.get("video_ratecontrol")
    vbit = p.get("vbitrate") or p.get("video_bitrate")
    params_field = p.get("params")  # optional string containing maxrate/vbvbuffer etc.

    if ratecontrol == "ABR":
        if vbit and vbit != "-" and vbit is not None:
            cmd += ["-b:v", vbit]
    else:
        # 如果模板里包含 params（例如 x264 参数、maxrate/bufsize 等），尝试解析并添加
        if params_field:
            # 简单解析 maxrate / vbvbuffer / bufsize
            import re
            maxrate = re.search(r"maxrate[=\:]\s*([0-9a-zA-Z]+)", params_field)
            bufsize = re.search(r"(?:vbvbuffer|vbvbuf|bufsize)[=\:]\s*([0-9a-zA-Z]+)", params_field)
            if maxrate:
                cmd += ["-maxrate", maxrate.group(1)]
            if bufsize:
                cmd += ["-bufsize", bufsize.group(1)]
            # 若 params 包含 crf
            crf = re.search(r"crf[=\:]\s*([0-9\.]+)", params_field)
            if crf:
                cmd += ["-crf", crf.group(1)]

    # GOP / bframes / me_method / rc-lookahead / qmin
    if p.get("gop") and p.get("gop") != "copy":
        try:
            cmd += ["-g", str(int(p["gop"]))]
        except Exception:
            pass
    if p.get("bframe") is not None:
        cmd += ["-bf", str(p["bframe"])]
    if p.get("me_method"):
        cmd += ["-me_method", p["me_method"]]
    if p.get("rc_lookahead") is not None:
        cmd += ["-rc-lookahead", str(p["rc_lookahead"])]
    if p.get("qmin") is not None:
        cmd += ["-qmin", str(p["qmin"])]

    # audio
    cmd += ["-c:a", p.get("audio_codec_type", p.get("audio_codec", "aac"))]

    return " ".join(cmd + [out])


def _build_h265_cmd(p: dict, inp: str, out: str):
    cmd = ["ffmpeg", "-i", inp]

    cmd += ["-c:v", "libx265"]

    # preset/profile
    if p.get("vpreset"):
        cmd += ["-preset", p["vpreset"]]
    if p.get("profile"):
        cmd += ["-profile:v", p["profile"]]

    # handle scale mapping if resolution present
    if "resolution" in p and p["resolution"]:
        mapping = {"1080P": "1920:1080", "720P": "1280:720", "540P": "960:540", "360P": "640:360"}
        res = p["resolution"].upper()
        if res in mapping:
            cmd += ["-vf", f"scale={mapping[res]}"]

    ratecontrol = p.get("ratecontrol") or p.get("video_ratecontrol")
    vbit = p.get("vbitrate") or p.get("video_bitrate")
    params_field = p.get("params")

    if ratecontrol == "ABR":
        if vbit and vbit != "-" and vbit is not None:
            cmd += ["-b:v", vbit]
    elif ratecontrol == "CRF":
        # 解析 params 字段中的 crf/maxrate/vbvbuffer/bufsize
        import re
        crf = None
        maxrate = None
        vbv = None
        if params_field:
            s = params_field.replace("，", ",")
            for kv in s.split(","):
                kv = kv.strip()
                if "crf=" in kv:
                    crf = kv.split("=", 1)[1]
                elif "maxrate=" in kv:
                    maxrate = kv.split("=", 1)[1]
                elif "vbvbuffer=" in kv or "vbvbuf=" in kv or "bufsize=" in kv:
                    vbv = kv.split("=", 1)[1]
        if crf:
            cmd += ["-crf", crf]
        if maxrate:
            cmd += ["-maxrate", maxrate]
        if vbv:
            cmd += ["-bufsize", vbv]

    # bframes
    if p.get("bframe") is not None:
        cmd += ["-bf", str(p["bframe"])]

    # x265 specific params: ipratio / opengop -> combine into single -x265-params if multiple
    x265_params = []
    if p.get("ipratio") is not None:
        x265_params.append(f"ipratio={p['ipratio']}")
    if p.get("opengop") is not None:
        x265_params.append(f"open-gop={p['opengop']}")
    # 如果 params_field 包含其它 x265-params 风格的配置，保留原样追加
    if params_field and "x265" in (params_field.lower()):  # 保守追加条件
        x265_params.append(params_field)
    if x265_params:
        cmd += ["-x265-params", ":".join(x265_params)]

    # audio
    cmd += ["-c:a", p.get("audio_codec_type", p.get("audio_codec", "aac"))]

    return " ".join(cmd + [out])
