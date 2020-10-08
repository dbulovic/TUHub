//
// Created by marson on 9/7/20.
//
#include "snake.h"
#include <stdlib.h>


WINDOW *game_window;
char game_map [MAP_LENGTH][MAP_WIDTH];

pthread_t user_snake_tid;
pthread_t enemy_snake_tid[NUMBER_ENEMIES];
pthread_t chest_tid;

time_t time1;

position user_snake_pos = {MAP_WIDTH / 2, MAP_LENGTH - 2,MAP_WIDTH / 2 + 1, MAP_LENGTH - 2,MAP_WIDTH / 2 + 2, MAP_LENGTH - 2};




int lifepoints = 100;
int points = 0;

int chest_collected_flag = 0;

void *snake()
{
  //TODO STUDENTS: Find out why the chests are not disappearing when the users snake eats them
  // -solve the problem described above
  // -add points (look at the constant definition) whenever the snake eats a chest
  // -set the the threads cancelability type to a type where it can be canceled at ANY time (look at the manpage)

  //TODO BEGIN:

  pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);

  //TODO END:

  char direction = 'l';
  char prev_direction = 'l';

  game_map[user_snake_pos.y_f_][user_snake_pos.x_f_] = (char) USER_SNAKE;
  game_map[user_snake_pos.y_m_][user_snake_pos.x_m_] = (char) USER_SNAKE;
  game_map[user_snake_pos.y_b_][user_snake_pos.x_b_] = (char) USER_SNAKE;

  refresh_map();
  int c;
  keypad (stdscr, TRUE);
  noecho();
  timeout(1);
  while (true)
  {
    c = getch();
    switch (c)
    {
      case 's':
        direction = 'd';
        break;
      case 'w':
        direction = 'u';
        break;
      case 'a':
        direction = 'l';
        break;
      case 'd':
        direction = 'r';
        break;
      default:
        break;
    }
    if(c == 'q')
    {
      lifepoints = 0;
      continue;
    }
    int counter = 10000;
    while(counter > 0)
    {
      if(game_map[user_snake_pos.y_f_][user_snake_pos.x_f_] == (char) ENEMY_SNAKE ||
         game_map[user_snake_pos.y_m_][user_snake_pos.x_m_] == (char) ENEMY_SNAKE||
         game_map[user_snake_pos.y_b_][user_snake_pos.x_b_] == (char) ENEMY_SNAKE )
      {
        lifepoints = 0;
      }
      counter--;
    }
    usleep(100000);
    if((game_map[user_snake_pos.y_f_][user_snake_pos.x_f_] == (char) CHEST_A ||
        game_map[user_snake_pos.y_m_][user_snake_pos.x_m_] == (char) CHEST_A||
        game_map[user_snake_pos.y_b_][user_snake_pos.x_b_] == (char) CHEST_A) )
    {
      //TODO: begin
      points++;
      pthread_cancel(chest_tid);
      //TODO: end
      chest_collected_flag = 1;
    }
    moveSnake(&direction, &prev_direction, &user_snake_pos, USER_SNAKE);

  }
  //not needed
  assert(direction);
  lifepoints = 0;
  return (void*)999;
}
void *enemySnakes(void* params)
{


  //TODO STUDENTS:
  // -parse the parameters that you shall have handed over in init_enemies() correctly
  // -make sure the position of the type of the enemy is taken from the parameters
  // -set the the threads cancelability type to a type where it can be canceled at ANY time (look at the manpage)

  //TODO: Begin
  
  pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);

  
  parameters *en_params = (parameters *) params;

  unsigned char position_x_f = en_params->pos_x_ ;
  unsigned char position_y_f = en_params->pos_y_ ;
  unsigned char enemy_type = en_params->type_ ;

  free(params);



  //TODO: END

  position enemy_snake_pos = {position_x_f, position_y_f, position_x_f +1, position_y_f, position_x_f +2, position_y_f};

  game_map[enemy_snake_pos.y_f_][enemy_snake_pos.x_f_] = (char) enemy_type;
  game_map[enemy_snake_pos.y_m_][enemy_snake_pos.x_m_] = (char) enemy_type;
  game_map[enemy_snake_pos.y_b_][enemy_snake_pos.x_b_] = (char) enemy_type;

  int nr_direction = 0;
  char prev_direction = 'l';

  while(lifepoints > 0)
  {
    usleep(100000);
    int counter = 10000;
    while(counter > 0)
    {
      if(game_map[user_snake_pos.y_f_][user_snake_pos.x_f_] == (char) enemy_type ||
         game_map[user_snake_pos.y_m_][user_snake_pos.x_m_] == (char) enemy_type||
         game_map[user_snake_pos.y_b_][user_snake_pos.x_b_] == (char) enemy_type )
      {
        lifepoints = 0;
        break;
      }
      counter--;
    }
    if (rand() % 5 == 0)
    {
      nr_direction = rand() % 4;
    }
    char direction;
    switch(nr_direction)
    {
    case 0:
      direction = 'l';
      moveSnake(&direction, &prev_direction,&enemy_snake_pos,(char) enemy_type);
      break;
    case 1:
      direction = 'r';
      moveSnake(&direction, &prev_direction,&enemy_snake_pos,(char) enemy_type);
      break;
    case 2:
      direction = 'u';
      moveSnake(&direction, &prev_direction,&enemy_snake_pos,(char) enemy_type);
      break;
    case 3:
      direction = 'd';
      moveSnake(&direction, &prev_direction,&enemy_snake_pos, (char)enemy_type);
      break;
    default:
      break;
    }
  }
  return (void*)999;
}


void init_enemies(int pid_pos, unsigned char pos_x_, unsigned char pos_y_,
                  unsigned char type_ )
{
  //TODO: Implement the whole function:
  // - spawn an enemy snake, make sure it appears at the coordinates from the parameters and has the type specified in type_
  // - use the enemy_snake_tid array 
  // - look at the provided data structures in the header make sure that you do a deep copy of the params when passing them (dynamic memory may be useful)

  //TODO BEGIN


  parameters *enemy_params = (parameters*)malloc(sizeof(parameters));


  // parameters enemy_params;
  
  enemy_params->pos_x_ = pos_x_;
  enemy_params->pos_y_ = pos_y_;
  enemy_params->type_ = type_;


  pthread_create(&enemy_snake_tid[pid_pos], NULL, enemySnakes, (void*)enemy_params);

  
  
  //TODO: END
}
void *placeChests()
{
  //TODO BEGIN:
  // -set the the threads cancelability type to a type where it can be canceled at ANY time (look at the manpage)
  pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);

  //TODO END

  unsigned char position_x = getRandPosX();
  unsigned position_y = getRandPosY();

  while(1)
  {
    game_map[position_y][position_x] = (char) CHEST_A;
  }
}


int main()
{
  void* rvalue_user_snake = 0;
  void* rvalue_enemies[1000];
  void* rvalue_chest = 0;
  init_map();
  

  //TODO STUDENTS: spawn the user's snake
  // -Arguments needed? Attributes needed? Look at the snake function
  // -look at the pthread_t variables from above... USE one of them!!

  //TODO BEGIN
  pthread_create(&user_snake_tid, NULL, snake, NULL);
  
  

  //TODO END

  srand((unsigned int) time(&time1));


  for (int i = 0; i < NUMBER_ENEMIES; i++)
  {
    char pos_x = getRandPosX();
    char pos_y = getRandPosY();

    init_enemies(i, pos_x, pos_y,ENEMY_SNAKE);
    if(i == 1)
      refresh_map();
  }

  //TODO: spawn a initial chest, if a chest is collected (there's a flag for that), a new chest shall be spawned
  // -make sure that all threads are terminated and store the return value in rvalue_chest
  // -have a look at the other TODOs from above (some of them need to be done in order to get the chests working)
  // -Arguments needed? look at the placeChest function

  //TODO: Begin

  pthread_create(&chest_tid, NULL, placeChests, NULL);

  //TODO: End

  while (lifepoints > 0)
  {
      usleep(10000);

      //TODO: Begin

      if (chest_collected_flag == 1)
      {
        pthread_join(chest_tid, &rvalue_chest);
        pthread_create(&chest_tid, NULL, placeChests, NULL);
        chest_collected_flag = 0;
      }     

      
      //TODO: END

      refresh_map();
  }
 

  //TODO make sure that the rest of all the running threads are terminated before returning from main and fetch their return values (store the return values in the predefined 'rvalue_*' variables)
  // - have a closer look on the other TODOs too there are connections

  //TODO: BEGIN
  for (int i = 0; i < NUMBER_ENEMIES; i++)
  {
    pthread_join(enemy_snake_tid[i], &rvalue_enemies[i]);
  }
  
  pthread_exit(&rvalue_user_snake);


  //TODO: END


  return end_game(rvalue_user_snake, rvalue_enemies, rvalue_chest);
}




