#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/11 下午7:40
# @Author : Sui Chen

from PIL import Image, ImageDraw
from PIL import ImageFont


class GridDraw(object):
    size = 3000
    right_margin = 1000
    padding = 200
    line_width = 10
    font_size = 70
    point_portion = 0.2
    max_w_h = size - 2 * padding
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    yellow = (255, 246, 0)

    def __init__(self, m, n, d, points, file_name):
        if m > n:
            h = float(self.max_w_h)
            w = (float(n - 1) / (m - 1)) * self.max_w_h
        else:
            w = float(self.max_w_h)
            h = (float(m - 1) / (n - 1)) * self.max_w_h
        im = Image.new('RGB', (int(w + 2 * self.padding + self.right_margin), int(h + 2 * self.padding)), color=self.black)
        self.font = ImageFont.truetype("SimSun.ttf", self.font_size)
        self.draw = ImageDraw.Draw(im)
        self.x_gap, self.y_gap = self.draw_grid(m, n, w, h)
        self.draw_points(points)
        next_x, next_y = self.draw_answer(d)
        self.draw_points_position(points, next_x, next_y)
        del self.draw
        im.save(file_name)
        im.show()

    def draw_points_position(self, points, begin_x, begin_y):
        self.draw.text((begin_x, begin_y + self.font_size), text=u'城市坐标:', font=self.font, fill=self.white)
        x = begin_x + self.font_size
        y = begin_y + self.font_size * 2
        for index, point in enumerate(points):
            self.draw.text((x, y), text='%s:(%s, %s)' % (index+1, point[0]+1, point[1]+1), font=self.font, fill=self.white)
            y += self.font_size

    def draw_answer(self, d):
        y = self.padding
        x = self.size
        self.draw.text((x, y), text=u'最短路径长度:%s' % d, font=self.font, fill=self.white)
        return x, y + self.font_size

    def get_point_x_y(self, point):
        x = self.padding + point[1] * self.x_gap
        y = self.padding + point[0] * self.y_gap
        return x, y

    def draw_index(self, index, point, dir):
        dir = 2
        x, y = self.get_point_x_y(point)
        if dir & 1:
            hori_sign = -1
            hori_shift = - self.font_size
        else:
            hori_sign = 1
            hori_shift = 0
        if dir & 2:
            vert_sign = 1
            vert_shift = 0
        else:
            vert_sign = -1
            vert_shift = - self.font_size
        x += self.x_gap * self.point_portion * hori_sign * 0.8 + hori_shift
        y += self.y_gap * self.point_portion * vert_sign * 0.8 + vert_shift
        self.draw.text((x, y), text=str(index+1), fill=self.red, font=self.font)

    def translate_direction(self, point, other):
        # left, bottom 3
        # left, top 1
        # right, bottom, 2
        # right, top 0
        hori = int(point[0] > other[0])
        vert = int(point[1] < other[1])
        return (vert << 1) | hori

    def get_usable_direction(self, before, point, next):
        before_dir = self.translate_direction(point, before)
        next_dir = self.translate_direction(point, next)
        avail_dirs = [2, 0, 3, 1]
        for avail_dir in avail_dirs:
            if avail_dir != before_dir and avail_dir != next_dir:
                return avail_dir

    def draw_point(self, point):
        point_portion = self.point_portion
        x, y = self.get_point_x_y(point)
        self.draw.ellipse((x - point_portion * self.x_gap, y - point_portion * self.y_gap,
                           x + point_portion * self.x_gap,
                           y + point_portion * self.y_gap), self.red, self.red)

    def draw_line(self, point, next):
        x0, y0 = self.get_point_x_y(point)
        x1, y1 = self.get_point_x_y(next)
        self.draw.line((x0, y0, x1, y1), self.yellow, width=self.line_width)
        
    def draw_points(self, points):
        for index in range(len(points)):
            self.draw_point(points[index])
            avail_dir = self.get_usable_direction(points[index-1], points[index], points[(index+1) % len(points)])
            self.draw_index(index, points[index], avail_dir)
            self.draw_line(points[index-1], points[index])

    def draw_grid(self, m, n, w, h):
        draw = self.draw
        line_y = self.padding
        y_gap = float(h) / (m - 1)
        x_gap = float(w) / (n - 1)
        for i in range(m):
            text_width = len(str(i+1)) * self.font_size * 0.5 + x_gap * self.point_portion
            draw.line((self.padding, line_y, w + self.padding, line_y), fill=self.white, width=self.line_width)
            draw.text((self.padding - text_width, line_y - self.font_size / 2),
                      text=str(i+1), fill=self.white, font=self.font)
            line_y += y_gap
        line_x = self.padding
        for j in range(n):
            text_width = len(str(j + 1)) * self.font_size * 0.5
            draw.line((line_x, self.padding, line_x, h + self.padding), fill=self.white, width=self.line_width)
            draw.text((line_x - text_width / 2, self.padding - self.font_size - y_gap * self.point_portion),
                      text=str(j+1), fill=self.white, font=self.font)
            line_x += x_gap
        return x_gap, y_gap
    

test = GridDraw(10, 20, '5 cm', points=((0,0), (1,0), (5,0), (8,0)), file_name='test.png')