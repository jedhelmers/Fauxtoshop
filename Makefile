CC = g++
# CFLAGS = -std=c++11 -Wall -Wextra -pedantic
CFLAGS = -std=c++11 -Wall -Wextra -pedantic -I/opt/homebrew/opt/opencv/include/opencv4
LDFLAGS = -L/opt/homebrew/opt/opencv/lib -lopencv_core -lopencv_highgui -lopencv_imgproc

LIBS = -lopencv_core -lopencv_imgproc -lopencv_highgui

SRCS = main.cpp
OBJS = $(SRCS:.cpp=.o)
EXECUTABLE = artboard

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS) $(LIBS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(EXECUTABLE)