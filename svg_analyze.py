from __future__ import division  # we need floating division
import json
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path
import pygame

""" demo of using a great python module svg.path by Lennart Regebro
    see site: https://pypi.org/project/svg.path/
    to draw svg in pygame
"""

from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path

svgpath = "M55.6 78.4h10.1c1.3-.3 2.1-.8 2.5-1.5l1.8-6.1H57.9l-2.3 7.6zm3.6-2.5l.8-2.7c0-.1.1-.1.2-.2l.3-.2c.1-.1.2-.1.3-.1h5c.2 0 .3.1.4.2l.2.2c.1.1.1.2.1.3l-.9 2.6c0 .1-.1.1-.1.2-.1.1-.3.2-.5.3-.1 0-.2.1-.3.1h-4.9c-.2 0-.3-.1-.4-.2l-.2-.2v-.3z" "M71.4 66.1c-.3-1.1-.4-2.1-.5-2.9v-.6h-8.4c-.2.3-.9 1.1-.9 1-2.2 2.9-3.2 3.3-3.9 3.1-.2-.1-.4-.2-.3-.4l1.1-3.7h-8.2l-4.9 15.8h6.1c1.2 0 2.3-.7 2.5-1.3l2.5-8.4c0-.1.1-.1.2-.2l.2-.1c.1-.1.2-.1.3-.1h.8c.2.1.3.1.4.3.1.2 0 .5-.1.6 0 .1 0 .1-.1.1h11.9c.1-.6.2-.9.5-1 .1-.1.3-.1.5-.1h.4l.5-1.7c-.4.1-.6-.2-.6-.4zm-16.6-1.6L51 76.8v.1c-.1.2-.3.3-.6.4H49.8c-.2 0-.3-.1-.4-.2l-.2-.1c-.1-.1-.1-.2-.1-.3L53 64.4c0-.1.1-.1.2-.2l.2-.1c.1-.1.2-.1.3-.1h.5c.2 0 .3.1.4.1l.2.1v.3zM68 67.6c-.1.1-.2.1-.4.1h-5c-.2 0-.3-.1-.4-.2-.1-.1-.1-.3 0-.4l1.2-1.4c.9-1.3 1.2-1.4 1.5-1.4H67c.2 0 .4.1.5.3l.6 2.6c0 .2-.1.3-.1.4zM78.9 74.9c0-.1 0-.1.1-.2l2.5-2.3 1.6-5.8c0-.1.1-.2.2-.2h.1c.1-.1.3-.2.6-.3l.5-1.7c-.3-.1-.4-.3-.5-.4v-.2l.3-1.2h-2.8L81 64c0 .1-.1.2-.2.2l-.3.2c-.1.1-.2.1-.3.1h-.5c-.1 0-.3-.1-.4-.1l-.2-.2c-.1-.1-.2-.2-.1-.3l.3-1.2h-2.8l-.4 1.3c0 .1-.1.2-.2.2l-.3.1c-.1 0-.2.1-.3.1H75l-.5 1.7c.4.1.7.2.7.6v.1l-1.6 5.7v.2l1.4 2.2c0 .1.1.2 0 .2v.1c0 .1-.1.1-.1.2-1.8 1.5-2.4 1.7-2.9 1.6-.1 0-.3 0-.4-.1h-.2l-.5 1.6H74c.8-.2 1.4-.6 1.9-1.1.1-.1.2-.1.4-.1h.1c.2 0 .4.1.4.2.4.6.9.9 1.4 1h2.7l.4-1.6c-1.1-.1-1.4-.2-1.6-.3-.1-.1-.1-.1-.1-.2l-.7-1.1c0-.1-.1-.1 0-.2v-.2zm-.2-2.9s0 .1 0 0c-.2.3-.4.5-.7.7-.1 0-.2.1-.3.1h-.2c-.1 0-.2 0-.3-.1-.3-.2-.4-.4-.5-.7v-.1l1.4-5.2c0-.1.1-.2.2-.2l.3-.2c.1-.1.2-.1.3-.1h.5c.2 0 .3.1.4.1l.2.2c.1.1.1.2.1.3L78.7 72zM97.8 68.3v-.1l1.4-5.5H86.6l-1.5 5.7c0 .1-.1.1-.1.2-.2.2-.4.3-.7.4l-.5 1.8c.3.1.4.3.5.4 0 .1.1.1 0 .2L82.8 77h8.7c.2 0 .3 0 .6.2.1.1.1.2.1.3 0 .1-.1.3-.3.3H90.5l-.1.9c4.3.1 3.9-.1 4.1-.1l.1-.1c.7-.3.9-.5.9-1.1v-.1c.1-.4.5-.2.9-.3l.4-1.7c-.3-.1-.6-.2-.6-.5v-.1l.9-3.3c0-.1.1-.2.2-.2l.2-.1c.1 0 .2-.1.2-.1h.3l.5-1.9c-.5-.4-.7-.6-.7-.8zm-4.6 6.4c0 .2-.3.3-.5.3h-.3c-.2 0-.8-.1-.9-.1-.1-.1-.1-.2-.1-.2v-2.2-.4h-2.2l-.1 2.8c0 .2-.2.4-.5.4h-1.7c-.2 0-.3-.1-.4-.1l-.1-.1c-.1-.1-.1-.2-.1-.3l.9-3.5c0-.1.1-.2.2-.2l.3-.2c.1-.1.2-.1.3-.1h5.5c.2 0 .3.1.4.2h.1c.1.1.1.2.1.3l-.9 3.4zm1.7-6.4c0 .1-.1.2-.2.2l-.2.2c-.1.1-.2.1-.3.1H94c-.2 0-.8-.1-.9-.1l-.1-.1c-.1-.1-.1-.1-.1-.2V66h-2c0 1.9 0 2.5-.1 2.7 0 .2-.3.3-.5.3h-1.8c-.2 0-.3-.1-.4-.1-.1-.1-.1-.2-.1-.3l.9-3.5c0-.1.1-.2.2-.2l.3-.2c.1 0 .2-.1.3-.1h5.5c.1 0 .3 0 .4.1l.2.2c.1.1.2.2.1.3l-1 3.1z" "M120.3 65.5l.2-.1c.1 0 .2-.1.3-.1h4.2l.5-1.8H121.1c-.3-.1-.6-.4-.4-.7v-.1h-3c-.1.5-.2.7-.5.9-.1.1-.3.1-.4.1h-4.4l-.5 1.8h4.2c.1 0 .3 0 .4.1l.2.1c.1.1.2.2.1.3l-.3 1.1c0 .1-.1.2-.2.2l-.2.1c-.1.1-.2.1-.3.1h-4.4l-.5 1.8h7.7c.1 0 .3 0 .4.1l.2.1c.1.1.2.2.1.3l-.2.7c0 .1-.1.2-.2.2l-.2.1c-.1 0-.2.1-.3.1H110l-.5 1.9h8.2c.2 0 .3.1.4.1l.2.2c.1.1.1.2.1.3l-.7 2.8c0 .2-.2.5-1 .6H115.3h-.1c-.2 0-.4-.1-.5-.2-.2-.2-.1-.5 0-.7.1-.1.1-.2.1-.3h-.1c-.4 0-1.2 0-1.3-.9 0-.2 0-.3-.1-.4h-4.1c.1.2.2.6.2.6.3 1.1.7 1.7 1.4 2 .5.3 1.2.3 2 .2.6-.1 1 0 1.2.2.4.3.1.8-.1 1 0 .1 0 .1-.1.1h4.6c1.4-.3 1.7-.8 1.9-1.3l1-4s0-.1.1-.1c.3-.3.7-.4 1.2-.3h-.1c.2 0 .7.1.8.1l.5-1.9c-.6 0-1.4-.1-1.6-.3-.1-.1-.1-.2-.1-.3l.2-.7c0-.1.1-.1.1-.2.4-.3.7-.3.9-.2.2 0 .6.1.7.1l.5-1.8h-4.4c-.2 0-.3 0-.4-.1l-.2-.1c-.1-.1-.1-.2-.1-.3l.3-1.1c.4-.2.5-.3.6-.4zM109.9 66.4l.4-1.7c-.6 0-1 0-1.2-.2-.1-.1-.1-.2-.1-.3l.4-1.5h-3.1l-.4 1.6c0 .1-.1.2-.2.2l-.2.1c-.1 0-.2.1-.3.1h-.7c-.1 0-.3 0-.4-.1-.1-.1-.1-.2-.1-.3l.1-.3c0-.1 0-.1.1-.1l.2-.5h-1.6v.2c-.7 2.2-1.1 3-1.6 3.2v1.7h.2c.7-.1 1.3-.5 1.6-1.2.1-.4.2-.7.4-.8.1-.1.3-.1.5-.1h-.1.7c.1 0 .3 0 .4.1l.2.1c.1.1.1.2.1.3l-.6 2.2s0 .1-.1.1c-2.5 3-3.9 3.3-4.5 3.6l-.5 2.2h1.3c.6-.1 1-.3 1.2-.5.1-.1.6-.2.8-.1.2.1.3.2.3.4l-1 3.6h3.1l2-7.6v-.1c.1-.1.4-.5 1.2-.3h-.1.4l.4-1.7c-.6 0-1 0-1.2-.2-.1-.1-.1-.2-.1-.4l.4-1.4v-.1c.1-.1.4-.4 1.2-.3h-.1c.3.1.5.1.6.1z" "M43.6 76.7H27.3h-.2c-.2 0-.3 0-.4-.1-.2-.1-.6-.6-.5-1.3 0-.1 0-.3.2-.6 0 0 .1-.2.3-.2.1-.1.2-.1.3-.1H40.8s.1 0 .2-.1c1.8-.3 2.8-.9 3.1-1.9l2.9-9.7H26.2c-.5 1.5-3.9 12.3-3.9 12.2l-.6 1.5c.2 1.4 1 2 2.4 2.1h17.4s.8.1 1.5-.5c.6-.4.6-1.3.6-1.3zm-8-4.9l2.2-6.6c0-.1.1-.1.2-.2l.3-.2c.1 0 .2-.1.3-.1h3.1c.1 0 .3 0 .4.1l.2.2c.1.1.1.2.1.3l-1.9 6c-.1.4-.5.8-1.5 1.1h.4-2.8c-.1 0-.2 0-.3-.1l-.2-.2c-.5-.1-.5-.2-.5-.3zm-8.3 0l2.2-6.6c0-.1.1-.1.2-.2l.3-.2c.1 0 .2-.1.3-.1h2.9c.1 0 .3 0 .4.1l.2.2c.1.1.1.2.1.3l-2.2 6.6c0 .1-.1.1-.2.2l-.3.2c-.1 0-.2.1-.3.1H28c-.1 0-.2 0-.3-.1l-.2-.2c-.2-.1-.2-.2-.2-.3z M92.5 40.1l-.3 3.6c-.5.2-1.2 1.9-1.2 1.9l-5.5 6.8c1.9.3 3.2-.2 3.2-.2-1-1.9 1.5-3.2 1.5-3.2l2.7-.2c3.3-1.5 4.7-4.5 4.7-4.5.7-2.4.2-3.9.1-4.1l-5.2-.1zM113 35.7l-2.2-1.8-4.4.5c-.4.5-1.9 1.2-1.9 1.2-.7.5-.8-.6-.8-.6l-.9-.8-.6 3.7 3.2-.1 1.1-1.6 1.5-.8c.2-.1.7-.5 1-.4h1.9l.1 1.6.8-.9-.2-.1c.7.3.7 1.9.7 1.9l.7-1.8zM100.5 33.9l-2.2-1.3s-1.8-1.9-1.7-3.4l5.8-12.7.2-.1h.3l.5.3c.3.4.7 1.1 1 1.3.2.6.4 1.3.7 1.7 0 0-.5-1.8-.2-2.9-1.1-.5-1.7-2.6-1.7-2.6l-.9.4c-.4 0-.8-.1-1-.1-.6-.3-1.3-.6-1.6-.7-2.6-1.3-10.4-5-20.4-6.7C66.9 4.9 36 4.6 28.7 5.7c-7.3 1.1-4.4.9-4.4.9S51.9 9.9 65 19.4l28.7 17.2 6.8-2.7z" "M108 62.2c-.2-.4-.4-.8-.5-1.2h-.2c.2.4.4.8.7 1.2zM84.5 80.1h-7l.2.2c6.4 7.6 17.6 8.6 25.2 2.2l.2-.2c-5.8 3.6-13.4 2.7-18.6-2.2zM84.5 57c6.3-5.3 16-4.2 21.6 2.4.4.5.8 1 1.1 1.5h.2c-.6-1.3-1.4-2.5-2.4-3.7-4.7-5.6-12.1-7.6-18.7-5.7.5-1 1.3-1.9 1.3-1.9.8 0 .4-.2 1.8-.8.3-.5 2.6-.8 2.6-.8 1.6-.3 3.1-1.6 4.1-3.3.9-1.6.6-3.2.6-3.2l4.8-3.5c1.6-.1 1.7-.2 1.7-.2l1.2.2 5.1-1.9-.2 1.6 1.3-1c.1.1.4.4.2 1.2-.1.4.9-.7.9-.7l.9-1.1-2.6-1.8-4.2 1c-.3-.2-1.3.9-.2-.2.5-.5 1.3-2.6 1.3-2.6l.1-2.6 1.4-1.8.7-.3c.3.1.7.2 1.1.2.3.1.6.2.8.4l.3.2 1-.8h-.6-.4v-.1l-.3.1c-.5-.3-1.2-1.2-1.2-1.2l.8-.9h1.1c.1 0 .4 0 .5.1l.4.5.1-.3c.6.1.5.6.5.6l.2-.3s-.4-1.8-1-1.5c-.4.1-1.5-.3-2.4-.7l-1.2-.6-4 .1c-.4 0-2.6 0-4 .5 0 0 2.4-.2 5.2.6.1.1.2.1.3.1-.8.3-5.7 1.2-6.4 1.2-1 0 3.3.4 5.7.2l-1.6 1.5c-.2.1-2.7 1.3-3.1 1.6-.6.3 1.6-.2 1.6-.2-.5.3-1.9.8-2.5.9 0 0 .5.6 1.1.7-.9.2-2.3.6-2.7.5 0 0 .7.2 1.2.4-1.5.2-2.6.6-2.6.6l1.3.7-1.3.9c-2.8-1.7-2.7-3.8-2.7-3.8l4.5-11.8c.2-.1.3-.1.5-.2l.6.4c.1.2.2.3.4.5.3 1.8 2.1 3.5 1.6 2.8-.3-.4-.5-1.3-.7-2.1l-.2-1.8-2.1-2.3-1.5.6s-18.9-4.9-21.2-4.8c-3.6-1.1-50.8 3.8-50.8 3.8l-6 1.5c2.3-.3 5.2-.5 8.4-.5 1.9.1 4.2.3 6.7.5l7.7 1.3c30.5 5.3 11.7 18.2 11.7 18.2l-1.4 1.2c10.3-6.2 18.1-6.1 18.1-6.1 8.1.5 2.5 11.2 2.5 11.2 6.4-6.5 13-7.4 16.7-7.3.9.1 1.8.4 2.5.8-.2.2-1.5 1.6-1.7 1.8L84.7 39c-.4.4 3.7 0 3.3.4-.6.5.2.2-.4.6-.5.3-4.6.6-5.1.9-.5.3 2.9.5 2.4.8-.5.3-.4.2-.3.2 0 0-.1 0-.4.1-.5.2-6.2.3-6.7.4-.5.1 2.8 1 2.3 1.1-5.2 1.2-5.7 2.8-13 .6-.6 0-3.6-2.7-4.1-2.7-.5 0 1.6 2.5 1.1 2.5-.4 0-5.1-2.3-5.4-2.3-1.2-.1 2.5 2 2.5 2-.8-.2-1.2-.4-2-.5-.6-.1-5-1.7-5.5-1.7-.3 0 2.6 1.6 2.3 1.6-1.1-.1-1.8-.2-2.7-.2-.6 0-5-1.1-5.6-1.1-.6 0 2.6 1.3 2.1 1.3-2.6.3-4.2.8-4.2.8-3.5 1.3-.8.8-.8.8 11.8-2 15.9.9 21.3 2.6C78 51 90.4 43.4 90.4 43.4l-.8 1.6c.2 1.6-1.5 3.1-1.5 3.1l-1.1.2-.8-.6-1 1-.2 1.6c-.1.2-.3 1.1-.5 2-1.6.7-3.2 1.6-4.6 2.8-2 1.7-3.5 3.7-4.6 5.9h5.9c.8-1.5 1.9-2.9 3.3-4zm25.6-31.9l-.1.2-1.1.2-1.1-.9 2.3.5z M8.6 93.3h1.1v-.9H11v-1H9.7v-.8H8.6v.8H6v1h2.6zM11.7 94.3h4.5v-.9H6.1v.9h4.5v2.9H5.9v1h4.7v.8H6.4v.9h4.2v1.6h1.1v-1.6h4.2V99h-4.2v-.8h4.8v-1h-4.8z M14.5 97.1v-.9h1.7v-1h-1.7v-.8h-1v.8h-1.4v1h1.4v.9zM7.8 94.4v.9H6.2v.9h1.6v.9h1v-.9h1.5v-.9H8.8v-.9zM12.6 93.3h1.1v-.9h2.7v-1h-2.7v-.8h-1.1v.8h-1.3v1h1.3zM25.8 92.4c.1-.6.1-1.2.1-1.6v-.2h-1.2v.3c0 2-.1 7.3-4.8 9.6l-.2.1.1.1c.3.2.5.4.7.7v.1h.1c2.3-1.2 3.8-3.3 4.6-6.2.9 3 2.5 5.1 4.7 6.1h.1v-.1c.1-.2.4-.5.6-.7l.1-.1-.1-.1c-2.5-1.2-4.3-4-4.8-8zM42.7 99.5c.8-.8 1.3-1.7 1.7-2.7v-.1l-.6-.3h-4.4v.9h.6v.1c.3.8.7 1.5 1.3 2-.6.4-1.3.8-2 1V96h5.5v-1H34.3v1h1v3.7c-.4 0-.7.1-1 .1h-.1l.1 1h.1c.6-.1 1.3-.1 2-.2.6-.1 1.2-.1 1.8-.2v1.2h1v-.6c.1.1.2.3.3.5v.1h.1c.8-.3 1.6-.7 2.3-1.2.7.5 1.5 1 2.4 1.2h.1v-.1c.1-.2.3-.5.5-.7l.1-.1h-.2c-.8-.4-1.5-.7-2.1-1.2zm.3-2.1c-.3.5-.6 1-1.1 1.5-.4-.5-.8-1-1-1.5H43zm-6.8-.9V96h1.9v.6h-1.9zm0 1.4v-.6h1.9v.6h-1.9zm0 1.6v-.7h1.9v.5c-.4 0-.8.1-1.3.1-.1.1-.3.1-.6.1zM36.6 91.9h5.8v2.9h1.1V91h-7.9v3.8h1z M36.9 93.7h5.2v.8h-5.2zM36.9 92.4h5.2v.8h-5.2zM54.5 95h4.4v-1.1h-4.8c.1-1.2.2-2.3.2-3.2v-.2h-1.1v.4c0 .8 0 1.8-.2 2.9h-4.5V95h4.3c-.6 2.7-2.1 4.5-4.5 5.5l-.2.1.1.1c.2.2.5.5.6.7v.1h.1c2.3-1.1 3.9-2.9 4.6-5.5 1 2.7 2.6 4.6 4.6 5.5h.1v-.1c.1-.2.4-.6.6-.8l.1-.1-.1-.1c-2.3-1-3.6-3.5-4.3-5.4zM64.2 95.9c.7-.1 1.4-.3 2.2-.4l.6-.1v-.7h-.1c-.9.1-2 .3-2.8.4H64v-1.8h3.4V96h1v-2.7H71l-.1.1c-.6.2-1.4.5-2 .6h-.1l.4.6h.1c.3-.1 1.5-.3 2.3-.7l.1-.1-.5-.6h.7v1.9H73v-2.7h-4.6v-.5h4V91h-9v.8h4v.5h-4.5V95h1l.3.9zM72.5 99l-.1-.1v.2c-.1 1.2-.2 1.3-.7 1.3h-2.6c-.7 0-.8-.1-.8-.4v-.3h3.6V96h-8.1v4.3h1v-.6h2.4v.3c0 1.1.5 1.3 1.8 1.3h2.7c1.2 0 1.5-.5 1.6-1.9v-.1h-.1c-.2 0-.5-.1-.7-.3zm-5.2-.7v.6h-2.4v-.6h2.4zm0-1.4v.6h-2.4v-.6h2.4zm1 .6v-.6h2.6v.6h-2.6zm0 1.4v-.6h2.6v.6h-2.6z M64.5 93.2l-.4.6h.1c.8.2 1.8.4 2.2.7h.1l.3-.7h-.1c-.4-.2-1.4-.4-2.2-.6zM68.9 94.6l-.3.7h.1c.9.1 2.1.4 2.7.6h.1l.3-.8h-.1c-.6-.2-1.8-.4-2.8-.5zM81.1 91.4h5.7v1h-5.7zM86.8 98.8l-.2-.2v.2c0 1.3-.1 1.5-.2 1.5h-.8c-.2 0-.2 0-.2-.3v-4.3h2v-1h-6.8v1h1.6c-.1 2.4-.4 4-2.7 4.9l-.2.1.1.1c.2.1.4.4.5.6v.1h.1c2.5-1 3.1-2.7 3.2-5.7h1.1v4.3c0 1 .3 1.3 1.1 1.3h1c.9 0 1.1-.7 1.1-2.1v-.1h-.1c-.1-.1-.4-.3-.6-.4z M81 98.9l-.1-1h-.1c-.3.1-.7.2-1 .3-.2 0-.4.1-.5.1v-2.5h1.3v-1h-1.3v-2.4h1.5v-1h-4.1v1h1.5v2.4h-1.4v1h1.4v2.7c-.3.1-.6.1-.8.2-.3.1-.6.1-.8.2h-.1l.2 1h.1c.8-.2 1.8-.5 2.9-.8l1.3-.2zM98.9 95.2h2.5v-1h-2.5v-3.7h-1.1v3.7h-2.5v1h2.5v4.7h-3v1.1h6.8v-1.1h-2.7z M95.5 97l-.3-.3c-.3-.4-.9-.9-1.3-1.3.6-.8 1.1-1.6 1.4-2.4v-.1l-.6-.4h-1.2l.6-.4V92c-.2-.4-.7-1-1.2-1.5l-.1-.1-.7.6.1.1c.4.4.8 1 1 1.5h-2.3v1h3c-.7 1.3-2 2.7-3.3 3.4h-.1l.1.1c.1.1.3.6.4.8v.1l.1-.1c.5-.3 1-.7 1.5-1.2v4.6h1.1v-4.9c.4.4.8.9 1 1.2l.1.1.7-.7zM113.6 96.2h1.8v-1h-1.8v-1.4h2v-1h-1.2c.3-.5.6-1.3.9-1.9v-.1l-1-.3v.1c-.2.6-.6 1.5-.8 2l-.1.1.3.1h-1.6l.3-.1v-.1c-.1-.5-.5-1.3-.9-1.9v-.1l-.9.3.1.1c.3.6.6 1.3.8 1.8h-.9v.2h-.6v-1.9h-4.4v1h1.4c0 .2 0 .5-.1.7v.2H105v1h1.8c-.1.3-.1.7-.2 1h-1.1v1h.8c-.4 1.1-.8 2-1.5 2.6l-.1.1.1.1c.2.2.5.5.6.7l.1.1.1-.1c.2-.2.4-.5.6-.8v2.9h1v-.6h3v-3.9H107c.1-.3.2-.7.3-1h2.6V94h.7v-.2h1.8v1.4h-1.8v1h1.8v1.5h-2.2v1h2.2v2.7h1v-2.7h2.3v-1h-2.3v-1.5zM109 94v1h-1.4c.1-.3.1-.6.2-1h1.2zm0-1.9v1h-1.1c0-.3.1-.6.1-1h1zm.1 5.8v2h-1.9v-2h1.9zM119.6 98.1c-.1 1.2-.3 2.1-.5 2.7v.1h.1c.2.1.5.2.6.2l.1.1v-.1c.2-.7.5-1.8.6-2.8v-.1l-.9-.1zM121.7 98.1l-.8.1v.1c.1.6.3 1.7.3 2.5v.1l.9-.2v-.1c-.2-.8-.3-1.8-.4-2.5z M123.5 97.1l-.7-2.1v-.1l-.8.3.2.4c.1.2.2.4.3.7l-1.6.2c.9-1.1 1.7-2.4 2.4-3.7v-.1l-.9-.5v.1c-.2.5-.5 1.1-.8 1.6l-1 .1c.6-.8 1.2-1.9 1.6-3v-.1l-.9-.4v.1c-.5 1.3-1.2 2.6-1.5 2.9-.2.4-.4.6-.6.6h-.1v.1c.1.2.2.6.2.7v.1l.1-.1c.1-.1.4-.1 1.4-.2-.4.6-.7 1-.8 1.2-.3.4-.6.7-.8.7h-.1l.1.1c.1.2.2.6.2.7v.1l.1-.1c.2-.1.6-.2 3.1-.6v.2c0 .1.1.2.1.3v.1l-.7.2v.1c.2.6.5 1.6.7 2.3v.1l.8-.3v1.4h1v-9.4h4.2v8.3c0 .1 0 .1-.1.1h-1.3l.1.2c.1.2.2.5.2.7v.1h.1c.7 0 1.2 0 1.5-.2.4-.2.5-.5.5-.9v-9.3h-6.2v6.3zm0 2.9c-.1-.7-.4-1.6-.7-2.3v-.1l.7-.3v2.7z M128.5 99.1l.1-.1v-.4-.4h-.1c-.1 0-.4.1-.7.1h-1.4c-.2 0-.2 0-.2-.3v-1h2.4v-.9h-1.4.1V96c-.1-.2-.3-.6-.4-.9h1.9v-.9h-1c.2-.5.4-1 .5-1.6v-.1l-.8-.2v.1c-.1.5-.3 1.3-.5 1.9h-.8l.4-.1v-.1c-.1-.5-.3-1.2-.6-1.7v-.1l-.7.3.1.1c.3.5.5 1.1.6 1.6h-1v.9h1.4l-.1.1.1.1c.2.3.3.6.4.9h-1.5v.7h.4v1c0 .8.2 1.2 1 1.2h1.5c-.1 0 .2 0 .3-.1zM134.5 98.6l.9-.2v-.1c-.1-1.1-.3-2.7-.6-4.2V94l-.9.2v.1c.3 1.4.5 3.1.6 4.2v.1zM144.1 94v-1h-2.9v-2.4h-1.1v5.6h-1.9v5.3h1v-.5h3.3v.5h1.1v-5.3h-2.5V94h3zm-1.5 3.1v2.7h-3.3v-2.7h3.3zM136.6 92.5c-.2-.6-.5-1.3-.9-1.9v-.1l-.9.3.1.1c.3.5.6 1.3.8 1.7h-2.1v1h4.7v-1H136l.6-.1z M136.8 98.4c.3-1.2.6-2.9.8-4.2v-.1l-1-.2v.1c-.1 1.4-.4 3.4-.7 4.6-.7.2-1.3.3-1.9.4-.2 0-.4.1-.6.1h-.1l.3 1.1h.1l4.4-1.1h.1l-.1-1-1.3.3z"

path = parse_path(svgpath)
def output_picture_json():
    global jsDict
    print("Saving Json Data...")
    with open("picture.json","w",encoding="utf-8") as f:
        json.dump(jsDict, f)
    print("Data Saved !")
    return jsDict
# svg.path point method returns a complex number p, p.real and p.imag can pull the x, and y
# # on 0.0 to 1.0 along path, represent percent of distance along path
n = 1000  # number of line segments to draw
magnification=5
# pts = []
# for i in range(0,n+1):
#     f = i/n  # will go from 0.0 to 1.0
#     complex_point = path.point(f)  # path.point(t) returns point at 0.0 <= f <= 1.0
#     pts.append((complex_point.real, complex_point.imag))

# list comprehension version or loop above
jsDict = {"drawing":[]}
pts=[]
for i in range(n):
    jsDict["drawing"].append({"x":800-path.point(i/n).real*magnification-200 , "y":600-path.point(i/n).imag*magnification+100})
    pts.append((path.point(i/n).real*magnification,path.point(i/n).imag*magnification))
pygame.init()                                  # init pygame
surface = pygame.display.set_mode((800,600))   # get surface to draw on
surface.fill(pygame.Color('white'))            # set background to white

pygame.draw.aalines( surface,pygame.Color('blue'), False, pts)  # False is no closing
pygame.display.update() # copy surface to display

while True:  # loop to wait till window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            output_picture_json()
            exit()