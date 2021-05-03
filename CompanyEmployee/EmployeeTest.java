import java.util.ArrayList;

public class EmployeeTest {

    private static ArrayList<Employee> employees = new ArrayList<Employee>();
    
    public static void main(String[] args){

        addEmployees();
        System.out.println(employees);

    }
    public static void addEmployees(){

        employees.add(new SalariedEmployee("Durmuş","Kartcı",1,1400));
        employees.add(new HourlyEmployee("Deniz","T.",2,25,14));
        employees.add(new ComissionEmployee("Melisa","S.",3,0.2,21000));
        employees.add(new BasePlusComissionEmployee("Kagan","O.",4,0.2,21000,3100));
        employees.add(new SalariedEmployee("Sinem","O.",5,1400));

    }
    
}
