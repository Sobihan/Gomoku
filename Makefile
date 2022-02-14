RM	=	rm -f

NAME	=	 pbrain-gomoku-ai

SRC	=	main.py

$(NAME)	:
			cp $(SRC)  pbrain-gomoku-ai
			chmod +x pbrain-gomoku-ai

.PHONY:
all	:
			$(NAME)

.PHONY:
clean	:
			$(RM) pbrain-gomoku-ai

.PHONY:
fclean	:	clean

.PHONY:
re: 		fclean
			cp $(SRC)  pbrain-gomoku-ai
			chmod +x pbrain-gomoku-ai