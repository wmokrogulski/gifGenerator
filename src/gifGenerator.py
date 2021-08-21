import os
import subprocess

from PIL import Image, ImageDraw, ImageFont

POSITION = (50, 90)  # %
TEXT_COLOR = (255, 255, 255)
TEXT_FONT = '../calm_down.otf'
TEXT_SIZE = 50
PATH_TO_FFMPEG = 'C:/ffmpeg/bin/ffmpeg.exe'


class GifGenerator:
    def __init__(self):
        self.frames = []
        # self.font = ImageFont.truetype(TEXT_FONT, TEXT_SIZE)
        self.font = ImageFont.truetype('arial.ttf', TEXT_SIZE)
        self.text_position = POSITION

    def setTextPosition(self, position):
        self.text_position = position

    def setFont(self, font_name, font_size):
        if not isinstance(font_size, int):
            font_size = TEXT_SIZE
        try:
            self.font = ImageFont.truetype(font_name, font_size)
        except:
            self.font = ImageFont.truetype(TEXT_FONT, font_size)

    def loadImage(self, path):
        return Image.open(path)

    def cropImages(self, rect):
        """
        crop frames
        :param rect: left, top, right, down
        """
        self.frames = [i.crop(rect) for i in self.frames]

    def resizeImages(self, size):
        """
        resize frames
        :param size: width,height
        """
        self.frames = [i.resize(size) for i in self.frames]

    def loadImages(self, path):
        os.chdir(path)
        for f in os.listdir():
            frame = self.loadImage(f)
            self.frames.append(frame)

    def addText(self, text_data):
        for text, start, end in text_data:
            if len(self.frames) > 0:
                if (0 <= start < len(self.frames)) and (start <= end < len(self.frames)):
                    for i in range(start, end + 1):
                        draw = ImageDraw.Draw(self.frames[i])
                        W, H = self.frames[i].size
                        W *= self.text_position[0] / 100
                        H *= self.text_position[1] / 100
                        w, h = draw.textsize(text, font=self.font)
                        w /= 2
                        h /= 2
                        draw.text((W - w, H - h), text, TEXT_COLOR, font=self.font)

    def generate(self, filename, duration_ms):
        if len(self.frames) > 0:
            frame_one = self.frames[0]
            try:
                frame_one.save(filename, format='GIF', append_images=self.frames, duration=duration_ms, save_all=True,
                               loop=0)
            except:
                msg = 'Error saving gif.'
            else:
                msg = 'Gif saved successfully.'
            print(msg)
            return msg

    @staticmethod
    def generateFromVideo(in_filename, out_filename='output.gif', fps=20, width=320):
        cmd = f'{PATH_TO_FFMPEG} -y -i {in_filename} ' \
              f'-vf "fps={fps},scale={width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" ' \
              f'-loop 0 {out_filename}'
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    gg = GifGenerator()
    gg.loadImages('D:\\Wawa\\Videos\\twisted')
    # gg.setFont('calm_down.otf', 50)
    gg.cropImages((74, 0, 854, 720))  # left, top, right, down
    gg.resizeImages((390, 360))
    text_data = [
        ('But', 30, 45),
        ('like', 50, 60),
        ('with', 70, 85),
        ('money?', 85, 100)
    ]
    gg.addText(text_data)
    gg.generate('test.gif', 50)
