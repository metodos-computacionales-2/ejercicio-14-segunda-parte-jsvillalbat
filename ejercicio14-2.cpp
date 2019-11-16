#include<iostream>
#include<cmath>
#include <fstream>
using namespace std;

//Defino mis constantes

const double K = 100;
const double M = 2;
const double LAMBDA = 1;
const double DeltaT = 0.01;

double f0(double t, double y0, double y1) //Derivada de y0
{
  return y1;
}

//Función que describe mi movimiento parabolico es decir la derivada de y1
double f1(double t, double y0, double y1)
{
  return (-K/M)*pow(y0, LAMBDA);
}

//FUncion que implementa el método de Euler para la derivada de y1
double euler(double & y0, double & y1, double &t)
{
    return y1 + DeltaT*f1(t,y0,y1);
}
//Euler para la derivada de y0
double euler1(double &y0,double & y1,double &t)
{
	return y0 + DeltaT*f0(t,y0,y1);
}

int main()
{
	//Defino mis condiciones iniciales
    double y0 = 1.0,t0 = 0.0,y1 = 0.0;
	//Abro el archivo al cual voy a mandar mis datos
	ofstream outfile;
    outfile.open("euler.dat");
	//Realizo 1000 iteraciones
    for(int i =0;i<1000;i++)
    {
		outfile << t0<<"\t"<<euler1(y0,y1,t0)<< "\t"<< euler(y0,y1,t0) <<endl;
        t0+=DeltaT;
		y0 = euler1(y0,y1,t0);
        y1 = euler(y0,y1,t0);
    }
	outfile.close();

   return 0;
}
