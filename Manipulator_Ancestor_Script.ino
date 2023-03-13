//library

#include <LiquidCrystal.h>
#include <Keypad.h>
#include <DynamixelSerial.h>
#include <Servo.h>

LiquidCrystal lcd (113, 12, 11, 10, 9, 8);

#include <math.h>

#define cosf cos
#define sinf sin
#define atan2f atan2
#define PI 3.141592654

Servo servo1;
Servo servo2;

float X, Y, Z;
float Xa, Ya, Za;
long int L1, L2, L3;
float s3a, s3, c3, h;
float s3ax, s3x, c3x, hx;
float p1, p2, theta2a;
float p1x, p2x, theta2ax;
float theta1, theta2, theta3;
float theta1x, theta2x, theta3x;
float T1a, T2a, T3a;
float T1b, T2b, T3b;
float T1, T2, T3;
float T1x, T2x, T3x;

int dynamixel = 2;
int b = 0;
int START = 3;
int val1, val2;

// Definisi variabel-variabel
String InputKordinatX;
String InputKordinatY;
String InputKordinatZ;
String InputKordinatX1;
String InputKordinatY1;
String InputKordinatZ1;

long int count = 0;
long int a = 0;
const byte numRows = 4;     //Baris pada keypad
const byte numCols = 4;     //Kolom pada keypad
char keymap [numRows][numCols] =
{
    {'1','2','3','A'},
    {'4','5','6','B'},
    {'7','8','9','C'},
    {'*','0','#','D'}
};

byte rowPins[numRows] = {30, 32, 34, 36};   //Connect to the row pinouts of the keypad
byte colPins[numCols] = {22, 24, 26, 28};   //Connect to the column pinouts of the keypad

Keypad myKeypad = Keypad(makeKeymap(keymap), rowPins, colPins, numRows, numCols);
char keypressed = myKeypad.getKey();

// Sub Program
void setup()
{
    // Set up the LCD's number of columns and rows:
    lcd.begin(20,4);
    Serial.begin(9600);
    lcd.setCursor(0,0);
    lcd.print("TUGAS AKHIR 2017");
    lcd.setCursor(0,1);
    lcd.print("ROBOT MANIPULATOR");
    lcd.setCursor(0,3);
    lcd.print("BY: ABAS & JOHN");
    delay(3000);
}

void InputKordinat_X()
{
    Input_Pertama:
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("INPUT KORDINAT X,Y,Z");
    lcd.setCursor(0,1);
    lcd.print("KORDINAT X:");
    lcd.setCursor(0,3);
    lcd.print("TEKAN D JIKA SELESAI");

    Input_Lagi:
    char keypressed = myKeypad.getKey();
    if (keypressed == 'D');
    {
        goto Input_Ok;
    }
    if (keypressed != NO_KEY)
    {
        keypressed;
        count++;
        if (count >= 0 && count <= 20)
        {
            lcd.setCursor(a,2);
            lcd.print(keypressed);
        }
        a++;
        InputKordinatX += keypressed;
        X = InputKordinatX.toInt();
        Serial.print(X);
        if (keypressed == 'C')
        {
            lcd.clear();
            lcd.setCursor(0,1);
            lcd.print("  INPUT BERHASIL  ");
            lcd.setCursor(0,2);
            lcd.print("   TERHAPUS   ");
            InputKordinatX = "";
            a = 0;
            delay(5000);
            goto Input_Pertama;
        }
    }
    goto Input_Lagi;
    Input_Ok:
    a = 0;
    lcd.clear();
}

void InputKordinat_X1()
{
    Input_Pertama:
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("INPUT KORDINAT X,Y,Z");
    lcd.setCursor(0,1);
    lcd.print("KORDINAT X':");
    lcd.setCursor(0,3);
    lcd.print("TEKAN D JIKA SELESAI");

    Input_Lagi:
    char keypressed = myKeypad.getKey();
    if (keypressed == 'D')
    {
        goto Input_Ok;
    }
    if (keypressed != NO_KEY)
    {
        keypressed;
        count++;
        if (count >= 0 && count <= 20)
        {
            lcd.setCursor(a,2);
            lcd.print(keypressed);
        }
        a++;
        InputKordinatX1 += keypressed;
        Xa = InputKordinatX1.toInt();
        Serial.print(Xa);
        if (keypressed == 'C');
        {
            lcd.clear();
            lcd.setCursor(0,1);
            lcd.print("  INPUT BERHASIL  ");
            lcd.setCursor(0,2);
            lcd.print("   TERHAPUS   ");
            InputKordinatX1 = "";
            a = 0;
            delay(5000);
            goto Input_Pertama;
        }
    }
    goto Input_Lagi;
    Input_Ok:
    a = 0;
    lcd.clear();
}

void InputKordinat_Y()
{
    Input_Pertama:
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("INPUT KORDINAT X,Y,Z");
    lcd.setCursor(0,1);
    lcd.print("KORDINAT Y:");
    lcd.setCursor(0,3);
    lcd.print("TEKAN D JIKA SELESAI");

    Input_Lagi:
    char keypressed = myKeypad.getKey();
    if (keypressed == 'D')
    {
        goto Input_Ok;
    }
    if (keypressed != NO_KEY)
    {
        keypressed;
        count++;
        if (count >= 0 && count <= 20)
        {
            lcd.setCursor(a,2);
            lcd.print(keypressed);
        }

        a++;
        InputKordinatY += keypressed;
        Y = InputKordinatY.toInt();
        Serial.print(Y);
        if (keypressed == 'C');
        {
            lcd.clear();
            lcd.setCursor(0,1);
            lcd.print("  INPUT BERHASIL  ");
            lcd.setCursor(0,2);
            lcd.print("   TERHAPUS   ");
            InputKordinatY = "";
            a = 0;
            delay(5000);
            goto Input_Pertama;
        }
    }
    goto Input_Lagi;
    Input_Ok:
    a = 0;
    lcd.clear();
}

void InputKordinat_Y1()
{
    Input_Pertama:
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("INPUT KORDINAT X,Y,Z");
    lcd.setCursor(0,1);
    lcd.print("KORDINAT Y':");
    lcd.setCursor(0,3);
    lcd.print("TEKAN D JIKA SELESAI");
    
    Input_Lagi:
    char keypressed = myKeypad.getKey();
    if (keypressed == 'D')
    {
        goto Input_Ok;
    }
    if (keypressed != NO_KEY)
    {
        keypressed;
        count++;
        if (count >= 0 && count <= 20)
        {
            lcd.setCursor(a,2);
            lcd.print(keypressed);
        }
        a++;
        InputKordinatY1 += keypressed;
        Ya = InputKordinatY1.toInt();
        Serial.print(Ya);
        if (keypressed == 'C')
        {
            lcd.clear();
            lcd.setCursor(0,1);
            lcd.print("  INPUT BERHASIL  ");
            lcd.setCursor(0,2);
            lcd.print("   TERHAPUS   ");
            InputKordinatY1 ="";
            a = 0;
            delay(5000);
            goto Input_Pertama;
        }
    }
    goto Input_Lagi;
    Input_Ok:
    a = 0;
    lcd.clear();
}

void InputKordinat_Z()
{
    Input_Pertama:
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("INPUT KORDINAT X,Y,Z");
    lcd.setCursor(0,1);
    lcd.print("KORDINAT Z:");
    lcd.setCursor(0,3);
    lcd.print("TEKAN D JIKA SELESAI");

    Input_Lagi:
    char keypressed = myKeypad.getKey();
    if (keypressed == 'D')
    {
        goto Input_Ok;
    }
    if (keypressed != NO_KEY)
    {
        keypressed;
        count++;
        if (count >= 0 && count <= 20)
        {
            lcd.setCursor(a,2);
            lcd.print(keypressed);
        }
        a++;
        InputKordinatZ += keypressed;
        Z = InputKordinatZ.toInt();
        Serial.print(Z);
        if (keypressed == 'C')
        {
            lcd.clear();
            lcd.setCursor(0,1);
            lcd.print("  INPUT BERHASIL  ");
            lcd.setCursor(0,2);
            lcd.print("   TERHAPUS   ");
            InputKordinatZ = "";
            a = 0;
            delay(5000);
            goto Input_Pertama;
        }
    }
    goto Input_Lagi;
    Input_Ok:
    a = 0;
    lcd.clear();
}

void InputKordinat_Z1()
{
    Input_Pertama:
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("INPUT KORDINAT X,Y,Z");
    lcd.setCursor(0,1);
    lcd.print("KORDInat z':");
    lcd.setCursor(0,3);
    lcd.print("TEKAN D JIKA SELESAI");

    Input_Lagi:
    char keypressed = myKeypad.getKey();
    if (keypressed == 'D')
    {
        goto Input_Ok;
    }
    if (keypressed != NO_KEY)
    {
        keypressed;
        count++;
        if (count >= 0 && count <= 20)
        {
            lcd.setCursor(a,2);
            lcd.print(keypressed);
        }
        a++;
        InputKordinatZ1 += keypressed;
        Za = InputKordinatZ1.toInt();
        Serial.print(Za);
        if (keypressed == 'C')
        {
            lcd.clear();
            lcd.setCursor(0,1);
            lcd.print("  INPUT BERHASIL  ");
            lcd.setCursor(0,2);
            lcd.print("   TERHAPUS   ");
            lcd.setCursor(0,1);
            InputKordinatZ1 = "";
            a = 0;
            delay(5000);
            goto Input_Pertama;
        }      
    }
    goto Input_Lagi;
    Input_Ok:
    a = 0;
    lcd.clear();
}

void Formulasi()
{
    L1 = 85;    //mm
    L2 = 165;   //mm
    L3 = 155;   //mm

    //Formulasi Invers Kinematics Robot Manipulator
    h = Z-L1;   //mm
    theta1 = atan2(Y,X);    //radian
    c3 = (X*X + Y*Y + h*h - L2*L2 - L3*L3)/(2*L2*L3);
    s3 = -sqrt(1-c3*c3);    //for down elbow
    s3a = sqrt(1-c3*c3);    //for up elbow
    theta3 = atan2(s3,c3);  //radian
    p1 = (Y*L3*cos(theta3)+Y*L2)+(X*L3*sin(theta3));
    p2 = (X*L3*cos(theta3)+X*L2)-(Y*L3*sin(theta3));
    theta2a = atan2(p1,p2); //radian
    theta2 = 2*theta2a;     //radian

    T1a = theta1 * 180.0/PI;    //degree
    T2a = theta2 * 180.0/PI;    //degree
    T3a = theta3 * 180.0/PI;    //degree

    T1 = (150+T1a)*3.41;
    T2 = (60+T2a)*3.41;
    T3 = (150+T3a)*3.41;
}

void Formulasi_2()
{
    L1 = 85;    //mm
    L2 = 165;   //mm
    L3 = 155;   //mm

    //Formulasi Invers Kinematics Robot Manipulator
    hx = Za - L1;   //mm
    theta1x = atan2(Ya,Xa); //radian
    c3x = (Xa*Xa + Ya*Ya + hx*hx - L2*L2 - L3*L3)/(2*L2*L3);
    s3x = -sqrt(1-c3x*c3x); //for down elbow
    s3ax = sqrt(1-c3x*c3x); //for up elbow
    theta3x = atan2(s3x,c3x);   //radian
    p1x = (Ya*L3*cos(theta3x)+Ya*L2)+(Xa*L3*sin(theta3x));
    p2x = (Xa*L3*cos(theta3x)+Xa*L2)-(Ya*L3*sin(theta3x));
    theta2ax = atan2(p1x,p2x);  //radian
    theta2x = 2*theta2ax;   //radian

    T1b = theta1x * 180.0/PI;   //degree
    T2b = theta2x * 180.0/PI;   //degree
    T3b = theta3x * 180.0/PI;   //degree

    T1x = (150+T1b)*3.41;
    T2x = (60+T2b)*3.41;
    T3x = (150+T3b)*3.41;
}

void setup_2()
{
    Dynamixel.begin(1000000,2); //Initialize the servo at 1Mbps and Pin Control 2
    delay(1000);

    //Initialize the dynamixel pin as an output:
    pinMode(dynamixel, OUTPUT);

    //Initialize the pushbutton pin as an input:
    servo1.attach(5);   //Attaches the servo on pin 5 to the servo object
    servo2.attach(6);   //Attaches the servo on pin 6 to the servo object
    pinMode(START, INPUT);
}

void Gerakan_1()
{
    if (digitalRead(START)==LOW && (b==1))
    {
        Dynamixel.moveSpeed(1,T1,50);   //240 degree motor = 90 degree manipulator
        delay(2000);
        Dynamixel.moveSpeed(2,T2,50);   //150 degree motor = 90 degree manipulator
        delay(2000);
        Dynamixel.moveSpeed(3,T3,50);   //60 degree motor = -90 degree manipulator
        delay(2000);
        val1 = map(0, 0, 1023, 0, 180); //Scale it to use it with the servo (value between 0 and 180)
        servo1.write(val1);             //Sets the servo position according to the scaled value
        delay(15);
        b = 2;
    }
}

void Gerakan_2()
{
    if (digitalRead(START)==LOW && (b==2))
    {
        Dynamixel.moveSpeed(2,376,50);  //120 degree motor
        delay(2000);
        val2 = map(1023, 0, 1023, 0, 180);  //Scale it to use it with the servo (value between 0 and 180)
        servo2.write(val2);                 //Sets the servo position according to the scaled value
        delay(30);
        delay(1000);
        Dynamixel.moveSpeed(1,T1x,50);  //240 degree motor = 90 degree manipulator
        delay(2000);
        Dynamixel.moveSpeed(2,T2x,50);  //150 degree motor = 90 degree manipulator
        delay(2000);
        Dynamixel.moveSpeed(3,T3x,50);  //60 degree motor = -90 degree manipulator
        delay(2000);
        val1 = map(426, 0, 1023, 0, 180);   //scale it to use it with the servo (value between 0 and 180)
        servo1.write(val1);                 //Sets the servo position according to the scaled value
        delay(15);
        b = 3;
    }
}

//main program
void loop()
{
    setup_2();
    Tunggu_Start:
    if (digitalRead(START)==HIGH && (b==0))
    {
        //POSISI AWAL ROBOT
        Dynamixel.moveSpeed(2,358,50);  //150 degree motor
        delay(1500);
        Dynamixel.moveSpeed(3,409,50);  //150 degree motor
        delay(1500);
        Dynamixel.moveSpeed(1,512,50);  //150 degree motor
        delay(1500);
        val1 = map(426, 0, 1023, 0, 180);   //scale it to use it with the servo (value between 0 and 180)
        servo1.write(val1);                 //Sets the servo position according to the scaled value
        delay(30);
        val2 = map(0, 0, 1023, 0, 180);     //scale it to use it with the servo (value between 0 and 180)
        servo2.write(val2);                 //Sets the servo position according to the scaled value
        delay(15);
        b = 1;
    }
    else
    {
        goto Tunggu_Start;
    }

    // INPUTAN KOORDINAT AWAL
    Step1:
    InputKordinat_X();
    InputKordinat_Y();
    InputKordinat_Z();

    lcd.setCursor(0,0);
    lcd.print("INPUT X= ");
    lcd.setCursor(10,0);
    lcd.print(X);
    lcd.setCursor(0,1);
    lcd.print("INPUT Y= ");
    lcd.setCursor(10,1);
    lcd.print(Y);
    lcd.setCursor(0,2);
    lcd.print("INPUT Z= ");
    lcd.setCursor(10,2);
    lcd.print(Z);
    lcd.setCursor(0,3);
    lcd.print("START=INPUTAN KEDUA");
    delay(2000);
    Formulasi();

    Tunggu_Konfirmasi:
    if (digitalRead(START)==HIGH && (b==1))
    {
        Step2:
        // INPUTAN KOORDINAT KEDUA
        InputKordinat_X1();
        InputKordinat_Y1();
        InputKordinat_Z1();

        lcd.setCursor(0,0);
        lcd.print("INPUT X'= ");
        lcd.setCursor(10,0);
        lcd.print(Xa);
        lcd.setCursor(0,1);
        lcd.print("INPUT Y'= ");
        lcd.setCursor(10,1);
        lcd.print(Ya);
        lcd.setCursor(0,2);
        lcd.print("INPUT Z'= ");
        lcd.setCursor(10,2);
        lcd.print(Za);
        lcd.setCursor(0,3);
        lcd.print("YA=START   TIDAK=B");
        delay(2000);
        Formulasi_2();
    }
    else
    {
        goto Tunggu_Konfirmasi;
    }

    Tunggu_Konfirmasi2:
    char keypressed = myKeypad.getKey();
    if (digitalRead(START)==HIGH)
    {
        setup_2();
        Gerakan_1();
        delay(2000);
        setup_2();
        Gerakan_2();
        delay(2000);
    }
    else if (keypressed == 'B')
    {
        a = 0;
        b = 1;
        Xa = 0;
        Ya = 0;
        Za = 0;
        InputKordinatX1 = "";
        InputKordinatY1 = "";
        InputKordinatZ1 = "";
        goto Step2;
    }
    else
    {
        goto Tunggu_Konfirmasi2;
    }

    Serial.begin(9600);
    Serial.println(" ");
    Serial.print(" Theta 1 = ");
    Serial.print(T1a);
    Serial.print(" Theta 2 = ");
    Serial.print(T2a);
    Serial.print(" Theta 3 = ");
    Serial.print(T3a);
    Serial.print(" Theta 1' = ");
    Serial.print(T1b);
    Serial.print(" Theta 2' = ");
    Serial.print(T2b);
    Serial.print(" Theta 3' = ");
    Serial.print(T3b);
    Serial.end();                    //End Serial Communication

    // POSISI AKHIR ROBOT
    setup_2();
    if (digitalRead(START)==LOW && (b==3))
    Dynamixel.moveSpeed(2,358,50);  //150 degree motor
    delay(2000);
    Dynamixel.moveSpeed(3,409,50);  //150 degree motor
    delay(2000);
    Dynamixel.moveSpeed(1,512,50);  //150 degree motor
    delay(3500);
    val2 = map(0, 0, 1023, 0, 180); //scale it to use it with the servo (value between 0 and 180)
    servo2.write(val2);             //Sets the servo position according to the scaled value
    delay(15);
    b = 4;

    Input_Baru:
    if (digitalRead(b==4))
    {
        lcd.setCursor(0,0);
        lcd.print("   PROSES   ");
        lcd.setCursor(0,1);
        lcd.print("  TELAH SELESAI  ");
        lcd.setCursor(0,2);
        lcd.print("   SILAHKAN   ");
        lcd.setCursor(0,3);
        lcd.print(" MENGINPUT KEMBALI ");
    }
    else
    {
        goto Input_Baru;
    }
    delay(5000);
    exit(0);
}