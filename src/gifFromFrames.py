import argparse
import os

import pandas as pd

from gifGenerator import GifGenerator


def gifFromFrames():
    ap = argparse.ArgumentParser()
    ap.add_argument('path', type=str, help='path to folder with images')
    ap.add_argument('filename', type=str, help='file name to save the gif')
    ap.add_argument('--crop', type=int, help='area to crop (left, top, right, down)', nargs=4)
    ap.add_argument('--resize', type=int, help='desired image size', nargs=2)
    ap.add_argument('--duration', type=int, help='frame duration in ms', default=100)
    ap.add_argument('--csv', type=str, help='path to csv file')
    args = ap.parse_args()

    cdir = os.getcwd()

    gg = GifGenerator()
    gg.loadImages(args.path)
    if args.crop is not None:
        gg.cropImages(args.crop)  # left, top, right, down
    if args.resize is not None:
        gg.resizeImages(args.resize)
    if args.csv is not None:
        try:
            df = pd.read_csv(cdir + '\\' + args.csv)
        except:
            df = pd.read_csv(args.csv)
        text_data = [tuple(x) for x in df.to_records(index=False)]
        gg.addText(text_data)
    gg.generate(args.filename, args.duration)


if __name__ == "__main__":
    gifFromFrames()
