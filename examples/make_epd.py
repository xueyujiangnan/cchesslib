# -*- coding: utf-8 -*-

'''
Copyright (C) 2014  walker li <walker8088@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys, os
import shutil

sys.path.append('..')
from cchess import *

def load_board(root_path):
        games = []
        files = os.listdir(root_path)
        for file in files:
                game_info = {}
                ext = os.path.splitext(file)[1].lower()
                if ext != '.xqf':
                        continue
                file_name = os.path.join(root_path, file)
                #print file_name
                game = read_from_xqf(file_name)
               
                game.init_board.move_side = ChessSide.RED
                fen = game.init_board.to_fen()
                print file[:-4],fen
                game_info['name'] = file[:-4]
                game_info['fen'] = fen
                game_info['moves'] = game.dump_std_moves()
                #f.write("%s|%s\n" % (file[:-4].encode('utf-8'), fen))
                #game.print_init_board()
                #game.print_chinese_moves()
                max_len = 0
                for move in game.dump_std_moves():
                        if len(move) > max_len:
                                max_len = len(move)
                game_info['len'] = max_len                
                games.append(game_info)
        
        games.sort(key=lambda x: x['len'])
        return games
                
with open(u'适情雅趣360.epp', 'wb') as f:
        for game in load_board(u'..\\games\\残局谱\\适情雅趣360局'):
                f.write("%s|%s\n" % (game['name'].encode('utf-8'), game['fen']))

            