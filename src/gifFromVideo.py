import argparse

from gifGenerator import GifGenerator


def gifFromVideo():
    ap = argparse.ArgumentParser()
    ap.add_argument('path', type=str, help='path to input video (can be relative)')
    ap.add_argument('filename', type=str, help='file name to save the gif')
    ap.add_argument('--fps', type=int, help='output framerate')
    ap.add_argument('--width', type=int, help='output width')
    args = ap.parse_args()
    if args.fps is None and args.width is None:
        GifGenerator.generateFromVideo(args.path, args.filename)
    elif args.fps is None:
        GifGenerator.generateFromVideo(args.path, args.filename, width=args.width)
    elif args.width is None:
        GifGenerator.generateFromVideo(args.path, args.filename, fps=args.fps)
    else:
        GifGenerator.generateFromVideo(args.path, args.filename, width=args.width, fps=args.fps)


if __name__ == "__main__":
    gifFromVideo()
