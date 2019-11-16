ejercicio14-2.png : ejercicio14-2.py euler.dat rk4.dat rk4f.dat
	python ejercicio14-2.py

euler.dat : e.x
	./e.x 

rk4.dat : r.x
	./r.x 0 > rk4.dat
	
rk4f.dat :r.x
	./r.x 1 >rk4f.dat
    
e.x : ejercicio14-2.cpp
	c++ ejercicio14-2.cpp -o e.x

r.x : ejercicio14-2rk4.cpp
	c++ ejercicio14-2rk4.cpp -o r.x

clean:
	rm e.x  ejercicio14-2.png euler.dat rk4.dat r.x rk4f.dat