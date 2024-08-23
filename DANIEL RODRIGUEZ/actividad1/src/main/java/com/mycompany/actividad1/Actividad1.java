
import java.util.Scanner;


public class Actividad1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int edad,sexo;
        System.out.print("Ingrese su nombre: ");
        String nombre = entrada.nextLine();
        System.out.print("Ingrese su apellido: ");
        String apellido = entrada.nextLine();
        System.out.print("Ingrese su edad: ");
        edad = entrada.nextInt();
        System.out.print("Ingrese su sexo (  Masculino (1) \n Femenino (2): ");
         sexo = entrada.nextInt();

        if (edad >= 18) {
            System.out.println("Es mayor de edad.");
        } else {
            System.out.println("Es menor de edad.");
        }
          switch(sexo){
              case 1:
              System.out.println(" es hombre");
              break;
              case 2:
              System.out.println("Es mujer");
             break;
       }
        
    }
}

