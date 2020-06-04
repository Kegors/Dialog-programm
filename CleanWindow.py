import curses


def main(stdscr, x, y, width, height):
	for i in range(x, height):
		for j in range(y, width):
			stdscr.addch(i, j, " ")
			

if __name__=="__main__":
	main()