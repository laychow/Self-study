
import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullet_number:	
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_q:
		sys.exit()


def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False	
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False



def check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens):
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y=pygame.mouse.get_pos()
				check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,aliens,ship,bullets)
			elif event.type==pygame.KEYDOWN:
				check_keydown_events(event,ai_settings,screen,ship,bullets)
			elif event.type==pygame.KEYUP:
				check_keyup_events(event,ship)
def check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,aliens,ship,bullets):
	if play_button.rect.collidepoint(mouse_x,mouse_y) and (stats.game_active==False):
		stats.reset_stats()
		stats.game_active=True
		aliens.empty()
		bullets.empty()
		ai_settings.initialize_dynamic_setting()
		create_fleet(ai_settings,screen,aliens,ship)
		ship.center_ship()
		pygame.mouse.set_visible(False)
def update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button,scoreboard):
	screen.fill(ai_settings.bg_color)		
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	aliens.draw(screen)
	if stats.game_active==False:
		play_button.draw_button()
	scoreboard.prep_score()
	scoreboard.prep_level()
	scoreboard.prep_ships()
	scoreboard.show_score()
	#show screen_painted
	pygame.display.flip()
def update_bullets(ai_settings,bullets,ship,aliens,screen,scoreboard,stats):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<ship.screen_rect.top:
			bullets.remove(bullet)
	#check shoot		
	check_collision(ai_settings,bullets,ship,aliens,screen,scoreboard,stats)

def check_collision(ai_settings,bullets,ship,aliens,screen,scoreboard,stats):	
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for aliens in collisions.values():
			stats.score+=ai_settings.alien_points*len(aliens)
			scoreboard.prep_score()
		check_high_score(stats,scoreboard)
	if len(aliens)==0:
		bullets.empty()
		create_fleet(ai_settings,screen,aliens,ship)
		ai_settings.increase_speed()
		stats.level+=1
		scoreboard.prep_level()

def get_number_aliens_x(ai_settings,alien_width):
	
	avaliable_space_x=ai_settings.screen_width-2*alien_width
	number_aliens_x=int(avaliable_space_x/(2*alien_width))
	return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)
		
def create_fleet(ai_settings,screen,aliens,ship):
	alien=Alien(ai_settings,screen)
	number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_aliens_y=get_number_rows(ai_settings,ship.rect.height,ship.rect.width)
	for row_number in range(number_aliens_y):
		for alien_number in range(number_aliens_x):
			creat_alien(ai_settings,screen,aliens,alien_number,row_number)
	
def get_number_rows(ai_settings,ship_height,alien_height):
	avaliable_space_y=ai_settings.screen_height-alien_height*3-ship_height
	number_rows=int(avaliable_space_y/(2*alien_height))
	return number_rows

def update_aliens(ai_settings,aliens,ship,stats,bullets,screen,scoreboard):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,bullets,ship,aliens,screen,scoreboard)
	check_aliens_bottom(ai_settings,stats,bullets,ship,aliens,screen,scoreboard)	
	
def check_fleet_edges(ai_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
		
def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y+=ai_settings.fleet_drop_speed 
	
	ai_settings.fleet_direction*=-1


def ship_hit(ai_settings,stats,bullets,ship,aliens,screen,scoreboard):
	stats.ships_left-=1
	if stats.ships_left>0:
		aliens.empty()
		bullets.empty()
		scoreboard.prep_ships()
		ai_settings.initialize_dynamic_setting()
		create_fleet(ai_settings,screen,aliens,ship)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active=False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,bullets,ship,aliens,screen,scoreboard):
	screen_rect=screen.get_rect()
	
	for alien in aliens.sprites():
		if alien.rect.bottom>=screen_rect.bottom:
			ship_hit(ai_settings,stats,bullets,ship,aliens,screen,scoreboard)
			break
	
def check_high_score(stats,scoreboard):
	if stats.score>stats.high_score:
		stats.high_score=stats.score
		scoreboard.prep_high_score()
