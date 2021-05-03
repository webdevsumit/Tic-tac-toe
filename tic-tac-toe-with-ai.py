import pygame
import random
import joblib
import pandas as pd

try:
    data = pd.read_csv("data.csv",index_col=0)
except:
    data = pd.DataFrame({}, columns=["0","1","2","3","4","5","6","7","8","9"])
    

model = joblib.load("model.joblib")   

data2 = data.copy()



pygame.init()

#window_surface = pygame.SDL_GetWindowSurface()

size = width,height = 2150, 1000

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic tec toe')


font32 = pygame.font.SysFont(None,32)
font64 = pygame.font.SysFont(None,64)
font72 = pygame.font.SysFont(None,72)
font96 = pygame.font.SysFont(None,96)


def main_page_singalplayer():
    global data2
    global data
    player = 1
    
    player_1_score = 0
    player_2_score = 0
    
    rectArray = [
        [800,100,200,200,0],[1000,100,200,200,0],[1200,100,200,200,0],
        [800,300,200,200,0],[1000,300,200,200,0],[1200,300,200,200,0],
        [800,500,200,200,0],[1000,500,200,200,0],[1200,500,200,200,0]
    ]
    
    win_line_x1 = 0
    win_line_y1 = 0
    win_line_x2 = 0
    win_line_y2 = 0
    winning_line_color = (0,0,255)
    
    main_game = True
    while main_game:
        
        screen.fill((150,150,150))
        
        rect = pygame.draw.rect(screen,(255,255,255),(0,0,width,height),1)
        
            
        winning_line = pygame.draw.line(screen,winning_line_color,(win_line_x1,win_line_y1),(win_line_x2,win_line_y2),10)
        
        font_img = font72.render("Machine",True, (155,0,0))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width/4,height/2-100)
        screen.blit(font_img,font_img_rect)
        
        font_img = font72.render(str(player_1_score),True, (155,0,0))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width/4,height/2)
        screen.blit(font_img,font_img_rect)
        
        font_img = font72.render("You",True, (0,0,255))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width*3/4,height/2-100)
        screen.blit(font_img,font_img_rect)
        
        
        font_img = font72.render(str(player_2_score),True, (0,0,255))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width*3/4,height/2)
        screen.blit(font_img,font_img_rect)
        
        
        font_img = font72.render("back",True, (255,255,255))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (200,100)
        screen.blit(font_img,font_img_rect)
        back_btn_rect = font_img_rect
        back_btn_rect.width =200
        back_btn_rect.height =100
        back_btn_rect.center = (200,100)
        back_btn = pygame.draw.rect(screen,(255,255,255),back_btn_rect,10,20)
        
        if player == 2:
            pygame.draw.circle(screen,(0,0,255),(width*3/4,height/2-200),20)
        else:
            pygame.draw.circle(screen,(155,0,0),(width/4,height/2-200),20)
        
        for ind in range(0,3):
            if rectArray[ind][4] == 1 and rectArray[ind+3][4] == 1 and rectArray[ind+6][4] == 1 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+6][0]+100
                win_line_y2 = rectArray[ind+6][1]+100
                winning_line_color = (155,0,0)
                
                player_1_score += 1
                data2 = data.copy()
                for b in rectArray:
                    b[4] = 0
                    
            elif rectArray[ind][4] == 2 and rectArray[ind+3][4] == 2 and rectArray[ind+6][4] == 2 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+6][0]+100
                win_line_y2 = rectArray[ind+6][1]+100
                winning_line_color = (0,0,255)
                
                player_2_score += 1
                data = data2.copy()
                data.to_csv("data.csv")
                for b in rectArray:
                    b[4] = 0
                    
        for ind in range(0,7,3):
            if rectArray[ind][4] == 1 and rectArray[ind+1][4] == 1 and rectArray[ind+2][4] == 1 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+2][0]+100
                win_line_y2 = rectArray[ind+2][1]+100
                winning_line_color = (155,0,0)
                
                player_1_score += 1
                data2 = data.copy()
                for b in rectArray:
                    b[4] = 0
            elif rectArray[ind][4] == 2 and rectArray[ind+1][4] == 2 and rectArray[ind+2][4] == 2 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+2][0]+100
                win_line_y2 = rectArray[ind+2][1]+100
                winning_line_color = (0,0,255)
                
                
                player_2_score += 1
                data = data2.copy()
                data.to_csv("data.csv")
                for b in rectArray:
                    b[4] = 0
         
        if rectArray[0][4] == 1 and rectArray[4][4] == 1 and rectArray[8][4] == 1 :
            
            win_line_x1 = rectArray[0][0]+100
            win_line_y1 = rectArray[0][1]+100
            win_line_x2 = rectArray[8][0]+100
            win_line_y2 = rectArray[8][1]+100
            winning_line_color = (155,0,0)
            
            
            player_1_score += 1
            data2 = data.copy()
            for b in rectArray:
                b[4] = 0
                
        elif rectArray[0][4] == 2 and rectArray[4][4] == 2 and rectArray[8][4] == 2 :
            
            win_line_x1 = rectArray[0][0]+100
            win_line_y1 = rectArray[0][1]+100
            win_line_x2 = rectArray[8][0]+100
            win_line_y2 = rectArray[8][1]+100
            winning_line_color = (0,0,255)

            player_2_score += 1
            data = data2.copy()
            data.to_csv("data.csv")
            for b in rectArray:
                b[4] = 0
                
        elif rectArray[2][4] == 1 and rectArray[4][4] == 1 and rectArray[6][4] == 1 :
            
            win_line_x1 = rectArray[2][0]+100
            win_line_y1 = rectArray[2][1]+100
            win_line_x2 = rectArray[6][0]+100
            win_line_y2 = rectArray[6][1]+100
            winning_line_color = (155,0,0)
            
            player_1_score += 1
            data2 = data.copy()
            for b in rectArray:
                b[4] = 0
                
                
        elif rectArray[2][4] == 2 and rectArray[4][4] == 2 and rectArray[6][4] == 2 :
            
            win_line_x1 = rectArray[2][0]+100
            win_line_y1 = rectArray[2][1]+100
            win_line_x2 = rectArray[6][0]+100
            win_line_y2 = rectArray[6][1]+100
            winning_line_color = (0,0,255)
            
            player_2_score += 1
            data = data2.copy()
            data.to_csv("data.csv")
            for b in rectArray:
                b[4] = 0
        
        no_of_box_filled = 0
        
        for b in rectArray:
            
            no_of_box_filled += b[4]
            
            box = pygame.draw.rect(screen,(255,255,255),b[:4],10)
            if b[4] == 1:
                pygame.draw.circle(screen,(155,0,0),(b[0]+100,b[1]+100),70,20)
            elif b[4] == 2:
                pygame.draw.line(screen,(0,0,255),(b[0]+50,b[1]+50),(b[0]+150,b[1]+150),20)
                pygame.draw.line(screen,(0,0,255),(b[0]+150,b[1]+50),(b[0]+50,b[1]+150),20)
        
        
        if no_of_box_filled >= 13:
            for b in rectArray:
                b[4] = 0
                
        if player == 1:
            value_position = [[]]
            for b in rectArray:
                value_position[0].append(b[4])
            random_no = model.predict(value_position)[0]
            
            
            if rectArray[random_no][4] == 0:
                rectArray[random_no][4] = player
                player = 2
            
            else:
                random_no = random.randint(0,8)
                if rectArray[random_no][4] == 0:
                    rectArray[random_no][4] = player
                    player = 2
            
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                main_game = False

                x = data.drop(["9"],axis=1)
                data = data.drop_duplicates(subset=x.columns,keep="last")
                
                x = data.drop(["9"],axis=1)
                y = data.drop(x.columns,axis=1)
                data.to_csv("data.csv")
                model.fit(x,y)
                joblib.dump(model,"model.joblib")

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.pos[0]>back_btn_rect.x and event.pos[1]>back_btn_rect.y and event.pos[0]<back_btn_rect.x+back_btn_rect.width and event.pos[1]<back_btn_rect.y+back_btn_rect.height:
                    pygame.draw.rect(screen,(255,255,255),back_btn_rect,100,20)
                    main_game = False

                    x = data.drop(["9"],axis=1)
                    data = data.drop_duplicates(subset=x.columns,keep="last")
                    
                    x = data.drop(["9"],axis=1)
                    y = data.drop(x.columns,axis=1)
                    data.to_csv("data.csv")
                    model.fit(x,y)
                    joblib.dump(model,"model.joblib")
                    
                    
                    
                data_dict = {}
                for index,b in enumerate(rectArray):
                    data_dict[str(index)] = b[4]
                    if event.pos[0]>b[0] and event.pos[1]>b[1] and event.pos[0]<b[0]+b[2] and event.pos[1]<b[1]+b[3]:
                        
                        if player == 2 and b[4] == 0:
                            
                            data_dict["9"] =     index
                            df = pd.DataFrame(data_dict, columns=["0","1","2","3","4","5","6","7","8","9"],index=[0])
                            data2 = data2.append(df,ignore_index=True)
                            data2.fillna(0,inplace=True)
                            
                            b[4] = player
                            player = 1
                            
                            
              
        if win_line_x1 < win_line_x2 and win_line_y1 < win_line_y2:
            win_line_x1 += 20
            win_line_x2 -= 20
            win_line_y1 += 20
            win_line_y2 -= 20
        elif win_line_x1 > win_line_x2 and win_line_y1 < win_line_y2:
            win_line_x1 -= 20
            win_line_x2 += 20
            win_line_y1 += 20
            win_line_y2 -= 20
        elif win_line_x1 < win_line_x2:
            win_line_x1 += 20
            win_line_x2 -= 20
        elif win_line_y1 < win_line_y2:
            win_line_y1 += 20
            win_line_y2 -= 20
        else:
            win_line_x1 = 0
            win_line_y1 = 0
            win_line_x2 = 0
            win_line_y2 = 0
             
        pygame.display.update()
        pygame.display.flip()
        pygame.time.Clock().tick(30)
    
    

player1_data = data.copy()
player2_data = data.copy()

def main_page_multiplayer():
    global player1_data
    global player2_data
    player = 1
    
    player_1_score = 0
    player_2_score = 0
    
    rectArray = [
        [800,100,200,200,0],[1000,100,200,200,0],[1200,100,200,200,0],
        [800,300,200,200,0],[1000,300,200,200,0],[1200,300,200,200,0],
        [800,500,200,200,0],[1000,500,200,200,0],[1200,500,200,200,0]
    ]
    
    win_line_x1 = 0
    win_line_y1 = 0
    win_line_x2 = 0
    win_line_y2 = 0
    winning_line_color = (0,0,255)
    
    main_game = True
    while main_game:
        
        screen.fill((150,150,150))
        
        rect = pygame.draw.rect(screen,(255,255,255),(0,0,width,height),1)
        
        winning_line = pygame.draw.line(screen,winning_line_color,(win_line_x1,win_line_y1),(win_line_x2,win_line_y2),10)
        
        font_img = font72.render("Player 1",True, (155,0,0))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width/4,height/2-100)
        screen.blit(font_img,font_img_rect)
        
        font_img = font72.render(str(player_1_score),True, (155,0,0))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width/4,height/2)
        screen.blit(font_img,font_img_rect)
        
        font_img = font72.render("Player 2",True, (0,0,255))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width*3/4,height/2-100)
        screen.blit(font_img,font_img_rect)
        
        
        font_img = font72.render(str(player_2_score),True, (0,0,255))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width*3/4,height/2)
        screen.blit(font_img,font_img_rect)
        
        font_img = font72.render("back",True, (255,255,255))
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (200,100)
        screen.blit(font_img,font_img_rect)
        back_btn_rect = font_img_rect
        back_btn_rect.width =200
        back_btn_rect.height =100
        back_btn_rect.center = (200,100)
        back_btn = pygame.draw.rect(screen,(255,255,255),back_btn_rect,10,20)
        
        if player == 2:
            pygame.draw.circle(screen,(0,0,255),(width*3/4,height/2-200),20)
        else:
            pygame.draw.circle(screen,(155,0,0),(width/4,height/2-200),20)
        
        for ind in range(0,3):
            if rectArray[ind][4] == 1 and rectArray[ind+3][4] == 1 and rectArray[ind+6][4] == 1 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+6][0]+100
                win_line_y2 = rectArray[ind+6][1]+100
                winning_line_color = (155,0,0)
                
                player_1_score += 1
                data = player1_data.copy()
                data.to_csv("data.csv")
                player2_data = player1_data.copy()
                for b in rectArray:
                    b[4] = 0
                    
            elif rectArray[ind][4] == 2 and rectArray[ind+3][4] == 2 and rectArray[ind+6][4] == 2 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+6][0]+100
                win_line_y2 = rectArray[ind+6][1]+100
                winning_line_color = (0,0,255)
                
                player_2_score += 1
                data = player2_data.copy()
                data.to_csv("data.csv")
                player1_data = player2_data.copy()
                for b in rectArray:
                    b[4] = 0
                    
        for ind in range(0,7,3):
            if rectArray[ind][4] == 1 and rectArray[ind+1][4] == 1 and rectArray[ind+2][4] == 1 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+2][0]+100
                win_line_y2 = rectArray[ind+2][1]+100
                winning_line_color = (155,0,0)
                
                player_1_score += 1
                data = player1_data.copy()
                data.to_csv("data.csv")
                player2_data = player1_data.copy()
                for b in rectArray:
                    b[4] = 0
                    
            elif rectArray[ind][4] == 2 and rectArray[ind+1][4] == 2 and rectArray[ind+2][4] == 2 :
                
                win_line_x1 = rectArray[ind][0]+100
                win_line_y1 = rectArray[ind][1]+100
                win_line_x2 = rectArray[ind+2][0]+100
                win_line_y2 = rectArray[ind+2][1]+100
                winning_line_color = (0,0,255)
                
                player_2_score += 1
                data = player2_data.copy()
                data.to_csv("data.csv")
                player1_data = player2_data.copy()
                for b in rectArray:
                    b[4] = 0
                    
                    
                    
        if rectArray[0][4] == 1 and rectArray[4][4] == 1 and rectArray[8][4] == 1 :
            
            win_line_x1 = rectArray[0][0]+100
            win_line_y1 = rectArray[0][1]+100
            win_line_x2 = rectArray[8][0]+100
            win_line_y2 = rectArray[8][1]+100
            winning_line_color = (155,0,0)
            
            player_1_score += 1
            data = player1_data.copy()
            data.to_csv("data.csv")
            player2_data = player1_data.copy()
            for b in rectArray:
                b[4] = 0
                
        elif rectArray[0][4] == 2 and rectArray[4][4] == 2 and rectArray[8][4] == 2 :
            
            win_line_x1 = rectArray[0][0]+100
            win_line_y1 = rectArray[0][1]+100
            win_line_x2 = rectArray[8][0]+100
            win_line_y2 = rectArray[8][1]+100
            winning_line_color = (0,0,255)
            
            player_2_score += 1
            data = player2_data.copy()
            data.to_csv("data.csv")
            player1_data = player2_data.copy()
            for b in rectArray:
                b[4] = 0
                
        elif rectArray[2][4] == 1 and rectArray[4][4] == 1 and rectArray[6][4] == 1 :
            
            win_line_x1 = rectArray[2][0]+100
            win_line_y1 = rectArray[2][1]+100
            win_line_x2 = rectArray[6][0]+100
            win_line_y2 = rectArray[6][1]+100
            winning_line_color = (155,0,0)
            
            player_1_score += 1
            data = player1_data.copy()
            data.to_csv("data.csv")
            player2_data = player1_data.copy()
            for b in rectArray:
                b[4] = 0
                
                
        elif rectArray[2][4] == 2 and rectArray[4][4] == 2 and rectArray[6][4] == 2 :
            
            win_line_x1 = rectArray[2][0]+100
            win_line_y1 = rectArray[2][1]+100
            win_line_x2 = rectArray[6][0]+100
            win_line_y2 = rectArray[6][1]+100
            winning_line_color = (0,0,255)
            
            player_2_score += 1
            data = player2_data.copy()
            data.to_csv("data.csv")
            player1_data = player2_data.copy()
            for b in rectArray:
                b[4] = 0
        
        no_of_box_filled = 0
        
        for b in rectArray:
            
            no_of_box_filled += b[4]
            
            box = pygame.draw.rect(screen,(255,255,255),b[:4],10)
            if b[4] == 1:
                pygame.draw.circle(screen,(155,0,0),(b[0]+100,b[1]+100),70,20)
            elif b[4] == 2:
                pygame.draw.line(screen,(0,0,255),(b[0]+50,b[1]+50),(b[0]+150,b[1]+150),20)
                pygame.draw.line(screen,(0,0,255),(b[0]+150,b[1]+50),(b[0]+50,b[1]+150),20)
        
        
        if no_of_box_filled >= 13:
            for b in rectArray:
                b[4] = 0
                
                
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                main_game = False
                x = data.drop(["9"],axis=1)
                data = data.drop_duplicates(subset=x.columns,keep="last")
                    
                x = data.drop(["9"],axis=1)
                y = data.drop(x.columns,axis=1)
                data.to_csv("data.csv")
                model.fit(x,y)
                joblib.dump(model,"model.joblib")



            if event.type == pygame.MOUSEBUTTONDOWN:
                
                
                if event.pos[0]>back_btn_rect.x and event.pos[1]>back_btn_rect.y and event.pos[0]<back_btn_rect.x+back_btn_rect.width and event.pos[1]<back_btn_rect.y+back_btn_rect.height:
                    pygame.draw.rect(screen,(255,255,255),back_btn_rect,100,20)
                    main_game = False
                    
                    x = data.drop(["9"],axis=1)
                    data = data.drop_duplicates(subset=x.columns,keep="last")
                    
                    x = data.drop(["9"],axis=1)
                    y = data.drop(x.columns,axis=1)
                    data.to_csv("data.csv")
                    model.fit(x,y)
                    joblib.dump(model,"model.joblib")

                data_dict = {}
                for index,b in enumerate(rectArray):
                    data_dict[str(index)] = b[4]
                    if event.pos[0]>b[0] and event.pos[1]>b[1] and event.pos[0]<b[0]+b[2] and event.pos[1]<b[1]+b[3]:
                        
                        if player == 1 and b[4] == 0:
                            data_dict["9"] =     index
                            df = pd.DataFrame(data_dict, columns=["0","1","2","3","4","5","6","7","8","9"],index=[0])
                            player1_data = player1_data.append(df,ignore_index=True)
                            player1_data.fillna(0,inplace=True)
                            
                            b[4] = player
                            player = 2
                            
                            
                        elif player == 2 and b[4] == 0:
                            data_dict["9"] =     index
                            df = pd.DataFrame(data_dict, columns=["0","1","2","3","4","5","6","7","8","9"],index=[0])
                            player2_data = player2_data.append(df,ignore_index=True)
                            player2_data.fillna(0,inplace=True)
                            
                            b[4] = player
                            player = 2
                            b[4] = player
                            player = 1
                     
        
        if win_line_x1 < win_line_x2 and win_line_y1 < win_line_y2:
            win_line_x1 += 20
            win_line_x2 -= 20
            win_line_y1 += 20
            win_line_y2 -= 20
        elif win_line_x1 > win_line_x2 and win_line_y1 < win_line_y2:
            win_line_x1 -= 20
            win_line_x2 += 20
            win_line_y1 += 20
            win_line_y2 -= 20
        elif win_line_x1 < win_line_x2:
            win_line_x1 += 20
            win_line_x2 -= 20
        elif win_line_y1 < win_line_y2:
            win_line_y1 += 20
            win_line_y2 -= 20
        else:
            win_line_x1 = 0
            win_line_y1 = 0
            win_line_x2 = 0
            win_line_y2 = 0
             
        pygame.display.update()
        pygame.display.flip()
        pygame.time.Clock().tick(30)
    





def hero_page():
    game_mode = True  
    x = 0
    
    game_type = 'singal'
    
    while game_mode:
        
                
        screen.fill((150,150,150)) 
        rect = pygame.draw.rect(screen,(255,255,255),(0,0,width,height),1)
        
       
        
        line = pygame.draw.line(screen,(0,0,255),(width/2,height/1.5),(width-x,height/1.5),10)
        line = pygame.draw.line(screen,(155,0,0),(width/2,height/1.5),(x,height/1.5),10)
        x += 30
        
        if x>width:
            x=0
            
        font_img = font96.render('TIC TAC TOE',True,(0,0,0) )
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width/3,height/3)
        screen.blit(font_img,font_img_rect)
        
        font_img = font64.render("Play with AI",True,(0,0,0) )
        font_img_rect = font_img.get_rect()
        font_img_rect.center = (width/3+90,height/3+64)
        screen.blit(font_img,font_img_rect)
        
        font_img = font64.render("Start",True,(255,255,255) )
        font_start_img_rect = font_img.get_rect()
        font_start_img_rect.center = (width/3+100,height/2+50)
        screen.blit(font_img,font_start_img_rect)
        
        start_btn_rect = font_start_img_rect
        start_btn_rect.width =200
        start_btn_rect.height = 100
        start_btn_rect.center = (width/3+100,height/2+50)
        start_btn = pygame.draw.rect(screen,(255,255,255),start_btn_rect,10,20)
        
        
        font_img = font64.render("Singal player",True,(0,0,0) )
        font_start_img_rect = font_img.get_rect()
        font_start_img_rect.center = (width/1.5,height/2+50)
        screen.blit(font_img,font_start_img_rect)
        
        
        font_img = font64.render("Multi player",True,(0,0,0) )
        font_start_img_rect = font_img.get_rect()
        font_start_img_rect.center = (width/1.5+500,height/2+50)
        screen.blit(font_img,font_start_img_rect)
        
        switch_btn_box = pygame.draw.rect(screen,(255,255,255),(width/1.5+183,height/2+5,150,90),10,200)
        
        
        if game_type == 'singal':
            switch_btn = pygame.draw.circle(screen,(255,255,255),(width/1.5+228,height/2+50),25)
        else:
            switch_btn = pygame.draw.circle(screen,(255,255,255),(width/1.5+288,height/2+50),25)
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                game_mode = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.pos[0]>start_btn_rect.x and event.pos[1]>start_btn_rect.y and event.pos[0]<(start_btn_rect.x + start_btn_rect.width) and event.pos[1]<(start_btn_rect.y+start_btn_rect.height) :
                    
                     pygame.draw.rect(screen,(255,255,255),start_btn_rect,100,20)
                     pygame.display.update()
                     pygame.display.flip()
                     if game_type == 'singal':
                        main_page_singalplayer()
                     else:
                         main_page_multiplayer()
                    
                if event.pos[0]>(width/1.5+183) and event.pos[1]>(height/2+10) and event.pos[0]<(width/1.5+333) and event.pos[1]<(height/2+90) :
                     
                     
                     if game_type == 'singal':
                         game_type = 'multi'
                     else:
                         game_type = 'singal'
                     
                     
                     
        pygame.display.update()
        pygame.display.flip()
        pygame.time.Clock().tick(30)
    
    pygame.quit()
        
             
    
                
hero_page()

