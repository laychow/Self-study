

import pygame
from pygame.sprite import Group

from settings import Settings 
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
import game_functions as gf    #other name 





def run_game():
	pygame.init();
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))     
	pygame.display.set_caption("Alien Invasion")   #title
	
	ship=Ship(ai_settings,screen)
	stats=GameStats(ai_settings)
	play_button=Button(ai_settings,screen,"Play")
	scoreboard=ScoreBoard(ai_settings,screen,stats)
	aliens=Group()
	bullets=Group()
	gf.create_fleet(ai_settings,screen,aliens,ship)
	ship.blitme()
	while True:
		gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens)
		if stats.game_active:
			ship.update(ai_settings.ship_speed_factor)
			gf.update_bullets(ai_settings,bullets,ship,aliens,screen,scoreboard,stats)
			gf.update_aliens(ai_settings,aliens,ship,stats,bullets,screen,scoreboard)
		
		gf.update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button,scoreboard)
		
		
		
run_game()
